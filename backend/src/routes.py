"""Route handlers for FastAPI application."""

from fastapi import FastAPI, UploadFile
from fastapi.responses import JSONResponse, RedirectResponse

from src.config.log_config import app_logger


def setup_routes(app: FastAPI) -> None:
    """Set up route handlers for the FastAPI application."""

    @app.get("/", response_class=RedirectResponse)
    async def root() -> RedirectResponse:
        """Redirect root path to API documentation."""
        return RedirectResponse(url="/docs")

    @app.post("/api/file/")
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
