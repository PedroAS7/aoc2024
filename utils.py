from os import getcwd
from sys import stderr
from os.path import (join,
                     dirname,
                     realpath)

def read_input(py_file: str, chall_number: int) -> str:
    file_path = dirname(realpath(py_file))
    input_text = None

    try:
        with open(join(file_path, f"input_{chall_number}.txt"), "rt") as input_file:
            input_text = input_file.read()
        # end with

        if not input_text:
            raise IOError()
        # end if
        
    except IOError:
        print("Failed to extract input", file=stderr)
    # end try

    return input_text
# end def
