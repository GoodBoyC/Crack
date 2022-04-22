import os, sys, platform
os.system('git pull')
try:

    import requests

except:

    os.system('pip install requests')

from main import chinda

chinda()
