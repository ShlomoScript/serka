import os
from argparse import Namespace
from .new_project.gen.gen_env import ProjectEnv
from .new_project.gen.gen_structure import ProjectStructure
from .new_project.gen.write_files import ProjectFiles

class Project(ProjectEnv, ProjectStructure, ProjectFiles):
    def __init__(
            self,
            args: Namespace,
            root: str = os.getcwd(),
        ):
        self.ver = 0.1
        self.root = root
        self.force: bool = args.force
        self.author: str = args.author
        self.name = os.path.basename(root)
        ProjectEnv.__init__(
            root,
            self.force,
            args.git,
            args.venv_name if args.venv else None,
            args.remote
        )
        ProjectStructure.__init__(
            args.docs,
            args.tests,
            args.author,
            self.name,
            self.ver,
            self.force,
            self.venv_exec
        )
        ProjectFiles.__init__(
            self.root,
            self.tests,
            self.name,
            self.ver,
            self.author,
            args.email,
            args.desc,
            self.force
        )

        


