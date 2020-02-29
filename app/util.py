import qrcode
from app import app


def get_qr_code(text):
    """
    :param text:
    :type text: string
    :return:
    """
    if not text or not isinstance(text, str):
        app.logger.info("No valid text found")
        return None

    return qrcode.make(text)
