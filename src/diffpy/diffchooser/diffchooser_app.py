import argparse

from diffpy.diffchooser.version import __version__  # noqa


def main():
    parser = argparse.ArgumentParser(
        prog="diffpy.diffchooser",
        description=(
            "Screen protein diffraction images for well diffracting samples\n\n"
            "For more information, visit: "
            "https://github.com/diffpy/diffpy.diffchooser/"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="Show the program's version number and exit",
    )

    args = parser.parse_args()

    if args.version:
        print(f"diffpy.diffchooser {__version__}")
    else:
        # Default behavior when no arguments are given
        parser.print_help()


if __name__ == "__main__":
    main()
