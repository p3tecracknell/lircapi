#!/usr/bin/python

import os,sys
from bottle import route, run
from configobj import ConfigObj
from validate import Validator

# Constants
CONFIG_PATH = 'config.ini'
CONFIG_SPEC = 'configspec.ini'

def main(args):
	config = ConfigObj(CONFIG_PATH, configspec = CONFIG_SPEC)
	validator = Validator()
	result = config.validate(validator, copy = True)
	
	run(host = config['host'],
		port = config['port'],
		debug = config['debug'],
		reloader = config['debug'],
		server = 'cherrypy')

@route('/')
def index():
	return "<a href=\"onkyo/KEY_POWER\">Onkyo Power</a>"
	
@route('/<remote>/<function>')
def irsend(remote, function):
	os.system("irsend SEND_ONCE " + remote + " " + function)
	return "ok"

if __name__ == '__main__':
    main(sys.argv[1:])