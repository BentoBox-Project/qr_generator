from package.util import get_qr_code
import qrcode


def test_get_qr_code():
	text = "This is my new text"
	result = get_qr_code(text)
	assert isinstance(result, qrcode.image.pil.PilImage)