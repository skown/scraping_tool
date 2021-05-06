from .client import RestClient
client = RestClient("adrian.skowron@brainly.com", "6a82d00b8f673110")

def Get_serp():
	response = client.get("/v3/serp/google/organic/tasks_ready")
	if response['status_code'] == 20000:
		results = []
		for task in response['tasks']:
			if (task['result'] and (len(task['result']) > 0)):
				for resultTaskInfo in task['result']:
					if(resultTaskInfo['endpoint_advanced']):
						results.append(client.get(resultTaskInfo['endpoint_advanced']))                
		return results
	else:
		print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))