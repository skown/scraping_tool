from .client import RestClient
import pandas as pd
import time
from csv import reader

client = RestClient("mail", "pass")
market = 'US'
location_csv = pd.read_csv('locations_serp_2021_03_10.csv')
locations = location_csv[(location_csv['country_iso_code'] == market) & (location_csv['location_type'] == 'Country')]
location_code = locations['location_code']

def Post_mobile_data(keywords):
	post_data = dict()
	for data in keywords:
		post_data[len(post_data)] = dict(
			language_code='en',
			location_code=2840,
			device='mobile',
			keyword=data)
		time.sleep(0.75)
		response = client.post("/v3/serp/google/organic/task_post", post_data)
		print(response)
		post_data.clear()

def Post_mobile_data2(keywords):
	post_data = dict()
	post_data[len(post_data)] = dict(
		language_code='en',
		location_code=location_code,
		device=device,
		keyword=keywords)
	time.sleep(0.75)
	response = client.post("/v3/serp/google/organic/task_post", post_data)
	print(response)
	post_data.clear()

def Post_desktop_data(keywords):
	post_data = dict()
	for data in keywords:
		post_data[len(post_data)] = dict(
			language_code='en',
			location_code=2840,
			device='desktop',
			keyword=data)
		time.sleep(0.75)
		response = client.post("/v3/serp/google/organic/task_post", post_data)
		print(response)
		post_data.clear()

