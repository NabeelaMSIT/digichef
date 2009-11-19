#!/usr/bin/python

import os

PATH = os.path.abspath(os.path.dirname(__file__))

# Make sure the user understands what's up
print """This will delete all data in the database
AND REPLACE IT WITH DEFAULT DATA!!!"
THE ONLY DATA LEFT WILL BE THAT SPECIFIED IN loaddata.py"
You lose anything else added later"
It should be noted that this isn't a joke"""
reply = raw_input("Are you seriously sure (type 'yes' to continue)? ")
#if they are sure
if reply == 'yes':
	os.system("python manage.py reset recipes tagging --noinput")# wipe DB
	ppath = os.path.join(PATH, '..')
	os.system("PYTHONPATH=\"%s\" DJANGO_SETTINGS_MODULE=digichef.settings python loaddata.py" % ppath)# fill with default data

