.PHONY: test install-hooks metrics-page validate validate-changed index build quick check-furigana check-kanji stats report clean full word-lookup note-scores check-symmetry check-clusters priorities audit-fields assemble-fields audit-scenarios assemble-scenarios audit-tiers consistency lock-status queue-populate queue-status queue-cleanup orchestrate orchestrate-status orchestrate-stop monitor

validate:
	python3 build/validate.py

validate-changed:
	python3 build/validate.py --changed-only

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

queue-populate:
	python3 pipeline/task_queue.py populate --all

queue-status:
	python3 pipeline/task_queue.py status

queue-cleanup:
	python3 pipeline/task_queue.py cleanup

orchestrate:
	python3 pipeline/orchestrator.py start

orchestrate-status:
	python3 pipeline/orchestrator.py status

orchestrate-stop:
	python3 pipeline/orchestrator.py stop

monitor:
	python3 pipeline/monitor.py

full: clean build

test:
	python3 -m unittest discover -s build/tests -t .

install-hooks:
	git config core.hooksPath .githooks
	@echo "pre-commit hook active (.githooks/pre-commit)"

metrics-page:
	python3 pipeline/metrics_report.py
