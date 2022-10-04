from .arg_parser import create_argparser


def run_cli(version=None):
    arg_parser = create_argparser(version=version)
    args = arg_parser.parse_args()
    print(f'Got args: {args}')


if __name__ == '__main__':
    run_cli()
