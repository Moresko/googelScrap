import requests
from pprint import pprint

payload = {
    'source': 'google',
    'url': 'https://www.google.com/search?hl=en&q=newton',
    'parse': True
}

response = requests.request(
    method='POST',
    url='https://realtime.oxylabs.io/v1/queries',
    auth=('Martin_1AbZT','xydWox_1pedpi_jufsab'),
    json=payload
)

job_id = response.json()['results'][0]['job_id']

response_csv = requests.request(
    method='GET',
    url=f'http://data.oxylabs.io/v1/queries/{job_id}/results/normalized?format=csv',
    auth=('Martin_1AbZT','xydWox_1pedpi_jufsab')
)

with open('results.csv', 'wb') as f:
    f.write(response_csv.content)
