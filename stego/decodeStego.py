import base64, urllib.request
from stegano import lsb

imgurl = input("Insert imgur link: ")
urllib.request.urlretrieve(url=imgurl, filename="dementorDecode.png")
imgDecode = lsb.reveal("dementorDecode.png")
print("Message Found")
print("Enrypted message is " + imgDecode)
msgEncrypted = imgDecode.encode("utf-8")
msgDecode = base64.b64decode(msgEncrypted)
print("Decode message is : " + msgDecode.decode("utf-8"))