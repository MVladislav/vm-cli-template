import click

from ..cli import Context, pass_context


@click.group(invoke_without_command=True)
@pass_context
def cli(ctx: Context):
    '''
        This a command
    '''
    ctx.utils.logging.info(ctx.verbose)
    # ctx.<...> = <...>


@cli.command()
@pass_context
def test(ctx: Context):
    '''
        This is a test
    '''
    ctx.utils.logging.info(ctx.verbose)
