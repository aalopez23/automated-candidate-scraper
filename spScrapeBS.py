from bs4 import BeautifulSoup
import requests

url = "https://advantechgsenterprisesinc.sharepoint.com/HR/TR/RESUMES%20%20INTERVIEWS/Forms/AllItems.aspx?e=2%3AnfVEJA&at=9"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody