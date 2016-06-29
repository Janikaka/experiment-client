import click
import requests
import random
import string

def randomString():
	upper_case = 1
	name_upper_chars = string.ascii_uppercase
	upper_name = ''.join(random.choice(name_upper_chars) for y in range(upper_case))
	name_size = 5
	name_chars = string.ascii_lowercase
	name = ''.join(random.choice(name_chars) for x in range(name_size))
	digits_size = 2
	digits_chars = string.digits
	digits = ''.join(random.choice(digits_chars) for z in range(digits_size))
	return upper_name + name + digits


def getConf(username, password, url):
	confURL = url + 'configurations'
	confHeaders = {'username':username, 'password':password}
	confPayload = {}
	r = requests.get(confURL, headers=confHeaders, json=confPayload)
	return r.json()['configurations']

def postEvent(username, url):
	eventsURL = url + 'events'
	eventsHearders = {'username':username}
	randValue = random.randint(0, 10)
	eventsPayload = {'value': randValue}
	requests.post(eventsURL, headers=eventsHearders, json=eventsPayload)

#click.echo("Conf: %s" %r.json()['configurations'])	

@click.command()
@click.option('--username')
@click.option('--password')
@click.option('--dataitems')
@click.option('--users')
@click.option('--url')
def login(username, password, dataitems, users, url):
	
	if username != None and password != None:
		conf = getConf(username, password, url)
		print("Configurations: %s" % conf)
		if dataitems != None:
			for i in range(int(dataitems)):
				postEvent(username, url)
	elif users != None:
		for i in range(int(users)):
			username = randomString()
			password = randomString()
			conf = getConf(username, password, url)
			print("Configurations: %s" % conf)
			if dataitems != None:
				for i in range(int(dataitems)):
					postEvent(username, url)
			else:
				for i in range(random.randint(10,30)):
					postEvent(username, url)


	

if __name__ == '__main__':
	login()

# $VENV/bin/python client.py --username=jaska --password=jokunen --dataitems=100 --url=http://localhost:6543/
# $VENV/bin/python client.py --users=20 --dataitems=10 --url=http://localhost:6543/

