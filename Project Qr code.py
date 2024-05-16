import qrcode
import image
qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5,
)

data = "https://www.linkedin.com/in/vaibhav-srivastava-0b686622a/"
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",black_colour = "white")
img.save("test.png")

#Vaibhav Srivastava
