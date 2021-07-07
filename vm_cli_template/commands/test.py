import click

from ..cli import pass_context


@click.group(invoke_without_command=True)
@pass_context
def cli(ctx):
    '''
        This a command
    '''
    ctx.utils.logging.info(ctx.verbose)
    # ctx.<...> = <...>


@cli.command()
@pass_context
def test(ctx):
    '''
        This is a test
    '''
    ctx.utils.logging.info(ctx.verbose)
