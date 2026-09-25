# Spot-check ratings

Upload the ratings file a spot-check page downloads (`ratings_spotcheck-YYYY-MM-DD.json`)
into this folder (GitHub: Add file → Upload files, commit to main). The next audio run
imports it with `python3 build/audio_maintenance.py import-ratings audio/spotchecks/*.json`:
every rated clip joins the regression suite, and a clip marked ✗ is re-recorded. Imported
files move to `imported/`.
