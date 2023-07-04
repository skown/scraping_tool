import json
import pandas as pd

with open("real_response_5.json") as json_file:
	real_response = json.load(json_file)

df_keyword = pd.DataFrame(columns=['Task Number', 'Keyword'])
for task_number in range(0, len(real_response)):
	for key, value in real_response[task_number]['tasks'][0]['result'][0].items():
		if key == 'keyword':
			df_keyword = df_keyword.append({'Task Number': task_number, 'Keyword': value}, ignore_index=True)

def Organic_Results(json_data):
	df_organic = pd.DataFrame(columns=['Type','Rank Group', 'Rank Absolute', 'Domain', 'Title', 'URL', 'Description', 'Task Number'])
	try:
		for task_number in range(0, len(json_data)):
			for organic_result in json_data[task_number]['tasks'][0]['result'][0]['items']:
				if organic_result['type'] == 'organic':
					df_organic = df_organic.append({
						'Type': organic_result['type'], 
						'Rank Group': organic_result['rank_group'], 
						'Rank Absolute': organic_result['rank_absolute'],
						'Domain': organic_result['domain'],
						'Title': organic_result['title'],
						'URL': organic_result['url'],
						'Description': organic_result['description'],
						'Task Number': task_number},ignore_index=True)
		organic_results = pd.merge(df_organic, df_keyword, on='Task Number')
		organic_results.to_csv('organic_result_4.csv')
	except TypeError as e:
		print(e)

def Featured_Snippets(json_data):
	df_featured_snippets = pd.DataFrame(columns=['Type', 'Rank Group', 'Rank Absolute', 'Domain', 'Title', 'Featured Title', 'URL', 'Description', 'Task Number'])
	try:
		for task_number in range(0, len(json_data)):
			for value in json_data[task_number]['tasks'][0]['result'][0]['items']:
				if value['type'] == 'featured_snippet':
					df_featured_snippets = df_featured_snippets.append({
						'Type': value['type'],
						'Rank Group': value['rank_group'], 
						'Rank Absolute': value['rank_absolute'],
						'Domain': value['domain'],
						'Title': value['title'],
						'Featured Title': value['featured_title'],
						'URL': value['url'],
						'Description': value['description'],
						'Task Number': task_number},ignore_index=True)
		fs_results = pd.merge(df_featured_snippets, df_keyword, on='Task Number')
		fs_results.to_csv('fs_results_5.csv')
	except TypeError as e:
		print(e)


def QA_results(json_data):
	df_qa = pd.DataFrame(columns=['Type', 'Rank Group', 'Rank Absolute', 'Type_QA', 'URL', 'Question_Text', 'Answer_Text', 'Source', 'Domain', 'Votes','Task Number'])
	try:
		for task_number in range(0, len(json_data)):
			for value in json_data[task_number]['tasks'][0]['result'][0]['items']:
				if value['type'] == 'questions_and_answers':
					for qa_value in value['items']:
						df_qa = df_qa.append({
							'Type': value['type'],
							'Rank Group': value['rank_group'],
							'Rank Absolute': value['rank_absolute'],
							'Type_QA': qa_value['type'],
							'URL': qa_value['url'],
							'Question_Text': qa_value['question_text'],
							'Answer_Text': qa_value['answer_text'],
							'Source': qa_value['source'],
							'Domain': qa_value['domain'],
							'Votes': qa_value['votes'],
							'Task Number': task_number}, ignore_index=True)
		qa_results = pd.merge(df_qa, df_keyword, on='Task Number')
		qa_results.to_csv('qa_results_5.csv')
	except TypeError as e:
		print(e)


#Organic_Results(real_response)
Featured_Snippets(real_response)
QA_results(real_response)
