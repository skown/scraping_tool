from .client import RestClient
client = RestClient("adrian.skowron@brainly.com", "6a82d00b8f673110")

def Check_results():
	response = client.get("/v3/serp/google/organic/tasks_ready")
	if response["status_code"] == 20000:
		for key, key_value in response['tasks'][0].items():
			if key == 'result_count':
				return key_value
			'''
			for task_number in range(len(response['tasks'][0]['result'])):
				for result_key, result_value in response['tasks'][0]['result'][task_number].items():
					if result_key == 'id':
						#print(result_value)
						print(task_number)
'''
	else:
	    print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
