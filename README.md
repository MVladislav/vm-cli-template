# Python CLI template

```sh
    MVladislav
```

---

- [Python CLI template](#python-cli-template)
  - [install](#install)
    - [DEBUG](#debug)
  - [run](#run)
    - [docker](#docker)

---

an template to copy to implement python with `setup.py` and `click` for **cli**.

## install

```sh
$pip3 install starlette && pip3 install .
```

### DEBUG

```sh
$python3 -m venv ./venv
$source venv/bin/activate
$pip3 install starlette && pip3 install -v --editable .
```

## run

### docker

run **docker-compose** build and up

```sh
$DOCKER_BUILDKIT=1 docker-compose build
$DOCKER_BUILDKIT=1 docker-compose up
```
