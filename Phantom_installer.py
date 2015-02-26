# -*- coding: utf-8 -*-
"""
Run this file to download PhantomChess to the directory of this file.
"""

import zipfile
import os
import urllib2

url = 'https://github.com/671620616/PhantomChess/archive/master.zip'

with urllib2.urlopen(url) as u:
    content = u.read()

zipped = zipfile.ZipFile(content)
zipped.extractall()

os.remove('Phantom_installer.py')
