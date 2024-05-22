from argparse import ArgumentParser

from .cap_gen import generate_captcha, random_text


def setup_argparse():
    """
    Generate text-to-image captcha.

    Args:
        -l, --length: The length of the captcha text to generate (int, optional): Defaults to 6.

    Returns:
        Namespace: An object containing the parsed arguments.
    """

    parser = ArgumentParser(description="Generate text-to-image captcha.")
    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=6,
        help="The length of the captcha text to generate.",
    )
    return parser.parse_args()


def main():
    """
    Runs the main functionality of the CAPTCHA generation CLI.

    Args:
        None

    Returns:
        None
    """

    args = setup_argparse()
    captcha_text = random_text(args.length)
    generate_captcha(captcha_text)
