import streamlit as st
import dfs_scripts as ds
import pandas as pd
import base64
import time

client = ds.RestClient("adrian.skowron@brainly.com", "6a82d00b8f673110")

st.title("SERP Scraping Tool")

st.subheader("Put you keywords")
keywords_area = st.text_area("Keywords")
keywords_line_area = keywords_area.split('\n')
st.write("Number of keywords that you want to process:", len(keywords_line_area))
if len(keywords_line_area) > 100:
	st.warning(f"You reach maximum number of keywords. Only first {100} will be processed.")
	keywords_line_area = keywords_line_area[:100]

#Setup Sidebar
st.sidebar.subheader('Scrape Setup')
st.sidebar.write('Make setup before clicking **Send Keywords to Scrape**')
#Device picker
device = st.sidebar.selectbox("Select Device", ['desktop','mobile'])
#Market picker
market = st.sidebar.selectbox("Select Market",['US','PL','TR', 'IN'])
#Language picker
language = st.sidebar.selectbox("Select Language", ['en','pl','hi', 'tr'])
#Number of results picker
#results_number = st.sidebar.slider("Slide for number of results", min_value=0, max_value=100)

location_csv = pd.read_csv('locations_serp_2021_03_10.csv')
locations = location_csv[(location_csv['country_iso_code'] == market) & (location_csv['location_type'] == 'Country')]
for x in locations['location_code']:
	location_code = x

def Post_mobile_data2(keywords):
	post_data = dict()
	post_data[len(post_data)] = dict(
		language_code=language,
		location_code=location_code,
		device=device,
		keyword=keywords)
	time.sleep(0.75)
	response = client.post("/v3/serp/google/organic/task_post", post_data)
	#print(response)
	post_data.clear()

send_keywords_button = st.button('Send Keywords to Scrape')
@st.cache
def Send_kws():
	if send_keywords_button == True:
		for kws in keywords_line_area:
			Post_mobile_data2(kws)
	return
data = Send_kws()

progress_keywords = []
st.subheader('Check if keywords are ready to download')	
results_button = st.button('Check SERP Results')
if results_button == True:
	check_results = ds.Check_results()
	progress_keywords =+ check_results
	st.write(f"Number of keywords ready to scrape:", check_results, "from:", len(keywords_line_area))

st.write("Click **Download SERP Button** when all keywords will be prepared to download")

def download_link(object_to_download, download_filename, download_link_text):
	if isinstance(object_to_download, pd.DataFrame):
		object_to_download = object_to_download.to_csv(index=False)

	b64 = base64.b64encode(object_to_download.encode()).decode()
	return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'

st.subheader('Ready Keywords')
download_button = st.button('Download SERP Button')
if(download_button == True):
	get_serp = ds.Get_serp()
	process = ds.Data_json_process(get_serp)
	st.write(process)
	tmp_download_link = download_link(process, 'serp_results.csv', 'Click here to download your data!')
	st.markdown(tmp_download_link, unsafe_allow_html=True)