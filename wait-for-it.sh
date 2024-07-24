#!/bin/sh
# wait-for-it.sh

set -e

host="$1"
shift
cmd="$@"

until curl -sSf "http://$host" >/dev/null; do
  >&2 echo "Selenium Grid is unavailable - waiting"
  sleep 1
done

>&2 echo "Selenium Grid is up - executing command"
exec $cmd
