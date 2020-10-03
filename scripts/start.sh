#! /bin/bash
set -e

until PGPASSWORD=$POSTGRES_PASS psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -d "$POSTGRES_NAME" -c '\q'; do
  echo "Postgres is unavailable - sleeping"
  sleep 1
done
  
echo "Postgres is up"
echo "Executing migrations"
alembic upgrade head
echo "Starting server"
uvicorn source.main:app --reload --host 0.0.0.0