# -*- coding: utf-8 -*-
"""
Run this file to download PhantomChess to the directory of this file.
"""
print "Preparing to install..."
import zipfile
import os
import shutil
import urllib
print "Downloading..."
url = 'https://github.com/671620616/PhantomChess/archive/master.zip'
urllib.urlretrieve(url, 'Phantom.zip')
print "Unzipping..."
zipped = zipfile.ZipFile('Phantom.zip', 'r')
zipped.extractall()
zipped.close()
print "Cleaing up..."
shutil.copytree(os.path.join('PhantomChess-master', 'Phantom'), 'Phantom')
shutil.rmtree('PhantomChess-master')
os.remove('Phantom.zip')
print "Done!"
