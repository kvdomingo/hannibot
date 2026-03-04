#!/usr/bin/env bash

set -euxo pipefail

uv sync --dev --all-groups
uv run alembic upgrade head

exec uv run watchmedo auto-restart --directory ./bot/ --directory ./common/ --recursive -- python -m bot
