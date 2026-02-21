# create a pdf form of an html file

import requests
import urllib.parse
from config import config as cfg

filename="andrew_beatty_books.pdf"

target_url= "https://andrewbeatty1.pythonanywhere.com/bookviewer.html"

api_key = cfg['html_to_pdf_key']

api_url = "https://api.html2pdf.app/v1/generate"

params = {'url':target_url, 'apiKey': api_key}
parsed_params = urllib.parse.urlencode(params)

request_url= api_url + "?" + parsed_params

response = requests.get(request_url)
print(response.status_code)

result = response.content

with  open(filename, 'wb') as handler:
    handler.write(result)
 #   result = response.content
    #json.dump(result, fp, indent=4)

