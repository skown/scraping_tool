import pandas as pd

def Data_json_process(json_data):
	df_keyword = pd.DataFrame(columns=['Task Number', 'Keyword'])
	df_data = pd.DataFrame(columns=['Type','Rank Group', 'Rank Absolute', 'Domain', 'Title', 'URL', 'Description', 'Task Number'])	
	df_featured_snippets = pd.DataFrame(columns=['Type', 'Rank Group', 'Rank Absolute', 'Domain', 'Title', 'Featured Title', 'URL', 'Description', 'Task Number'])
	df_qa = pd.DataFrame(columns=['Type', 'Rank Group', 'Rank Absolute', 'Type_QA', 'URL', 'Question_Text', 'Answer_Text', 'Source', 'Domain', 'Votes','Task Number'])

	for task_number in range(0, len(json_data)):
		for key, value in json_data[task_number]['tasks'][0]['result'][0].items():
			if key == 'keyword':
				df_keyword = df_keyword.append({'Task Number': task_number, 'Keyword': value}, ignore_index=True)

	for task_number in range(0, len(json_data)):
		for serp_results in json_data[task_number]['tasks'][0]['result'][0]['items']:
			if serp_results['type'] == 'organic':
				df_data = df_data.append({
					'Type': serp_results['type'],
					'Rank Group': serp_results['rank_group'],
					'Rank Absolute': serp_results['rank_absolute'],
					'Domain': serp_results['domain'],
					'Title': serp_results['title'],
					'URL': serp_results['url'],
					'Description': serp_results['description'],
					'Task Number': task_number},ignore_index=True)

	for task_number in range(0, len(json_data)):
		for fs_value in json_data[task_number]['tasks'][0]['result'][0]['items']:
			if fs_value['type'] == 'featured_snippet':
				df_featured_snippets = df_featured_snippets.append({
					'Type': fs_value['type'],
					'Rank Group': fs_value['rank_group'], 
					'Rank Absolute': fs_value['rank_absolute'],
					'Domain': fs_value['domain'],
					'Title': fs_value['title'],
					'Featured Title': fs_value['featured_title'],
					'URL': fs_value['url'],
					'Description': fs_value['description'],
					'Task Number': task_number},ignore_index=True)
	
	for task_number in range(0, len(json_data)):
		for a_value in json_data[task_number]['tasks'][0]['result'][0]['items']:
			if a_value['type'] == 'questions_and_answers':
				for qa_value in a_value['items']:
					df_qa = df_qa.append({
						'Type': a_value['type'],
						'Rank Group': a_value['rank_group'],
						'Rank Absolute': a_value['rank_absolute'],
						'Type_QA': qa_value['type'],
						'URL': qa_value['url'],
						'Question_Text': qa_value['question_text'],
						'Answer_Text': qa_value['answer_text'],
						'Source': qa_value['source'],
						'Domain': qa_value['domain'],
						'Votes': qa_value['votes'],
						'Task Number': task_number}, ignore_index=True)

	organic_results = pd.merge(df_data, df_keyword, on='Task Number')
	fs_results = pd.merge(df_featured_snippets, df_keyword, on='Task Number')
	qa_results = pd.merge(df_qa, df_keyword, on='Task Number')
	frames = [organic_results, fs_results, qa_results]
	all_results = pd.concat(frames)
	sorted_all_results = all_results.sort_values(['Task Number', 'Rank Absolute'], ascending=[True, True])
	top_20 = sorted_all_results[sorted_all_results['Rank Absolute'] <= 20]

	return top_20
			