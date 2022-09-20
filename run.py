import os, platform
bit = platform.architecture()[0]
if bit == '64bit':
    from fb import Selamat
    Selamat()
elif bit == '32bit':
    from fb import Selamat
    Selamat()
