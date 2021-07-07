import os

import click

from .config import PROJECT, VERBOSE, VERSION
from .utilities.utils import Utils

# ------------------------------------------------------------------------------
#
#
#
# ------------------------------------------------------------------------------


class Context:

    def __init__(self):
        self.verbose = VERBOSE

        self.utils = None

# ------------------------------------------------------------------------------
#
#
#
# ------------------------------------------------------------------------------


class ComplexCLI(click.MultiCommand):
    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(os.path.join(os.path.dirname(__file__), "./commands")):
            if filename.endswith(".py") and not filename.startswith("__"):
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        try:
            mod = __import__(f"{PROJECT}.commands.{name}", None, None, ["cli"])
            return mod.cli
        except ImportError as e:
            pass
            print(e)


# ------------------------------------------------------------------------------
#
#
#
# ------------------------------------------------------------------------------

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'], ignore_unknown_options=True, auto_envvar_prefix="COMPLEX")

pass_context = click.make_pass_decorator(Context, ensure=True)


@click.command(cls=ComplexCLI, context_settings=CONTEXT_SETTINGS)
@click.version_option(VERSION)
@click.option('-v', '--verbose', help='Enables verbose mode', default=None, count=True)
@pass_context
def cli(ctx, verbose):
    """Welcome to vm-hack"""
    if verbose != None:
        ctx.verbose = verbose
    ctx.utils = Utils(ctx)
