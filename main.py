from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse

import requests
import json

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:1420",
    "http://localhost:5050",
    "https://pro.openbb.dev",
    "https://pro.openbb.co",
    "https://excel.openbb.co",
    "https://excel.openbb.dev",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(url="/docs")


@app.get("/health", include_in_schema=False)
def health_check():
    return {"status": "ok"}


@app.get("/widgets.json")
def get_widgets():
    """Widgets configuration file for the OpenBB Terminal Pro"""
    return JSONResponse(content=json.load((Path(__file__).parent.resolve() / "widgets.json").open()))


@app.get("/maverick-top-stocks")
def get_maverick_top_stocks():
    """Get the Maverick Top Stocks Report from the Capital Companion API"""
    response = requests.get("https://capitalcompanion.io/maverick-top-stocks")

    if response.status_code == 200:
        return response.json()["maverick_stocks"]

    print(f"Request error {response.status_code}: {response.text}")
    return JSONResponse(content={"error": response.text}, status_code=response.status_code)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5050)
