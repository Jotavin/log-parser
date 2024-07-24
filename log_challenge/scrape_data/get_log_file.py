import requests
from bs4 import BeautifulSoup as bs


url = 'URL'
response = requests.get(url)


soup = bs(response.text, 'html.parser')
html_content = soup.find('table', 'highlight tab-size js-file-line-container js-code-nav-container js-tagsearch-file')

raw_text = html_content.getText(separator='\n', strip=True)

with open('quake_info.txt', 'w', encoding='utf-8') as file:
    file.write(raw_text)