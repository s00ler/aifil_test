import argparse
import sys


class ArgumentParser:
    """Class to handle arguments parse.

    Initialize with a argument dictionary, example below.
    Use parse method to parse arg list.
    """

    def __init__(self, argumet_struct: dict):
        """Init parser with argument_struct."""
        self._parser = argparse.ArgumentParser(description='My task3 parser')
        for arg_name, arg_rules in argumet_struct.items():
            help_message = 'Set {} param{}'.format(
                arg_name, ', required' if arg_rules['required'] else '')
            if arg_rules['type'] == bool:
                self._parser.add_argument(
                    arg_name, help=help_message,
                    required=arg_rules['required'],
                    default=False, action='store_true')
            else:
                self._parser.add_argument(
                    arg_name, help=help_message,
                    required=arg_rules['required'],
                    default=None, type=arg_rules['type'])

    def parse(self, arg_list: list):
        """Parse an argument list, sys.argv[1:] for example."""
        return self._parser.parse_args(arg_list)


if __name__ == '__main__':

    arg_struct = {
        '--int': {
            'type': int,
            'required': True},
        '--str': {
            'type': str,
            'required': True},
        '--bool': {
            'type': bool,
            'required': False},
        '--float': {
            'type': float,
            'required': False}}

    parser = ArgumentParser(arg_struct)
    if len(sys.argv) > 1:
        args = parser.parse(sys.argv[1:])
        print(args)
