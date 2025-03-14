"""Logging configuration module."""

import logging

import colorlog


def setup_logging() -> logging.Logger:
    """
    Set up logging with color formatting.

    Returns:
        logging.Logger: Configured logger instance

    """
    log_formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    logger = logging.getLogger("app")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)
    return logger


# アプリケーション全体で使用するロガーインスタンス
app_logger = setup_logging()
