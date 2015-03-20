# -*- coding: utf-8 -*-
"""
Run this file to download PhantomChess to the directory of this file.
"""
print "Preparing to install..."
import zipfile
import os
import shutil
import urllib
import sys
print "Downloading..."
url = 'https://github.com/671620616/PhantomChess/archive/master.zip'
urllib.urlretrieve(url, 'Phantom.zip')
print "Unzipping..."
with zipfile.ZipFile('Phantom.zip', 'r') as zipped:
    zipped.extractall()
print "Adding to importable location..."
for p in sys.path:
    if os.path.split(p)[1] == 'site-packages':
        copyto = os.path.join(p, 'Phantom')
        try:
            shutil.rmtree(copyto)
        except:
            pass
        shutil.copytree(os.path.join('PhantomChess-master', 'Phantom'), copyto)
print "Cleaing up..."
try:
    shutil.rmtree('Phantom')
except:
    pass
shutil.copytree(os.path.join('PhantomChess-master', 'Phantom'), 'Phantom')
shutil.rmtree('PhantomChess-master')
os.remove('Phantom.zip')
print "Done!"
