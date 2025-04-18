import argparse
import os
from .new_project.init import init
from .new_project.new import new

def main():
    args = parse()
    if args.command == "init":
        init(args)
        print(f"Initialized new project in {os.getcwd}")
    elif args.command == "new":
        new(args)


def parse():
    parser = argparse.ArgumentParser(
        prog="Serka",
        description="A Python Scaffolding Tool"
    )
    subparsers = parser.add_subparsers(title="commands", dest="command")

    init_parser = subparsers.add_parser(name="init")
    init_parser.add_argument('-a', '--author', nargs=1, type=str, default=None)
    init_parser.add_argument('-e', '--email', nargs=1, type=str, default=None)
    init_parser.add_argument('-f', '--force', action='store_true', default=False)
    init_parser.add_argument('-v', '--verbose', action='store_true', default=False)
    init_parser.add_argument('-r', '--remote', nargs=1, type=str, default=None)
    init_parser.add_argument('-d', '--description', nargs=1, type=str, default="no description", dest="desc")
    init_parser.add_argument('--venv-name', nargs=1, default='.venv')
    init_parser.add_argument('--no-git', action='store_false', default=True, dest="git")
    init_parser.add_argument('--no-tests', action='store_false', default=True, dest="tests")
    init_parser.add_argument('--no-docs', action='store_false', default=True, dest="docs")
    init_parser.add_argument('--no-venv', action='store_false', default=True, dest="venv")
    
    new_parser = subparsers.add_parser(name="new")
    new_parser.add_argument('package', type=str)
    new_parser.add_argument('-a', '--author', nargs=1, type=str, default=None)
    new_parser.add_argument('-e', '--email', nargs=1, type=str, default=None)
    new_parser.add_argument('-f', '--force', action='store_true', default=False)
    new_parser.add_argument('-v', '--verbose', action='store_true', default=False)
    new_parser.add_argument('-r', '--remote', nargs=1, type=str, default=None)
    new_parser.add_argument('-d', '--description', nargs=1, type=str, default="no description", dest="desc")
    new_parser.add_argument('--venv-name', nargs=1, default='.venv')
    new_parser.add_argument('--no-git', action='store_false', default=True, dest="git")
    new_parser.add_argument('--no-tests', action='store_false', default=True, dest="tests")
    new_parser.add_argument('--no-docs', action='store_false', default=True, dest="docs")
    new_parser.add_argument('--no-venv', action='store_false', default=True, dest="venv")
    
    return parser.parse_args()
    




