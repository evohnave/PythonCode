'''
This context manager will capture stdout and stderr.

Example usage:

...
    with self.assertRaises(SystemExit) as cm:
        with capture_sys_output():
            arg_parse_obj.parse_known_args(['-h'])

    self.assertEqual(cm.exception.code, 0)
    self.assertEqual(stderr.getvalue(), '')
    self.assertEqual(stdout.getvalue(), 'Help text from argparse')
'''

import sys
from contextlib import contextmanager
from io import StringIO

@contextmanager
def capture_sys_output():
    ''' capture sys output to clean up test output '''
    capture_out, capture_err = StringIO(), StringIO()
    current_out, current_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = capture_out, capture_err
        yield capture_out, capture_err
    finally:
        sys.stdout, sys.stderr = current_out, current_err
