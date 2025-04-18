from subprocess import run

def pip_install(venv_python: str, *packages: str, editable: bool = False):
        """
        Install packages with pip inside the virtual environment.
        
        Args:
            venv_python (str): Path to the virtual environment's python executable.
            *packages (str): Package(s) to install into the virtual environment.
        """
        if editable:
            run([venv_python, '-m', 'pip', 'install', '-e', *packages], check=True)
        else:
            run([venv_python, '-m', 'pip', 'install', *packages], check=True)