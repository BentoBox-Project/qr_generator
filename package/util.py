import qrcode
import logging


def get_qr_code(text):
    """
    :param text:
    :type text: string
    :return: qrcode.image.pil.PilImage
    """
    if not text or not isinstance(text, str):
        logging.info("No valid text found")
        return None

    return qrcode.make(text)


def get_qr_from_single_json(json_params):
    """
    :param json_params:
    :return: qrcode.image.pil.PilImage
    """
    params_str = ""
    for key, value in json_params.items():
        params_str = f"{key}: {value}, " + params_str

    params_image = get_qr_code(params_str)

    return params_image
