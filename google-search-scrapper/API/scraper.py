import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import requests
from io import BytesIO

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


@app.post("/string")
def receive_string(data: InputData):
    global googleWord
    googleWord = data.value
    payload = {
        'source': 'google',
        'url': f"https://www.google.com/search?hl=en&q={googleWord}",
        'parse': True
    }

    response = requests.post(
        url='https://realtime.oxylabs.io/v1/queries',
        auth=('Martin_1AbZT', 'xydWox_1pedpi_jufsab'),
        json=payload
    )

    job_id = response.json()['results'][0]['job_id']

    # Fetch the CSV result
    response_csv = requests.get(
        url=f'http://data.oxylabs.io/v1/queries/{job_id}/results/normalized?format=csv&page=1',
        auth=('Martin_1AbZT', 'xydWox_1pedpi_jufsab')
    )

    # Create an in-memory binary stream
    csv_file = BytesIO(response_csv.content)

    # Dynamically set the filename to the googleWord
    filename = f"{googleWord}_results.csv"

    # Return the CSV file as a streaming response to trigger the download
    return StreamingResponse(csv_file, media_type="text/csv", headers={"Content-Disposition": f"attachment; filename={googleWord}"})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
