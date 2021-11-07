# Python CLI template

```sh
    MVladislav
```

---

- [Python CLI template](#python-cli-template)
  - [install](#install)
    - [DEBUG `(PREFERRED)`](#debug-preferred)
  - [run](#run)
    - [docker](#docker)

---

an template to copy to implement python with `setup.py` and `click` for **cli**.

## install

```sh
$pip3 install starlette && pip3 install .
```

### DEBUG `(PREFERRED)`

```sh
$mkdir -p "$HOME/.vm_cli"
$python3 -m venv "$HOME/.vm_cli/venv"
$source "$HOME/.vm_cli/venv/bin/activate"
$pip3 install -v --editable .
```

## run

### docker

run **docker-compose** build and up

```sh
$DOCKER_BUILDKIT=1 docker-compose build
$DOCKER_BUILDKIT=1 docker-compose up
```
