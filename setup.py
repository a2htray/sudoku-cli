from setuptools import setup

setup(
    name='sudoku-cli',
    version='1.0',
    packages=[
        'src',
        'src.commands',
        'src.abs'
    ],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        sudokucli=src.cli:cli
    ''',
)