import requests
from bs4 import BeautifulSoup

#getting the URL
url = input("Enter URL: ")

#get the webpage
response = requests.get(url)
html_content = response.content

#parse the response
temp = BeautifulSoup(html_content, 'html.parser')

