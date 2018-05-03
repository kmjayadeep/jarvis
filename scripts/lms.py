import configparser
import subprocess
import sys

def process(input_args,parser):
	settings = configparser.ConfigParser()
	settings.read(sys.path[0]+'/configs/lms.ini')

	parser.add_argument('command',choices=['update','deploy','restart'])
	parser.add_argument('application',choices=['reporting','framework'])
	parser.add_argument('customer',choices=settings.sections())

	args = parser.parse_args(input_args)

	customer = args.customer
	command = args.command
	application = args.application
	host = settings.get(customer,'host')
	account = settings.get(customer,'account')
	user = settings.get(customer,'user')
	password = settings.get(customer,'password')
	source = settings.get(customer,application+'Source')
	application = settings.get(customer,application)

	if(password[0]=='$'):
		password = subprocess.check_output((password[2:-1]).split(' '))

	neoCommand = ''

	if(command=='restart'):
		neoCommand=['/home/I341935/Apps/neo/tools/neo.sh','restart','--application', application,'--account',account,'--host',host,'--user',user,'-y','-p',password]
	if(command=='deploy'):
		neoCommand=['/home/I341935/Apps/neo/tools/neo.sh','deploy','--application', application,'--account',account,'--host',host,'--user',user,'-p',password,'--source',source]

	subprocess.call(neoCommand)