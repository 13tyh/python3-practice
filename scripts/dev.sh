#!/usr/bin/env bash
set -euo pipefail

command="${1:-build}"

case "$command" in
  up)
    docker compose up -d --build
    ;;
  shell)
    docker compose exec app bash
    ;;
  lint)
    poetry run lint
    ;;
  fmt)
    poetry run fmt "${@:2}"
    ;;
  build)
    poetry run build
    ;;
  *)
    echo "usage: ./scripts/dev.sh [up|shell|lint|fmt|build]"
    exit 2
    ;;
esac

