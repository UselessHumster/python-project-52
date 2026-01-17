build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

migrate:
	uv run python manage.py migrate

create-venv:
	@pipx install uv
	@uv venv --python=python3.10

package-install:
	@echo "Installing package: $(PACKAGE)-$(VERSION)-py3-none-any.whl"
	@echo "To override installation please type: make package-install PACKAGE=name:string VERSION=version:string"
	@uv tool install dist/$(PACKAGE)-$(VERSION)-py3-none-any.whl

install: create-venv build package-install

dev:
	uv run manage.py runserver

lint:
	uv run ruff check .

format:
	uv run ruff check . --fix


collectstatic:
	uv run manage.py collectstatic  --noinput