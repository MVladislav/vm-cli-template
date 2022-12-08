# Python CLI template

```sh
    MVladislav
```

[![Python DEV CI](https://github.com/MVladislav/vm-cli-template/actions/workflows/python-dev.yml/badge.svg?branch=develop)](https://github.com/MVladislav/vm-cli-template/actions/workflows/python-dev.yml)
[![Docker Build CI](https://github.com/MVladislav/vm-cli-template/actions/workflows/docker-build.yml/badge.svg?branch=develop)](https://github.com/MVladislav/vm-cli-template/actions/workflows/docker-build.yml)

---

- [Python CLI template](#python-cli-template)
  - [on clone this project](#on-clone-this-project)
    - [on update from this repo](#on-update-from-this-repo)
  - [install](#install)
    - [DEBUG `(PREFERRED)`](#debug-preferred)
    - [docker](#docker)
  - [code quality and git](#code-quality-and-git)
    - [pre-commit](#pre-commit)
    - [manual test run](#manual-test-run)

---

an template to copy to implement python with `setup.py` and `click` for **cli**.

## on clone this project

change to your project name:

```sh
$sed -i "s|vm_cli|<PROJECT_NAME>|g" .github/workflows/docker-build.yml 2>/dev/null
$sed -i "s|vm_cli|<PROJECT_NAME>|g" .github/workflows/python-dev.yml 2>/dev/null
$sed -i "s|vm_cli|<PROJECT_NAME>|g" scripts/setup-dev.sh 2>/dev/null
$sed -i "s|vm_cli|<PROJECT_NAME>|g" scripts/setup.sh 2>/dev/null
$sed -i "s|vm_cli|<PROJECT_NAME>|g" vm_cli/utils/config.py 2>/dev/null
$sed -i "s|vm_cli|<PROJECT_NAME>|g" .env_project 2>/dev/null
$sed -i "s|vm_cli|<PROJECT_NAME>|g" docker-compose.yaml 2>/dev/null
$sed -i "s|vm_cli|<PROJECT_NAME>|g" Dockerfile 2>/dev/null
$sed -i "s|vm_cli|<PROJECT_NAME>|g" pyproject.toml 2>/dev/null
$sed -i "s|vm_cli|<PROJECT_NAME>|g" setup.cfg 2>/dev/null
$sed -i "s|vm_cli|<PROJECT_NAME>|g" setup.py 2>/dev/null

$mv vm_cli <PROJECT_NAME>
$sed -i "s|vm_cli\b|<PROJECT_NAME>|g" .gitignore 2>/dev/null
$sed -i "s|vm_cli\b|<PROJECT_NAME>|g" .dockerignore 2>/dev/null
$sed -i "s|vm_cli\b|<PROJECT_NAME>|g" .pre-commit-config.yaml 2>/dev/null
$sed -i "s|vm_cli\b|<PROJECT_NAME>|g" docker-compose.yaml 2>/dev/null
$sed -i "s|vm_cli\b|<PROJECT_NAME>|g" pyproject.toml 2>/dev/null
$sed -i "s|vm_cli\b|<PROJECT_NAME>|g" setup.cfg 2>/dev/null
$sed -i "s|vm_cli\b|<PROJECT_NAME>|g" setup.py 2>/dev/null
$sed -i "s|vm_cli\b|<PROJECT_NAME>|g" tox.ini 2>/dev/null
$sed -i "s|vm_cli\b|<PROJECT_NAME>|g" .github/workflows/python-dev.yml 2>/dev/null
$sed -i "s|vm_cli\b|<PROJECT_NAME>|g" <PROJECT_NAME>/main.py 2>/dev/null
```

update version:

```sh
$sed -i "s|0.0.1|<NEW_VERSION>|g" .github/workflows/docker-build.yml 2>/dev/null
$sed -i "s|0.0.1|<NEW_VERSION>|g" .github/workflows/python-dev.yml 2>/dev/null
$sed -i "s|0.0.1|<NEW_VERSION>|g" app/utils/config.py 2>/dev/null
$sed -i "s|0.0.1|<NEW_VERSION>|g" .env_project 2>/dev/null
$sed -i "s|0.0.1|<NEW_VERSION>|g" docker-compose.yaml 2>/dev/null
$sed -i "s|0.0.1|<NEW_VERSION>|g" Dockerfile 2>/dev/null
$sed -i "s|0.0.1|<NEW_VERSION>|g" pyproject.toml 2>/dev/null
$sed -i "s|0.0.1|<NEW_VERSION>|g" setup.cfg 2>/dev/null
$sed -i "s|0.0.1|<NEW_VERSION>|g" setup.py 2>/dev/null
```

### on update from this repo

first commit your current work than copy main files

```sh
$export PATH_TO_VM_CLI=<TODO>
$cp -r "$PATH_TO_VM_CLI/.vscode/" ./
$cp -r "$PATH_TO_VM_CLI/vm_cli/main.py" ./vm_cli/
$cp -r "$PATH_TO_VM_CLI/vm_cli/utils/" ./vm_cli/
$cp -r "$PATH_TO_VM_CLI/.dockerignore" ./.dockerignore
$cp -r "$PATH_TO_VM_CLI/.env_project" ./.env_project
$cp -r "$PATH_TO_VM_CLI/.env_template" ./.env_template
$cp -r "$PATH_TO_VM_CLI/.gitignore" ./.gitignore
$cp -r "$PATH_TO_VM_CLI/.pre-commit-config.yaml" ./.pre-commit-config.yaml
$cp -r "$PATH_TO_VM_CLI/LICENCE" ./LICENCE
$cp -r "$PATH_TO_VM_CLI/SECURITY.md" ./SECURITY.md
$cp -r "$PATH_TO_VM_CLI/pyproject.toml" ./pyproject.toml
$cp -r "$PATH_TO_VM_CLI/requirements_dev.txt" ./requirements_dev.txt
$cp -r "$PATH_TO_VM_CLI/setup.cfg" ./setup.cfg
$cp -r "$PATH_TO_VM_CLI/setup.py" ./setup.py
$cp -r "$PATH_TO_VM_CLI/tox.ini" ./tox.ini
```

## install

```sh
$python3 -m pip install .
```

### DEBUG `(PREFERRED)`

```sh
$mkdir -p "$HOME/.vm_cli"
$python3 -m venv "$HOME/.vm_cli/venv"
$source "$HOME/.vm_cli/venv/bin/activate"
$python3 -m pip install .
```

### docker

run **docker-compose** build and up

```sh
$DOCKER_BUILDKIT=1 docker-compose build
$DOCKER_BUILDKIT=1 docker-compose up
```

---

## code quality and git

### pre-commit

run:

```sh
$git config --local core.hooksPath .git/hooks
$pre-commit install
```

### manual test run

```sh
$mkdir logs
$mypy app | tee logs/mypy.log
$python3 -m pylint --rcfile=setup.cfg `find app -regextype egrep -regex '(.*.py)$'` | tee logs/pylint.log
$flake8 app --count --select=E9,F63,F7,F82 --show-source --statistics | tee logs/flake8_1.log
$flake8 app --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics | tee logs/flake8_2.log
$python3 -m pytest --cov=tests | tee logs/pytest.log
$tox | tee logs/tox.log
```
