#!/bin/sh
CURRENT_DIR=$("pwd")
PROJECT_DIR="$(cd .. && pwd)"
MAIN_DIR="$(cd ../.. && pwd)"
git --git-dir="$PROJECT_DIR/.git" --work-tree="$PROJECT_DIR" pull origin main &&
"$MAIN_DIR/venv/bin/pip" install -r "$PROJECT_DIR/requirements/production.txt"
"$MAIN_DIR/venv/bin/python" "$PROJECT_DIR/manage.py" collectstatic --noinput
"$MAIN_DIR/venv/bin/python" "$PROJECT_DIR/manage.py" migrate && "$CURRENT_DIR/reload.sh"
# shellcheck disable=SC2039
echo -e "\033[0;32m ------ TASKS ------ \n1.Pulled \n2.Installed requirements \n3.Collected static files \n4.Migrated \n5.Reloaded\033[0m"
