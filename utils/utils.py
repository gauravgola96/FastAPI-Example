import logging
from uuid import uuid4

logger = logging.getLogger(__name__)


def generate_png_string():
    logger.info("Generating random string .png")
    return uuid4().hex[:6].upper().replace('0', 'X').replace('O', 'Y') + ".png"

