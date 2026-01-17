build:
	./build.sh

install:
	uv sync

render-start:
	gunicorn task_manager.wsgi

migrate:
	uv run python manage.py migrate

dev:
	uv run manage.py runserver

lint:
	uv run ruff check .

format:
	uv run ruff check . --fix

collectstatic:
	uv run manage.py collectstatic  --noinput

test:
	uv run manage.py test