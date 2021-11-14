# Python CLI template

```sh
    MVladislav
```

[![Python DEV CI](https://github.com/MVladislav/vm-cli-template/actions/workflows/python-dev.yml/badge.svg?branch=develop)](https://github.com/MVladislav/vm-cli-template/actions/workflows/python-dev.yml)
[![Docker Build CI](https://github.com/MVladislav/vm-cli-template/actions/workflows/docker-build.yml/badge.svg?branch=develop)](https://github.com/MVladislav/vm-cli-template/actions/workflows/docker-build.yml)

---

- [Python CLI template](#python-cli-template)
  - [on clone this project](#on-clone-this-project)
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
sed -i "s|vm_cli|<PROJECT_NAME>|g" .github/workflows/docker-build.yml 2>/dev/null
sed -i "s|vm_cli|<PROJECT_NAME>|g" .github/workflows/python-dev.yml 2>/dev/null
sed -i "s|vm_cli|<PROJECT_NAME>|g" scripts/setup-dev.sh 2>/dev/null
sed -i "s|vm_cli|<PROJECT_NAME>|g" scripts/setup.sh 2>/dev/null
sed -i "s|vm_cli|<PROJECT_NAME>|g" app/utils/config.py 2>/dev/null
sed -i "s|vm_cli|<PROJECT_NAME>|g" .env_project 2>/dev/null
sed -i "s|vm_cli|<PROJECT_NAME>|g" docker-compose.yaml 2>/dev/null
sed -i "s|vm_cli|<PROJECT_NAME>|g" Dockerfile 2>/dev/null
sed -i "s|vm_cli|<PROJECT_NAME>|g" pyproject.toml 2>/dev/null
sed -i "s|vm_cli|<PROJECT_NAME>|g" setup.cfg 2>/dev/null
sed -i "s|vm_cli|<PROJECT_NAME>|g" setup.py 2>/dev/null
```

update version:

```sh
sed -i "s|0.0.1|<NEW_VERSION>|g" .github/workflows/docker-build.yml 2>/dev/null
sed -i "s|0.0.1|<NEW_VERSION>|g" .github/workflows/python-dev.yml 2>/dev/null
sed -i "s|0.0.1|<NEW_VERSION>|g" app/utils/config.py 2>/dev/null
sed -i "s|0.0.1|<NEW_VERSION>|g" .env_project 2>/dev/null
sed -i "s|0.0.1|<NEW_VERSION>|g" docker-compose.yaml 2>/dev/null
sed -i "s|0.0.1|<NEW_VERSION>|g" Dockerfile 2>/dev/null
sed -i "s|0.0.1|<NEW_VERSION>|g" pyproject.toml 2>/dev/null
sed -i "s|0.0.1|<NEW_VERSION>|g" setup.cfg 2>/dev/null
sed -i "s|0.0.1|<NEW_VERSION>|g" setup.py 2>/dev/null
```

## install

```sh
$python3 -m pip install .
# $pip3 install .
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
$mypy app
$flake8 app
$pytest --cov=tests
$tox
```
