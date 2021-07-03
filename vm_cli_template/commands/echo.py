import click


class Context:

    def __init__(self) -> None:
        pass

@click.group()
@click.pass_context
def cli(ctx):
    """This is a echo command"""
    ctx.obj = Context()
    ctx.obj.is_loaded = "Yes, this works"

@cli.command()
@click.pass_context
def ls(ctx):
    """This is ls"""
    print(ctx.obj.is_loaded)
