import argparse
import sys


class ArgumentParser:
    def __init__(self, argumet_struct):
        self._parser = argparse.ArgumentParser(description='My task3 parser')
        for arg_name, arg_rules in arg_struct.items():
            help_message = 'Set {} param{}'.format(
                arg_name, ', required' if arg_rules['required'] else '')
            self._parser.add_argument(
                arg_name, help=help_message, required=arg_rules['required'],
                type=arg_rules['type'])

    def parse(self, arg_list):
        return self._parser.parse_args(arg_list)


arg_struct = {
    '--int': {
        'type': int,
        'required': True},
    '--str': {
        'type': str,
        'required': True},
    '--bool': {
        'type': lambda x: False if x in ['0', 'F', 'f', 'False'] else True,
        'required': False},
    '--float': {
        'type': int,
        'required': False}}


if __name__ == '__main__':
    parser = ArgumentParser(arg_struct)
    if len(sys.argv) > 1:
        args = parser.parse(sys.argv[1:])
        print(args)
