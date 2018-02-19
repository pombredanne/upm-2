import click
import logging
import sys
from os import getcwd

from cli import commands


log = logging.getLogger(__name__)
console_handler = logging.StreamHandler(sys.stderr)

# logging.basicConfig(level=logging.INFO)


@click.group()
@click.option('--debug', default=False, type=bool)
def main(debug):
    logging.basicConfig(level=logging.DEBUG)
    # if debug:
    #     logging.basicConfig(level=logging.DEBUG)


@main.command(help="create new package")
def init():
    path = getcwd()
    commands.initialize_package(path)


@main.command()
# @click.argument('path')
def install():
    path = getcwd()
    commands.install_package(path)


@main.command()
def publish():
    pass


if __name__ == '__main__':
    main()