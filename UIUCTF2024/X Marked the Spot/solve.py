from itertools import cycle

tmpC = b'\x1D\x0D\x1C\x12\x16\x00\x11\x0C'
tmpFlag = b"uiuctf{}"
c = b'\x1D\x0D\x1C\x12\x16\x00\x11\x1F\x58\x10\x36\x1B\x17\x53\x1E\x2E\x1C\x0C\x5A\x2E\x11\x12\x5E\x03\x1C\x3B\x0B\x04\x16\x39\x5E\x1D\x5D\x54\x36\x05\x0A\x55\x35\x42\x06\x00\x48\x50\x43\x47\x4B\x0C'

key = bytes(x ^ y for x, y in zip(tmpC, tmpFlag))

flag = bytes(x ^ y for x, y in zip(c, cycle(key)))
print(flag)