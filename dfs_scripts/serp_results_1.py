from .client import RestClient
import pandas as pd
import time
from csv import reader

client = RestClient("adrian.skowron@brainly.com", "6a82d00b8f673110")
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
'''
if response["status_code"] == 20000:
	for task_number in range(len(response['tasks'])):
		for tasks, task_value in response['tasks'][task_number].items():
			if tasks == 'id':
				for keyword, keyword_value in response['tasks'][task_number]['data'].items():
					if keyword == 'keyword':
						print(task_number)
						print(task_value, '->', keyword_value)
else:
	print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
'''

'''
response = client.post("/v3/serp/google/organic/task_post", post_data)
if response["status_code"] == 20000:
    print(response)
    # do something with result
else:
    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
'''

'''
update = dict()
keywords = ['brainly', 'brainly app', 'brainly page']
for u in keywords:
	update = dict(keyword=u)
	print(update)
'''