import qrcode

def gen_qr(bn, num):
	# Create qr code instance
	qr = qrcode.QRCode(
	    version = 1,
	    error_correction = qrcode.constants.ERROR_CORRECT_H,
	    box_size = 20,
	    border = 2,
	)

	# Add data: CCB-URL for media codes
	qr.add_data(f'https://www.ccbuchner.de/clip_code-{bn}-{num:02d}/')
	qr.make(fit=True)

	# Create an image from the QR Code instance
	img = qr.make_image()
	# Save image as png
	img.save(f'{bn}_{num:02d}.png')
	print(f'{bn}_{num:02d}.png')

# Get user input
bn = input('Bitte BN eingeben:\n')
num = int(input('Wie viele QR-Codes werden benötigt?\n'))

for user_num in range(1, num + 1):
	gen_qr(bn, user_num)