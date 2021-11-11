"""
    will setup the project, by install it local
    with needed dependencies
"""
import logging
import re
import sys
import unicodedata
from subprocess import check_call

from setuptools import find_packages, setup
from setuptools.command.develop import develop
from setuptools.command.install import install

try:
    from starlette.config import Config
except ImportError:
    source_to_install = 'starlette'
    logging.log(logging.CRITICAL, f'Failed to Import {source_to_install}')
    try:
        # choice = input(f'[*] Attempt to Auto-istall {source_to_install}? [y/N]')
        choice = 'y'
    except KeyboardInterrupt:
        logging.log(logging.INFO, 'User Interrupted Choice')
        sys.exit(1)
    if choice.strip().lower()[0] == 'y':
        logging.log(logging.INFO, f'Attempting to Install {source_to_install}')
        sys.stdout.flush()
        try:
            import subprocess
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", source_to_install])
            from starlette.config import Config
            logging.log(logging.INFO, '[DONE]')
        except Exception:
            logging.log(logging.CRITICAL, '[FAIL]')
            sys.exit(1)
    elif choice.strip().lower()[0] == 'n':
        logging.log(logging.INFO, 'User Denied Auto-install')
        sys.exit(1)
    else:
        logging.log(logging.WARNING, 'Invalid Decision')
        sys.exit(1)

config_project = Config('.env_project')
PROJECT_NAME: str = config_project('PROJECT_NAME')

# ------------------------------------------------------------------------------
#
# POST installer
#
# ------------------------------------------------------------------------------


class PostDevelopCommand(develop):
    """
        Post-installation for development mode.
    """

    def run(self):
        check_call(['/bin/bash', './scripts/setup-dev.sh'])
        develop.run(self)


class PostInstallCommand(install):
    """
        Post-installation for installation mode.
    """

    def run(self):
        check_call(['/bin/bash', './scripts/setup.sh'])
        install.run(self)

# ------------------------------------------------------------------------------
#
# TEXTs and requirements
#
# ------------------------------------------------------------------------------


def read_long_description():
    """
        load the readme to add as long description
    """
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
    return long_description


def read_requirements():
    """
        load and read the dependencies
        from the requirements.txt file
        and return them as a list
    """
    with open("requirements.txt", "r", encoding="utf-8") as req:
        requirements = req.read().split("\n")
    return requirements

# ------------------------------------------------------------------------------
#
# HELPER
#
# ------------------------------------------------------------------------------


def slugify(value, allow_unicode=False):
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    return re.sub(r'[-\s]+', '-', re.sub(r'[^\w\s-]', '', value.lower())).strip('-_')

# ------------------------------------------------------------------------------
#
# SETUP
#
# ------------------------------------------------------------------------------


PROJECT_NAME_SLUG = slugify(PROJECT_NAME)

setup(
    name=PROJECT_NAME,
    version='0.0.1',
    license='GNU AGPLv3',
    description=PROJECT_NAME,
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    author='MVladislav',
    author_email='info@mvladislav.online',
    # package_dir={"": "app"},
    # packages=find_packages(where="app"),
    packages=find_packages(),
    data_files=[('', ['requirements.txt', 'scripts/setup.sh', 'scripts/setup-dev.sh'])],
    include_package_data=True,
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    },
    install_requires=read_requirements(),
    python_requires=">=3.8",
    zip_safe=True,
    entry_points=f"""
        [console_scripts]
        {PROJECT_NAME_SLUG}=app.main:cli
    """,
)
