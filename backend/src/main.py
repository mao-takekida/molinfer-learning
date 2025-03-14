"""FastAPI application for file upload handling."""

import logging

import colorlog
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse


def setup_logging() -> logging.Logger:
    """
    Set up logging with color formatting.

    Returns:
        logging.Logger: Configured logger instance

    """
    log_formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)s - <%(name)s> - [%(levelname)s] - %(message)s",
        datefmt="%Y/%m/%d|%H:%M:%S",
    )
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)
    return logger


def setup_cors(app: FastAPI) -> None:
    """Set up CORS middleware for the FastAPI application."""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"],  # フロントエンド（Next.js）からのリクエストを許可
        allow_credentials=True,
        allow_methods=["*"],  # すべての HTTP メソッド（GET, POST, PUT など）を許可
        allow_headers=["*"],  # すべての HTTP ヘッダーを許可
    )


# アプリケーションの初期化
logger = setup_logging()
app = FastAPI(
    title="File Upload API",
    description="API for handling file uploads with FastAPI",
    version="1.0.0",
)
setup_cors(app)


@app.get("/", response_class=RedirectResponse)
async def root() -> RedirectResponse:
    """Redirect root path to API documentation."""
    return RedirectResponse(url="/docs")


@app.post("/uploadfile/")
async def upload_file(file: UploadFile | None = None) -> JSONResponse:
    """
    Handle file upload endpoint.

    Args:
        file: The uploaded file object. Optional, but required for successful upload.

    Returns:
        JSONResponse: Response containing upload status and filename if successful.

    """
    if file is None:
        logger.warning("No file uploaded")
        return JSONResponse(content={"message": "No file uploaded"}, status_code=400)

    logger.info("File uploaded: %s", file.filename)
    return JSONResponse(content={"filename": file.filename})
