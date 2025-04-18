import os
from argparse import Namespace
from .init import init

def new(args: Namespace):
    if not os.path.exists(args.package):
        print(f"Creating {args.package}")
        os.mkdir(args.package)
        os.chdir(args.package)
        init(args)
        os.chdir("..")
    elif args.force:
        print(f"{args.package} directory already exists")
        print("Overwriting...")
        os.rmdir(args.package)
        os.mkdir(args.package)
        os.chdir(args.package)
        init(args)
        os.chdir("..")

    else:
        print(f"{args.package} directory already exists")