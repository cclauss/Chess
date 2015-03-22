#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Run this file to download PhantomChess to the current working directory and install it in site-packages.
"""
print('=' * 31)

import os
import shutil
import sys
import urllib
import zipfile

module_name = 'Phantom'
print('Preparing to install {}...'.format(module_name))
master_name = module_name + 'Chess-master'
zip_filename = module_name + '.zip'
url = 'https://github.com/671620616/PhantomChess/archive/master.zip'

print('Downloading {}...'.format(zip_filename))
urllib.urlretrieve(url, zip_filename)
print('Unzipping {}...'.format(zip_filename))
with zipfile.ZipFile(zip_filename, 'r') as zipped:
    zipped.extractall()
print('Adding {} to importable location...'.format(module_name))
for p in sys.path:
    if os.path.split(p)[1] == 'site-packages':
        copyto = os.path.join(p, module_name)
        try:
            shutil.rmtree(copyto)
        except:
            pass
        try:
            shutil.copytree(os.path.join(master_name, module_name), copyto)
            print('Successfully copied {} to: {}'.format(module_name, copyto))
# a homebrew installed Python on Mac OS X has a read-only /Library/Python/2.7/site-packages
        except OSError as e:
            print('Failed to copy {} to: {} ({})'.format(module_name, copyto, e))
print('Cleanng up...')
try:
    shutil.rmtree(module_name)
except:
    pass
shutil.copytree(os.path.join(master_name, module_name), module_name)
shutil.rmtree(master_name)
os.remove(zip_filename)
print('Done! {}'.format('=' * 25))
