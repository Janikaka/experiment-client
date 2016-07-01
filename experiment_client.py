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
@click.option('--random_min', default=0, type=click.INT)
@click.option('--random-max', default=100, type=click.INT)
@click.option('--key', type=click.STRING)
def cli(url, username, dataitem, dataitems, random_dataitems, random_min, random-max, key):
	getConf(username, url)
	if dataitem is not None:
		for item in dataitem:
			arr = item.split(":")
			key = str(arr[0])
			value = int(arr[1])
			if type(key) is not str or type(value) is not int:
				click.echo("ERRORkey")
				click.echo(type(key))
				click.echo(value)
				return 1
			postEvent(username, key, value, url)
	if dataitems is not None:
		for filename in dataitems:
			dataitemsFromFile = readFile(filename)
			for dataitem in dataitemsFromFile:
				postEvent(username, dataitem['key'], dataitem['value'], url)
	if random_dataitems is not None:
		if key is None:
			click.echo("ERRORdataitem")
			return 2
		for i in range(random_dataitems):
			postEvent(username, key, random.randint(random_min, random-max), url)
	return 0


def getConf(username, url):
	confURL = url + 'configurations'
	confHeaders = {'username':username}
	confPayload = {}
	r = requests.get(confURL, headers=confHeaders, json=confPayload)
	click.echo(r.json()['configurations'])

def postEvent(username, key, value, url):
	eventsURL = url + 'events'
	eventsHearders = {'username':username}
	eventsPayload = {'value': value, 'key':key}
	requests.post(eventsURL, headers=eventsHearders, json=eventsPayload)

def readFile(filename):
	dataitems = []
	f = open(filename, 'r')
	for line in f:
		arr = line.split(":")
		key = arr[0]
		value = int(arr[1])
		if type(key) is not str or type(value) is not int:
			click.echo("ERRORfile")
			return 3
		dataitems.append({'key':key, 'value':value})
	return dataitems

if __name__ == '__main__':
	cli()





