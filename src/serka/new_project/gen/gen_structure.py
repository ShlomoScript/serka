import os
import shutil
from subprocess import run
from ...utils.pip_utils import pip_install

class ProjectStructure:

    def __init__(
            self,
            docs: bool,
            tests: bool,
            author: str,
            name: str,
            ver: float,
            force: bool,
            python_exec: str
        ):
        self.docs = docs
        self.tests = tests
        self.author = author
        self.name = name
        self.ver = ver
        self.force = force
        self.python_exec = python_exec
        self.build_structure()
    
    def build_structure(self):
        """Creates the structure of the project."""
        if self.docs:
            self.create_docs()
            self.docs = 'docs'
        if self.tests:
            self.create_tests()
            self.tests = 'tests'
        self.create_src()

    def create_src(self):
        """Creates the src directory of the project"""
        if not os.path.exists('src'):
            print(f"Creating src and src/{self.name} directories")
            os.mkdir('src')
            os.mkdir(os.path.join('src', self.name))
        elif not os.path.exists(os.path.join('src', self.name)):
            print(f"Creating src/{self.name} directory")
            os.mkdir(os.path.join('src', self.name))
        elif self.force:
            print(f"src/{self.name} directory already exists")
            print("Overwriting...")
            os.mkdir(os.path.join('src', self.name))
        else:
            print(f"src/{self.name} directory already exists")
            print("Continuing")


    def create_docs(self):
        """Generate the docs directory using sphinx."""
        if not os.path.exists('docs'):
            print("Making docs directory")
            pip_install(self.python_exec, 'sphinx')
            run(['sphinx-quickstart', 'docs', '--quiet', '--no-sep', '-p', self.name, '-a', self.author, '-r', f'{self.ver}', '-l', 'en', '--makefile', '--batchfile', '-m', '--ext-autodoc'])
        elif self.force:
            print("Docs directory already exists")
            print("Overwriting...")
            pip_install(self.python_exec, 'sphinx')
            run(['sphinx-quickstart', 'docs', '--quiet', '--no-sep', '-p', self.name, '-a', self.author, '-r', f'{self.ver}', '-l', 'en', '--makefile', '--batchfile', '-m', '--ext-autodoc'])
        else:
            print("Docs direcotry already exists")
            print("Continuing")
        

    def create_tests(self):
        """Creates the tests directory."""
        if not os.path.exists('tests'):
            print("Making tests directory")
            os.mkdir('tests')
            os.mkdir(os.path.join('tests', f'test_{self.name}'))
        elif self.force:
            print("Tests directory already exists")
            print("Overwriting...")
            shutil.rmtree('tests')
            os.mkdir('tests')
            os.mkdir(os.path.join('tests', f'test_{self.name}'))
        else:
            print("Tests directory already exists")
            print("Continuing")

