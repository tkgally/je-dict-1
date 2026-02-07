.PHONY: validate index build quick check-furigana check-kanji stats report clean full word-lookup

validate:
	python3 build/validate.py

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

full: clean build
