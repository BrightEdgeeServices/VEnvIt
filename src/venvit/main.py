import argparse
import sys

from venvit.upgrade import upgrade


class ParseArgs:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog="venvit",
            description="Tools for creating, maintaining and automating Python virtual environments.",
        )
        # self.upgrade = None
        self.parser_upgrade = None
        self.subparsers = self.parser.add_subparsers(title="Commands")

    def upgrade(self):
        self.parser_upgrade = self.subparsers.add_parser(
            "upgrade",
            help="Execute upgrade procedure.",
        )
        self.parser_upgrade.add_argument(
            "upgrade_id",
            # help="Upgrade process id.",
            # action="store_true",
            # default=False,
            # choices=upgrade.UpgradeIds().model_dump().keys(),
            help="",
        )
        self.parser_upgrade.set_defaults(func=upgrade.Upgrade)
        pass


def main():
    pa = ParseArgs()
    pa.upgrade()
    if len(sys.argv) > 1:
        args = pa.parser.parse_args()
        args.func(args)
    else:
        pa.parser.print_help()
        sys.exit(2)
    pass


if __name__ == "__main__":
    main()
