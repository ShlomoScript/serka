import os
import shutil
import subprocess
import venv
from ...utils.pip_utils import pip_install
from subprocess import run, call

class ProjectEnv:

    def __init__(self, root: str, force: bool, git: bool, venv_name: str | None, remote: str | None):
        self.force = force
        self.git = git
        self.venv_name = venv_name
        self.remote = remote
        self.root = root
        self.build_env()
        pip_install(self.venv_exec, 'git+https://github.com/ShlomoScript/serka.git')

    def build_env(self):
        """Build the project environment. Git repository and virtual environment."""
        if self.git:
            self.create_git_repo()
        if self.venv_name:
            self.create_venv()
        self.venv_exec, self.venv_bin = self.venv_paths()

    def create_venv(self):
        """Create the virtual environment."""
        if self.venv_name:
            if not os.path.exists(self.venv_name):
                venv.create(self.venv_name, with_pip=True)
            elif self.force:
                print(f"Virtual environment named '{self.venv_name}' already exists")
                print("Overwriting...")
                shutil.rmtree(self.venv_name)
                venv.create(self.venv_name, with_pip=True)
            else:
                print(f"Virtual environment named '{self.venv_name}' already exists.")
    
    def venv_paths(self) -> tuple[str, str]:
        """
        Get the path of the virtual environment's bin directory and python executable.
        
        Returns:
            tuple[str, str]: Tuple of the virtual environment's python executable and bin directory.
        """
        if os.name == 'nt':
            venv_exec = os.path.join(self.root, self.venv_name, 'Scripts', 'python.exe')
            bin_dir = os.path.join(self.root, self.venv_name, 'Scripts')
        else:
            venv_exec = os.path.join(self.root, self.venv_name, "bin", "python")
            bin_dir = os.path.join(self.root, self.venv_name, "bin")
        return venv_exec, bin_dir

    def is_git_repo_root() -> bool:
        """
        Check if the current directory is the root of a git repository.

        Returns:
            bool: Whether it is or isn't the root of a git repository.
        """
        return os.path.exists('.git')

    def create_git_repo(self):
        """Create a git repository in the current directory."""
        if self.is_git_repo_root() is True:
            print("Existing git Repository already initialized in current directory")
            return
        if self.in_git_repo():
            print("Initializing git repository inside existing git repository")
            print(f"If this is meant to be a submodule, please run 'git submodule add {self.root}' in the super repository after your first commit")
        run(['git', 'init'])
        run(['git', 'branch', '-M', 'main'])
        if self.remote:
            run(['git', 'remote', 'add', 'origin', self.remote])
            run(['git', 'branch', '-u', 'origin/main', 'main'])
        

    def in_git_repo(self) -> bool:
        """
        Check if the current directory is in a git repository.
 
        Returns:
            bool: Whether it is or isn't in a git repository.
        """
        return call(['git', '-C', self.root, 'status'], stderr=subprocess.STDOUT, stdout=open(os.devnull, 'w')) == 0