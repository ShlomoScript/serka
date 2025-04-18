import os
import tomli_w


class ProjectFiles:

    def __init__(
            self,
            root: str,
            tests: bool | str,
            name: str,
            ver: float,
            author: str,
            email: str,
            desc: str,
            force: bool
        ):
        self.root = root
        self.tests = tests
        self.name = name
        self.ver = ver
        self.author = author
        self.email = email
        self.desc = desc
        self.force = force
        self.write_files()
    
    def write_files(self):
        """Write the files of the project."""
        self.write_gitignore()
        self.write_pyproject()
        self.write_readme()
        self.write_src_files()
        self.write_test_files()

    def write_readme(self):
        """Create the README."""
        if not os.path.exists('README.md'):
            print("Creating README.md")
            with open('README.md', 'x', ) as f:
                f.write(f"# {self.name}\n")
        elif self.force:
            print("README.md already exists")
            print("Overwriting...")
            with open('README.md', 'w') as f:
                f.write(f"# {self.name}")
        else:
            print("README.md already exists")
            print("Continuing")

    def write_pyproject(self):
        """Create the pyproject.toml."""
        pyproject = {
            'build-system': {
                'requires': ["setuptools"],
                'build-backend': "setuptools.build_meta"
            },
            'project': {
                'name': self.name,
                'version': self.ver,
                'authors': [{'name': self.author, 'email': self.email}],
                'description': self.desc,
                'readme': "README.md",
                'dependencies': []
            },
            'project.scripts': {
                self.name: f"{self.name}.main:main"
            },
            'tool.setuptools': {
                'package-dir': { "": "src"}
            },
            'tool.setuptools.packages.find': {
                'where': ["src"]
            }
        }
        if not os.path.exists('pyproject.toml'):
            print("Creating pyproject.toml")
            with open('pyproject.toml', 'x') as f:
                tomli_w.dump(pyproject, f)
        elif self.force:
            print("pyroject.toml already exists")
            print("Overwriting...")
            with open('pyproject.toml', 'w'):
                tomli_w.dump(pyproject, f)
        else:
            print("pyproject.toml already exists")
            print("Continuing")

    def write_gitignore(self):
        """Create the .gitignore"""
        ignore = """
                __pycache__/
                *.py[cod]
                *$py.class
                *.so
                .Python
                build/
                develop-eggs/
                dist/
                downloads/
                eggs/
                .eggs/
                lib/
                lib64/
                parts/
                sdist/
                var/
                wheels/
                share/python-wheels/
                *.egg-info/
                .installed.cfg
                *.egg
                MANIFEST
                pip-log.txt
                pip-delete-this-directory.txt
                *.manifest
                *.spec
                .pytest_cache/
                docs/_build/
                .env
                .venv
                env/
                venv/
                ENV/
                env.bak/
                venv.bak/
                .pypirc
                """
        if not os.path.exists('.gitignore'):
            print("Creating .gitignore.")
            with open('.gitignore', 'x') as f:
                f.write(ignore)
        elif self.force:
            print(".gitignore already exists")
            print("Overwriting")
            with open('.gitignore', 'w') as f:
                f.write(ignore)
        else:
            print(".gitignore already exists")
            print("Continuing")

    def write_src_files(self):
        """Create the source files."""
        main = os.path.join('src', self.name, 'main.py')
        if not os.path.exists(main):
            print("Creating main.py")
            self.write_main(main)
        elif self.force:
            print("Existing main.py found")
            print("Overwriting...")
            self.write_main(main)
        else:
            print("Existing main.py found")
            print("Continuing")
        init = os.path.join('src', self.name, '__init__.py')
        if not os.path.exists(init):
            print("Creating, __init__.py")
            with open(init, 'w') as f:
                f.write(f"__version__ = {self.ver}")
        elif self.force:
            print("__init__.py already exists")
            print("Overwriting...")
            with open(init, 'w') as f:
                f.write(f"__version__ = {self.ver}")
        else:
            print("__init__.py already exists")
            print("Continuing")


    def write_test_files(self):
        """Create the test files."""
        test = os.path.join('tests', f'test_{self.name}', 'test_main.py')
        conf = os.path.join('tests', f'test_{self.name}', 'conftest.py')
        if not os.path.exists(test):
            print("Creating test_main.py")
            self.write_test(test)
        elif self.force:
            print("test_main.py already exists")
            print("Overwriting...")
            self.write_test(test)
        else:
            print("test_main.py already exists")
            print("Continuing")
        if not os.path.exists(conf):
            print("Creating pytest configuration file")
            with open(conf, 'x') as f:
                f.writelines(
                    [
                        "import sys",
                        "import os",
                        "sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), \".../src\")))"
                    ]
                )
        elif self.force:
            print("Pytest configuration file already exists")
            print("Overwriting...")
            with open(conf, 'x') as f:
                f.writelines(
                    [
                        "import sys",
                        "import os",
                        "sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), \".../src\")))"
                    ]
                )
        else:
            print("Pytest configuration file already exists")
            print("Continuing")


    def write_test(self, path: str):
        """Create the main test file."""
        with open(path, 'w') as f:
            lines = [
                "# test_main.py - test file to test functions in main.py\n",
                "import pytest\n",
                f"from {self.name}.main import main\n",
                "\n",
                "def test_main(capfd):\n",
                "    main()\n",
                "captured = capfd.readouterr()\n",
                "assert captured.out == \"Hello, World\"\n"
            ]
            f.writelines(lines)
    
    @staticmethod
    def write_main(path):
        """Create the main file"""
        with open(path, 'w') as f:
            lines = [
                "# main.py — entry point of your program\n",
                "\n",
                "def main():\n",
                "    print(\"Hello, World\")\n",
                "\n",
                "if __name__ == \"__main__\":\n",
                "    main()\n"
            ]
            f.writelines(lines)