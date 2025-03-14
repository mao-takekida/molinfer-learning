"""FastAPI app"""

import logging
from pathlib import Path

from fastapi import FastAPI, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

# ロギング設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# 静的ファイルを提供
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def root() -> HTMLResponse:
    """Root path"""
    with (Path(__file__).parent / "static" / "index.html").open() as f:
        return HTMLResponse(content=f.read(), status_code=200)


@app.post("/uploadfile/")
async def upload_file(file: UploadFile = None) -> JSONResponse:
    """Upload file"""
    if file is None:
        return JSONResponse(content={"message": "No file uploaded"}, status_code=400)
    logger.info("File uploaded: %s", file.filename)
    return JSONResponse(content={"filename": file.filename})
