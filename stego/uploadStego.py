#https://www.geeksforgeeks.org/image
#https://www.geeksforgeeks.org/encoding-and-decoding-base64-strings-in-python/
import pyimgur, base64, requests, json
from stegano import lsb

mess = input("Input message:")
mess_utf = mess.encode("utf-8")
mess_b64 = base64.b64encode(mess_utf)
print(f'Encoded String : '+ mess_b64.decode("utf-8"))
mess_b64dec = mess_b64.decode("utf-8")
img = lsb.hide("dementor.png", message=mess_b64dec)
img.save("dementorStego.png")
img_decode = lsb.reveal("dementorStego.png")
print(img_decode)
print("Message injected successfully!!")
PATH = "dementorStego.png"
CLIENT = "7d47254c4bb6c3d"
imgUpload = pyimgur.Imgur(CLIENT)
uploaded = imgUpload.upload_image(path=PATH, title="Stego")
print(uploaded.link)