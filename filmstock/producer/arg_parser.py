import argparse


def create_argparser(version=None):
    if not version:
        version = 'MISSING'
    parser = argparse.ArgumentParser(
        description='Helper tool for creating new flask projects, my way')
    parser.add_argument('--path', '-p',
                        type=str,
                        help='Path to project')
    parser.add_argument('--debug', '-d',
                        action='store_true',
                        help='Turn on the debug flag '
                             '(will ensure we do not '
                             'actually do anything only logs')
    parser.add_argument('--version',
                        action='version',
                        version=version)
    return parser
