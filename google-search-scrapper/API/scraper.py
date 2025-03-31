import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI(debug=True)

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    value: str

googleWord = ''

@app.post("/string")
def receive_string(data: InputData):
    googleWord = data.value
    return {"message": "String received", "value": data.value}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


print(googleWord)
payload = {
    'source': 'google',
    'url': f"https://www.google.com/search?hl=en&q={"dog"}",
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
