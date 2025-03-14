"""FastAPI application for file upload handling."""

from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse

from .log_config import app_logger


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
        app_logger.warning("No file uploaded")
        return JSONResponse(content={"message": "No file uploaded"}, status_code=400)

    app_logger.info("File uploaded: %s", file.filename)
    return JSONResponse(content={"filename": file.filename})
