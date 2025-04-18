import os
from argparse import Namespace
from ..project import Project


def init(args: Namespace):
    Project(args)


