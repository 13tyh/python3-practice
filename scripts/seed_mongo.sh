#!/usr/bin/env bash
set -euo pipefail

docker compose exec mongo mongosh /docker-entrypoint-initdb.d/01_seed.js
