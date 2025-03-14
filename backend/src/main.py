"""FastAPI app"""

import logging

import colorlog
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse

# 色付きのログフォーマットを設定
log_formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(asctime)s - <%(name)s> - [%(levelname)s] - %(message)s",  # ログのフォーマット
    datefmt="%Y/%m/%d|%H:%M:%S",  # 日付のフォーマット
)

# ログハンドラを作成
console_handler = logging.StreamHandler()

# ハンドラにフォーマットを設定
console_handler.setFormatter(log_formatter)

# ログハンドラを作成
console_handler = logging.StreamHandler()

# ハンドラにフォーマットを設定
console_handler.setFormatter(log_formatter)

# ロガーを作成
logger = logging.getLogger()
# ログレベルを設定
logger.setLevel(logging.DEBUG)

# ハンドラをロガーに追加
logger.addHandler(console_handler)


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
