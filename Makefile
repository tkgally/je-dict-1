.PHONY: gate mechanical audio-deps audio-status audio-regression test install-hooks metrics-page validate validate-articles validate-changed index build quick check-furigana check-kanji report clean full word-lookup note-scores check-symmetry check-clusters priorities audit-fields assemble-fields audit-scenarios assemble-scenarios audit-tiers consistency lock-status

validate:
	python3 build/validate.py
	python3 build/validate_articles.py

validate-articles:
	python3 build/validate_articles.py

validate-changed:
	python3 build/validate.py --changed-only

# Exactly the checks .github/workflows/validate.yml runs on a PR. Run it before
# every push: a PR that fails here fails CI. --changed-only compares against
# origin/main, so main must be fetched (the fetch is here).
gate:
	python3 -m unittest discover -s build/tests -t .
	python3 build/validate.py
	python3 build/validate_articles.py
	git fetch -q origin main
	python3 build/validate.py --changed-only --ratchet
	python3 build/validate_tags.py --check-no-new-unknown
	python3 build/check_note_headers.py --gate
	python3 build/check_link_baseform.py --gate
	python3 build/check_link_homophones.py --gate
	python3 build/check_no_binaries.py

# The deterministic pass after changing entries (CLAUDE.md, routine2.md §3):
#   make mechanical IDS=00426,31073
mechanical:
	@test -n "$(IDS)" || { echo "usage: make mechanical IDS=<comma-separated entry IDs>"; exit 2; }
	python3 build/normalize_notes.py --ids $(IDS) --apply
	python3 build/auto_link.py --ids $(IDS) --apply --confirm-real-entries
	python3 build/harvest_crossrefs.py --ids $(IDS) --apply
	@for i in $$(echo "$(IDS)" | tr ',' ' '); do python3 build/validate.py --id $$i || exit 1; done

index: validate
	python3 build/update_indexes.py
	python3 build/update_kanji_index.py

build: index
	python3 build/build_flat.py

quick: index
	python3 build/build_flat.py --quick

word-lookup:
	python3 build/generate_word_lookup.py

check-furigana:
	python3 build/find_missing_furigana.py

check-kanji:
	python3 build/verify_kanji_index.py

report:
	python3 build/report.py

clean:
	rm -rf docs_build_temp/ docs_backup/

note-scores:
	python3 build/score_note_quality.py --summary

check-symmetry:
	python3 build/find_merge_candidates.py --asymmetry-only

check-clusters:
	python3 build/check_semantic_clusters.py --summary

priorities:
	python3 build/prioritize_polishing.py

audit-fields:
	python3 build/audit_semantic_field.py --summary

assemble-fields:
	python3 build/assemble_semantic_fields.py

audit-scenarios:
	python3 build/analyze_scenarios.py --summary

assemble-scenarios:
	python3 build/assemble_learner_scenarios.py

audit-tiers:
	python3 build/audit_tiers.py --outliers

consistency:
	python3 build/check_consistency.py

lock-status:
	python3 build/entry_lock.py status

full: clean build

test:
	python3 -m unittest discover -s build/tests -t .

install-hooks:
	git config core.hooksPath .githooks
	@echo "pre-commit hook active (.githooks/pre-commit)"

metrics-page:
	python3 pipeline/metrics_report.py

# Example audio (AUDIO_WORKFLOW.md). audio-deps: MeCab/UniDic and the MP3 encoder.
audio-deps:
	pip install -q -U setuptools || true
	pip install -q -r build/requirements-audio.txt

audio-status:
	python3 build/audio_pipeline.py status

# Rerun the checks on the 163 regression clips (about $0.25); required before any workflow change.
audio-regression:
	python3 build/audio_regression.py
