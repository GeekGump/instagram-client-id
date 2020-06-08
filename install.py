'''
github.com/razyar

for using InstagramClientId you need to install some modules
'''

import os
import sys
from os import system


def install(module):
	try:
		system('python -m pip install %s' % str(module))
		print '%s installed sucessfully' % str(module)
	except Exception as installingError:
		print 'Cannot install this moudle. check your pip version. error:\n %s \n solve this: https://github.com/razyar' % str(installingError)


install('python-instagram')
install('httplib2')
install('simplejson')
install('six')

