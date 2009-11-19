#!/usr/bin/python

import os

PATH = os.path.abspath(os.path.dirname(__file__))

print """This will delete all data in the database
AND REPLACE IT WITH DEFAULT DATA!!!"
THE ONLY DATA LEFT WILL BE THAT SPECIFIED IN loaddata.py"
You lose anything else added later"
It should be noted that this isn't a joke"""
reply = raw_input("Are you seriously sure (type 'yes' to continue)? ")
if reply == 'yes':
	print "here"
	os.system("python manage.py reset recipes tagging --noinput")
	print "here2"
	ppath = MEDIA_ROOT = os.path.join(PATH, '..')
	print ppath
	print "here3"
	os.system("PYTHONPATH=\"%s\" DJANGO_SETTINGS_MODULE=digichef.settings python loaddata.py" % ppath)
	print "here4"

