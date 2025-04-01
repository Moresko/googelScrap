import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import requests
from io import BytesIO

app = FastAPI(debug=True)

# address = ["http://localhost:3000"]
address = ["https://googel-scrap.vercel.app"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=address,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    value: str


@app.post("/")
def receive_string(data: InputData):
    global googleWord
    googleWord = data.value
    payload = {
        'source': 'google',
        'url': f"https://www.google.com/search?hl=sk&lr=lang_sk&q={googleWord}",
        'parse': True
    }

    response = requests.post(
        url='https://realtime.oxylabs.io/v1/queries',
        auth=('Martin_1AbZT', 'xydWox_1pedpi_jufsab'),
        json=payload
    )

    csvIndex = response.json()['results'][0]['job_id']

    response_csv = requests.get(
        url=f'http://data.oxylabs.io/v1/queries/{csvIndex}/results/normalized?format=csv&page=1',
        auth=('Martin_1AbZT', 'xydWox_1pedpi_jufsab')
    )

    csvFile = BytesIO(response_csv.content)

    return StreamingResponse(csvFile, media_type="text/csv", headers={"Content-Disposition": f"attachment; filename={googleWord}"})


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
