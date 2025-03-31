import requests
from pprint import pprint

payload = {
    'source': 'google',
    'url': 'https://www.google.com/search?hl=en&q=newton',
    'parse': True
}

# Request for the job ID for Google search results.
response = requests.request(
    method='POST',
    url='https://realtime.oxylabs.io/v1/queries',
    auth=('Martin_1AbZT', 'xydWox_1pedpi_jufsab'),
    json=payload
)

# Extract job ID from response
job_id = response.json()['results'][0]['job_id']

# Get the first page of results in CSV format.
response_csv = requests.request(
    method='GET',
    url=f'http://data.oxylabs.io/v1/queries/{job_id}/results/normalized?format=csv&page=1',  # Assuming page=1 to restrict results to the first page
    auth=('Martin_1AbZT', 'xydWox_1pedpi_jufsab')
)

# Save the CSV data to a file
with open('results.csv', 'wb') as f:
    f.write(response_csv.content)

print('CSV saved as results.csv')
