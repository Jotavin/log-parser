import requests
from bs4 import BeautifulSoup as bs

url = 'https://gist.github.com/cloudwalk-tests/be1b636e58abff14088c8b5309f575d8'
response = requests.get(url)


soup = bs(response.text, 'html.parser')
html_content = soup.find('table', 'highlight tab-size js-file-line-container js-code-nav-container js-tagsearch-file')

raw_text = html_content.getText(separator='\n', strip=True)

with open('log_file.txt', 'w', encoding='utf-8') as file:
    file.write(raw_text)