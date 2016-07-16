#!/usr/bin/env python3

import click
import requests
import random
import getpass

#http://click.pocoo.org/5/parameters/#implementing-custom-types 


@click.command()
@click.argument('url', required=1)
@click.option('--username', default=getpass.getuser(), type=click.STRING)
@click.option('--dataitem', multiple=True)
@click.option('--dataitems', multiple=True, type=click.STRING)
@click.option('--random_dataitems', type=click.INT)
@click.option('--random_min', type=click.INT)
@click.option('--random_max', type=click.INT)
@click.option('--key', type=click.STRING)
@click.option('--verbose', is_flag=True)
def cli(url, username, dataitem, dataitems, random_dataitems, random_min, random_max, key, verbose):
	if dataitem or dataitems or random_dataitems or random_min or random_max or key:
		default = False
	else:
		default = True
	if random_min is None:
		random_min = 0
	elif random_dataitems is None:
		click.echo('ERROR: invalid random_dataitems')
	if random_max is None:
		random_max = 100
	elif random_dataitems is None:
		click.echo('ERROR: invalid random_dataitems')
	conf = getConf(username, url)
	if verbose or default:
		click.echo('Configurations: %s' % conf)
	if dataitem is not None:
		for item in dataitem:
			arr = item.split(":")
			key = str(arr[0])
			value = int(arr[1])
			postEvent(username, key, value, url, verbose)
	if dataitems is not None:
		for filename in dataitems:
			if type(filename) is not str:
				click.echo("ERROR: invalid filename")
				return 1
			dataitemsFromFile = readFile(filename)
			for dataitem in dataitemsFromFile:
				postEvent(username, dataitem['key'], dataitem['value'], url, verbose)
	if random_dataitems is not None:
		if key is None:
			click.echo("ERROR: invalid key")
			return 1
		for i in range(random_dataitems):
			postEvent(username, key, random.randint(random_min, random_max), url, verbose)
	return 0


def getConf(username, url):
	confURL = url + 'configurations'
	confHeaders = {'username':username}
	confPayload = {}
	r = requests.get(confURL, headers=confHeaders, json=confPayload)
	if r.status_code != 200:
		click.echo('ERROR: status %d' % r.status_code)
		return 1
	return r.json()['data']

def postEvent(username, key, value, url, verbose):
	eventsURL = url + 'events'
	eventsHearders = {'username':username}
	eventsPayload = {'value': value, 'key':key}
	r = requests.post(eventsURL, headers=eventsHearders, json=eventsPayload)
	if r.status_code != 200:
		click.echo('ERROR: status %d' % r.status_code)
		return 1
	elif verbose:
		click.echo('Dataitem (%s:%d) sent' % (key, value))

def readFile(filename):
	dataitems = []
	f = open(filename, 'r')
	for line in f:
		arr = line.split(":")
		key = arr[0]
		value = int(arr[1])
		if type(key) is not str:
			click.echo("ERROR: invalid file")
			return 1
		dataitems.append({'key':key, 'value':value})
	return dataitems

if __name__ == '__main__':
	cli()





