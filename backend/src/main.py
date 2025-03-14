"""FastAPI app"""

import logging

from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse

# ロギング設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# logger format
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

app = FastAPI()

# CORS の設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # フロントエンド（Next.js）からのリクエストを許可
    allow_credentials=True,
    allow_methods=["*"],  # すべての HTTP メソッド（GET, POST, PUT など）を許可
    allow_headers=["*"],  # すべての HTTP ヘッダーを許可
)


@app.get("/", response_class=RedirectResponse)
async def root() -> RedirectResponse:
    """Root path"""
    # docs へリダイレクトする
    return RedirectResponse(url="/docs")


@app.post("/uploadfile/")
async def upload_file(file: UploadFile = None) -> JSONResponse:
    """Upload file"""
    if file is None:
        logger.warning("No file uploaded")
        return JSONResponse(content={"message": "No file uploaded"}, status_code=400)
    logger.info("File uploaded: %s", file.filename)
    return JSONResponse(content={"filename": file.filename})
