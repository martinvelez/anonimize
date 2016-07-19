import sys
from anonimize import anonimize

def fatal_syntax_error_message(message):
    print(message)
    sys.exit('Use the following syntax: python3 driver.py [-i] target_dir')

if __name__ == "__main__":
        modify_in_place = False
        target_dir = ''
        if len(sys.argv) == 3:
                if sys.argv[1] == '-i':
                        modify_in_place = True
                        target_dir = sys.argv[2]
                else:
                        fatal_syntax_error_message("fatal: unrecognized argument: {0}".format(sys.argv[1]))
        elif len(sys.argv) == 2:
                target_dir = sys.argv[1]
        else:
                fatal_syntax_error_message('fatal: missing target directory')
        anonimize(target_dir, modify_in_place)