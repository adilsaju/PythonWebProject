
"""/home/adil/Downloads/cat1.jpg"""

from PIL import Image
i = Image.open("/home/adil/Downloads/cat1.jpg")
i.thumbnail((200,200))
i.show()