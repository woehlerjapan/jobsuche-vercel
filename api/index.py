import requests
from fastapi import FastAPI, Query

app = FastAPI()

BASE_URL = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs"
CLIENT_ID = "jobboerse-jobsuche"

HEADERS = {
    "X-API-Key": CLIENT_ID,
    "Content-Type": "application/json",
}


@app.get("/jobs")
@app.get("/api/jobs")
def jobs(
    what: str | None = Query(None, description="Jobtitel"),
    where: str | None = Query(None, description="Ort"),
    size: int = Query(10, ge=1, le=50),
    page: int = Query(1, ge=1, le=1000),
):
    params = {"page": page, "size": size}
    if what:
        params["was"] = what
    if where:
        params["wo"] = where

    resp = requests.get(BASE_URL, headers=HEADERS, params=params, timeout=20)
    resp.raise_for_status()
    return resp.json()


@app.get("/", include_in_schema=False)
@app.get("/api", include_in_schema=False)
def root():
    return {"status": "ok", "info": "Nutze /api/jobs"}
