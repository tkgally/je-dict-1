#!/bin/bash
# Automatic backup script for je-dict-1 project
# Creates timestamped backups of all project files

PROJECT_DIR="/home/user/je-dict-1"
BACKUP_DIR="$PROJECT_DIR/backups"

# Ensure backup directory exists
mkdir -p "$BACKUP_DIR"

# Create timestamp
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Create backup archive (excluding .git, backups, node_modules, etc.)
tar --exclude='.git' \
    --exclude='backups' \
    --exclude='node_modules' \
    --exclude='__pycache__' \
    --exclude='*.pyc' \
    -czf "$BACKUP_DIR/je-dict-1_${TIMESTAMP}.tar.gz" \
    -C "$(dirname "$PROJECT_DIR")" "$(basename "$PROJECT_DIR")" 2>/dev/null

# Keep only the last 20 backups to save space
cd "$BACKUP_DIR"
ls -t je-dict-1_*.tar.gz 2>/dev/null | tail -n +21 | xargs -r rm --

echo "Backup created: $BACKUP_DIR/je-dict-1_${TIMESTAMP}.tar.gz" >&2
exit 0
