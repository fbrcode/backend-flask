# Poetry + Flask

This is a template for a Flask application using Poetry for dependency management.

## Getting Started

### Prerequisites

- Python 3.10+
- Poetry

## Project installation sequence

```sh
poetry new --name=app --src backend-flask

cd backend-flask

git init

cat pyproject.toml
```

```txt
[tool.poetry]
name = "app"
version = "0.1.0"
description = ""
authors = ["fbrcode <fabio.bressler@gmail.com>"]
readme = "README.md"
packages = [{include = "app", from = "src"}]

[tool.poetry.dependencies]
python = "^3.10"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

poetry config virtualenvs.in-project true --local

cat poetry.toml

```txt
[virtualenvs]
in-project = true
```

```sh
poetry config --list

poetry shell

poetry add flask@2.2.2

echo ".venv" >> .gitignore

tree -a
```

```txt
.
├── .git
│   └── ...
├── .gitignore
├── .venv
│   └── ...
├── README.md
├── poetry.lock
├── poetry.toml
├── pyproject.toml
├── src
│   └── app
│       └── __init__.py
└── tests
    └── __init__.py
```

Run server

```sh
poetry shell # enable venv
python -m src.app # run app
# or
poetry run python -m src.app
# or
export FLASK_APP=src.app && export FLASK_DEBUG=1 && flask run # not working
```

Check endpoints

```sh
curl http://localhost:5000/health -vvv
```

```txt
OK
```

```sh
curl http://localhost:5000/users -vvv
```

```json
[
  {
    "name": "John Doe"
  },
  {
    "name": "Jane Doe"
  }
]
```

```sh
curl http://localhost:5000/users \
-H 'Content-Type: application/json' \
-d '{ "name": "Fabio Test" }' -vvv
```
