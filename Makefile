.PHONY: validate validate-changed index build quick check-furigana check-kanji stats report clean full word-lookup note-scores check-symmetry check-clusters priorities

validate:
	python3 build/validate.py

validate-changed:
	python3 build/validate.py --changed-only

index:
	python3 build/update_indexes.py

build: validate index
	python3 build/build_flat.py

quick: validate index
	python3 build/build_flat.py --quick

word-lookup:
	python3 build/generate_word_lookup.py

check-furigana:
	python3 build/find_missing_furigana.py

check-kanji:
	python3 build/verify_kanji_index.py

stats:
	python3 build/tag_statistics.py

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

full: clean build
