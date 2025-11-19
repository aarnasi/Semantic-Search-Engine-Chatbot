"""Central logging configuration."""

from __future__ import annotations

import logging
from logging import config as logging_config


def configure_logging(level: int = logging.INFO) -> None:
    """Configure structured logging for the application."""

    logging_config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "standard": {
                    "format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
                }
            },
            "handlers": {
                "default": {
                    "level": level,
                    "formatter": "standard",
                    "class": "logging.StreamHandler",
                }
            },
            "root": {"handlers": ["default"], "level": level},
        }
    )


