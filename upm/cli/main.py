import click
import logging
import sys
from os import getcwd
from os.path import abspath

from cli import commands

log = logging.getLogger(__name__)
console_handler = logging.StreamHandler(sys.stderr)


# logging.basicConfig(level=logging.INFO)


@click.group()
@click.option('--debug', is_flag=True)
def main(debug):
    logging.basicConfig(level=logging.DEBUG)
    # if debug:
    #     logging.basicConfig(level=logging.DEBUG)


@main.command(help="create new package")
def init():
    path = getcwd()
    commands.initialize_package(path)


@main.command()
@click.option('--dev', is_flag=True)
@click.argument('folder', nargs=1, type=click.Path(exists=True), required=False)
def install(folder, dev):
    if folder:
        folder = abspath(folder)
    path = getcwd()
    commands.install_package(path, folder, dev)

@main.command()
def daemon():
    path = getcwd()
    commands.upm_set_daemon(path)

@main.command()
def publish():
    pass


if __name__ == '__main__':
    main()
