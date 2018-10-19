import os
import minitest

p = os.popen("python test.py 2")
p.read().p()
p.close()

from robot.utils import (PY2, console_decode)
import os
import mock

class MyProcess:

    def __init__(self, command):
        self._command = self._process_command(command)
        self._process = os.popen(self._command)

    def __str__(self):
        return self._command

    def read(self):
        return self._process_output(self._process.read())

    def close(self):
        try:
            rc = self._process.close()
        except IOError:  # Has occurred sometimes in Windows
            return 255
        if rc is None:
            return 0
        # In Windows (Python and Jython) return code is value returned by
        # command (can be almost anything)
        # In other OS:
        #   In Jython return code can be between '-255' - '255'
        #   In Python return code must be converted with 'rc >> 8' and it is
        #   between 0-255 after conversion
        if os.sep == '\\' or sys.platform.startswith('java'):
            return rc % 256
        return rc >> 8

    def _process_command(self, command):
        if '>' not in command:
            if command.endswith('&'):
                command = command[:-1] + ' 2>&1 &'
            else:
                command += ' 2>&1'
        return self._encode_to_file_system(command)

    def _encode_to_file_system(self, string):
        enc = sys.getfilesystemencoding() if PY2 else None
        return string.encode(enc) if enc else string

    def _process_output(self, output):
        if '\r\n' in output:
            output = output.replace('\r\n', '\n')
        if output.endswith('\n'):
            output = output[:-1]
        return console_decode(output, force=True)

robot.libraries.OperatingSystem._Process = MyProcess     


from robot.libraries.OperatingSystem import OperatingSystem as oos
aa = oos()
aa.run("ls -l")   

import subprocess
subprocess.call(["ls", "-l"])
