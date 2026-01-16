# je-dict-1 Code Review: Diagnoses + Proposed Patches

This file includes the diagnoses and concrete patch proposals. Patch blocks are presented as unified diffs; apply selectively.

## High

### 1) Cross-reference migration drops distinct refs by reading
**File:** `je-dict-1-main/build/migrate_cross_references.py` (around `normalize_cross_references`)

**Problem**
Deduplication uses only `reading`, so distinct references that share a reading but differ in `type`, `headword`, or `label` are collapsed during migration.

**Impact**
Data loss and incorrect cross-reference semantics after migration.

**Proposed fix**
Deduplicate by a composite key of `(type, reading, headword, label)` (or at minimum include `type` + `headword`).

```diff
--- a/je-dict-1-main/build/migrate_cross_references.py
+++ b/je-dict-1-main/build/migrate_cross_references.py
@@ -83,7 +83,7 @@ def normalize_cross_references(
     Returns:
         List of structured cross-references with duplicates removed
     """
     normalized = []
-    seen_readings = set()
+    seen_keys = set()
@@ -108,15 +108,18 @@ def normalize_cross_references(
-        # Check for duplicates by reading
-        reading = structured.get('reading', '')
-        if reading and reading in seen_readings:
-            # Skip duplicate
-            continue
-
-        if reading:
-            seen_readings.add(reading)
+        # Check for duplicates by composite identity
+        reading = structured.get('reading', '')
+        ref_type = structured.get('type', '')
+        headword = structured.get('headword', '')
+        label = structured.get('label', '')
+        key = (ref_type, reading, headword, label)
+        if reading and key in seen_keys:
+            continue
+
+        if reading:
+            seen_keys.add(key)

         normalized.append(structured)
```

---

### 2) Pending page build crashes when candidate fields are null
**File:** `je-dict-1-main/build/build_flat.py` (around `generate_pending_page`)

**Problem**
`html.escape()` is called directly on `candidate.get('reading')` and `candidate.get('notes')`. If either is `None`, Python raises `TypeError`.

**Impact**
Full build failure if any candidate has missing `reading` or `notes`.

**Proposed fix**
Coerce to `''` before escaping.

```diff
--- a/je-dict-1-main/build/build_flat.py
+++ b/je-dict-1-main/build/build_flat.py
@@ -797,9 +797,9 @@ def generate_pending_page(candidates: list) -> str:
     )
 
     for candidate in sorted_candidates:
-        word = html.escape(candidate.get('word', ''))
-        reading = html.escape(candidate.get('reading', ''))
-        notes = html.escape(candidate.get('notes', ''))
+        word = html.escape(candidate.get('word') or '')
+        reading = html.escape(candidate.get('reading') or '')
+        notes = html.escape(candidate.get('notes') or '')
```

## Medium

### 3) Self-reference allowed when headword omitted
**File:** `je-dict-1-main/build/validate.py` (around `validate_structured_cross_reference`)

**Problem**
Self-reference detection only fires when *both* reading and headword match. If a cross-reference omits headword but uses the same reading, it passes validation.

**Impact**
Self-links can appear in output or be unresolved, depending on build rules.

**Proposed fix**
If reading matches current entry and headword is missing, treat as self-reference. If you want to allow same-reading refs, require explicit headword.

```diff
--- a/je-dict-1-main/build/validate.py
+++ b/je-dict-1-main/build/validate.py
@@ -172,7 +172,13 @@ def validate_structured_cross_reference(ref: dict, entry_reading: str, entry_headword: str) -> list[str]:
-        if ref['reading'] == entry_reading and ref_headword == entry_headword:
-            errors.append(f"Self-reference not allowed: '{ref['reading']}' with headword '{ref_headword}'")
+        if ref['reading'] == entry_reading:
+            # Require headword for same-reading refs; otherwise treat as self-reference.
+            if not ref_headword:
+                errors.append(f"Self-reference not allowed: reading '{ref['reading']}' without headword")
+            elif ref_headword == entry_headword:
+                errors.append(f"Self-reference not allowed: '{ref['reading']}' with headword '{ref_headword}'")
```

---

### 4) Schema rejects legacy cross-reference format still supported in code
**File:** `je-dict-1-main/build/schema.json`

**Problem**
Schema allows only object cross-references, but code still accepts legacy string refs.

**Impact**
Schema validation fails for valid legacy data; tooling is inconsistent.

**Proposed fix**
Allow either string or object until migration is complete.

```diff
--- a/je-dict-1-main/build/schema.json
+++ b/je-dict-1-main/build/schema.json
@@ -103,25 +103,38 @@
     "cross_references": {
       "type": "array",
       "items": {
-        "type": "object",
-        "required": ["type", "reading"],
-        "properties": {
-          "type": {
-            "type": "string",
-            "enum": ["pair", "synonym", "antonym", "keigo", "related", "see_also", "contrast"],
-            "description": "Relationship type"
-          },
-          "reading": {
-            "type": "string",
-            "pattern": "^[ぁ-んー]+$",
-            "description": "Hiragana reading of target word (primary lookup key)"
-          },
-          "headword": {
-            "type": "string",
-            "description": "Display form with kanji/furigana (optional, for display before entry exists)"
-          },
-          "label": {
-            "type": "string",
-            "description": "Short label like 'intransitive', 'honorific', 'formal'"
-          }
-        }
+        "oneOf": [
+          {
+            "type": "string",
+            "description": "Legacy entry ID reference"
+          },
+          {
+            "type": "object",
+            "required": ["type", "reading"],
+            "properties": {
+              "type": {
+                "type": "string",
+                "enum": ["pair", "synonym", "antonym", "keigo", "related", "see_also", "contrast"],
+                "description": "Relationship type"
+              },
+              "reading": {
+                "type": "string",
+                "pattern": "^[ぁ-んー]+$",
+                "description": "Hiragana reading of target word (primary lookup key)"
+              },
+              "headword": {
+                "type": "string",
+                "description": "Display form with kanji/furigana (optional, for display before entry exists)"
+              },
+              "label": {
+                "type": "string",
+                "description": "Short label like 'intransitive', 'honorific', 'formal'"
+              }
+            }
+          }
+        ]
       },
       "description": "Array of cross-references to related entries"
     },
```

---

### 5) Search results render unescaped gloss text
**File:** `je-dict-1-main/docs/search.js` and `je-dict-1-main/build/build_flat.py`

**Problem**
Search results use `innerHTML` and interpolate gloss without escaping. If a gloss contains `<`/`&` it can break markup or inject HTML.

**Impact**
Broken UI or XSS in generated static site (even if data is trusted, a malformed gloss can break markup).

**Proposed fix (preferred)**
Escape gloss when generating `search-index.js`, so the client only renders safe strings.

```diff
--- a/je-dict-1-main/build/build_flat.py
+++ b/je-dict-1-main/build/build_flat.py
@@ -839,7 +839,7 @@ def generate_search_index(entries: list) -> str:
         # Store minimal entry data for display
         entries_data[entry_id] = {
             'id': entry_id,
             'headword': process_furigana(headword),
             'reading': reading,
             'romaji': hiragana_to_romaji(reading),
-            'gloss': gloss,
+            'gloss': html.escape(gloss),
             'folder': folder,
             'prefix': prefix
         }
```

**Alternative fix (JS side)**
Stop using `innerHTML` and build nodes with `textContent`.

```diff
--- a/je-dict-1-main/docs/search.js
+++ b/je-dict-1-main/docs/search.js
@@ -73,16 +73,34 @@
     } else {
         resultsHeading.textContent = results.length + ' result' + (results.length === 1 ? '' : 's') + ' for "' + query + '"';
-        resultsList.innerHTML = results.map(function(entry) {
-            const folder = entry.folder || 'a';
-            const prefix = entry.prefix || entry.id.substring(0, 2);
-            return '<a href="entries/' + folder + '/' + prefix + '/' + entry.id + '.html" class="result-item">' +
-                '<div class="result-headword">' + entry.headword + '</div>' +
-                '<div class="result-reading">' + entry.reading + '</div>' +
-                '<div class="result-gloss">' + entry.gloss + '</div>' +
-            '</a>';
-        }).join('');
+        resultsList.innerHTML = '';
+        results.forEach(function(entry) {
+            const folder = entry.folder || 'a';
+            const prefix = entry.prefix || entry.id.substring(0, 2);
+
+            const link = document.createElement('a');
+            link.href = 'entries/' + folder + '/' + prefix + '/' + entry.id + '.html';
+            link.className = 'result-item';
+
+            const headword = document.createElement('div');
+            headword.className = 'result-headword';
+            headword.innerHTML = entry.headword;
+
+            const reading = document.createElement('div');
+            reading.className = 'result-reading';
+            reading.textContent = entry.reading;
+
+            const gloss = document.createElement('div');
+            gloss.className = 'result-gloss';
+            gloss.textContent = entry.gloss;
+
+            link.appendChild(headword);
+            link.appendChild(reading);
+            link.appendChild(gloss);
+            resultsList.appendChild(link);
+        });
     }
 }
```

## Low

### 6) Furigana toggle not included on pending.html
**File:** `je-dict-1-main/build/build_flat.py`

**Problem**
`generate_pending_page()` omits the furigana toggle script, so the toggle in the header is inert on `pending.html`.

**Impact**
Inconsistent UX across pages.

**Proposed fix**
Append `generate_furigana_script()` like other pages.

```diff
--- a/je-dict-1-main/build/build_flat.py
+++ b/je-dict-1-main/build/build_flat.py
@@ -814,6 +814,7 @@ def generate_pending_page(candidates: list) -> str:
     html_parts.append('''
         <footer>
             <p><a href="index.html">Japanese-English Learner's Dictionary</a></p>
         </footer>
     ''')
+    html_parts.append(generate_furigana_script())
     html_parts.append('</body>')
     html_parts.append('</html>')
```

## Optional Improvements

### Validator performance
**File:** `je-dict-1-main/build/validate.py`

**Idea**
Initialize `Draft7Validator` once and reuse it instead of creating it per entry. This reduces per-file overhead.

```diff
--- a/je-dict-1-main/build/validate.py
+++ b/je-dict-1-main/build/validate.py
@@ -27,6 +27,7 @@
 def load_schema(schema_path: Path) -> dict:
     """Load the JSON schema."""
     with open(schema_path, 'r', encoding='utf-8') as f:
         return json.load(f)
+
@@ -34,7 +35,7 @@ def validate_entry_file(file_path: Path, schema: dict, all_ids: set) -> tuple[list[str], dict | None]:
     """
     Validate a single entry file.
@@ -48,7 +49,7 @@ def validate_entry_file(file_path: Path, schema: dict, all_ids: set) -> tuple[list[str], dict | None]:
     except json.JSONDecodeError as e:
         return [f"Invalid JSON: {e}"], None
 
     # Validate against schema
-    validator = Draft7Validator(schema)
+    validator = Draft7Validator(schema)
     schema_errors = list(validator.iter_errors(entry))
```

If you want this, we can push the validator construction up into `validate_all_entries()` and pass it into `validate_entry_file()`.
