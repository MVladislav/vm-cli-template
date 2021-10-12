import logging
import sys

import click

from ..main import Context, pass_context
from ..service.test_service import TestService

default_split_by = ';'

# ------------------------------------------------------------------------------
#
#
#
# ------------------------------------------------------------------------------


@click.group(invoke_without_command=True)
@pass_context
def cli(ctx: Context):
    '''
        This a command
    '''
    ctx.service = TestService(ctx)

# ------------------------------------------------------------------------------
#
#
#
# ------------------------------------------------------------------------------


@cli.command()
@click.option('-d', '--host', type=str, help='host to scan for', required=True)
@click.option('-p', '--port', type=int, help='define port [443]', default=443)
@click.option('-o', '--options', type=str, help=f'options to scan with (seperated by "{default_split_by}") [None]', default=None)
@click.option('-oa', '--options_append', is_flag=True, help='append new options to existing option list')
@pass_context
def test(ctx: Context, host, port, options, options_append):
    '''
        This is a test
    '''
    service: TestService = ctx.service
    try:
        logging.log(logging.INFO, f"this is a service call")

        options = service.utils.define_option_list(options=options, options_append=options_append, default_split_by=default_split_by)

    except KeyboardInterrupt as k:
        logging.log(logging.DEBUG, f"process interupted! ({k})")
        sys.exit(5)
    except Exception as e:
        logging.log(logging.CRITICAL, e)
        sys.exit(2)


# ------------------------------------------------------------------------------
#
#
#
# ------------------------------------------------------------------------------
