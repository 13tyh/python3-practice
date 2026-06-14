import logging


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)


def mask_secret(value: str | None) -> str:
    if not value:
        return ""
    if len(value) <= 4:
        return "***"
    return f"{value[:2]}...{value[-2:]}"
