import click
from src.cli import pass_context
from src.abs.game import Game


@click.command('generate', short_help='Show a view of 9*9 sudoku map')
@pass_context
def cli(ctx):
    game = Game(
        with_coordinate=True, step_check=True, mode='easy',
        random=6, mutiple=18, lmutiple=8)
    game.fill_random()
    game.flush()
