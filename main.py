import qrcode
from qrcode.constants import ERROR_CORRECT_L

qr = qrcode.QRCode(
  version=3,
  error_correction=ERROR_CORRECT_L,
  box_size=3,
  border=5
)

link = str(input("Enter the link you want: "))
qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
file_name= input("Enter the name of your file: ")
# print(file_name + ".png")

img.save(file_name + '.png')