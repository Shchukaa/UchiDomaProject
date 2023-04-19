import io
import json
import cv2
import requests
from pprint import pprint
import re

img = cv2.imread("screenshot4.jpg")
url_api = "https://api.ocr.space/parse/image"

# Сжимаем изображение, т.к. api не принимает больше 1mb
_, compressedimage = cv2.imencode(".jpg", img, [1, 90])
file_bytes = io.BytesIO(compressedimage)

result = requests.post(url_api,
                       files={"screenshot.jpg": file_bytes},
                       data={"apikey": "K89439205688957",
                             "language": "rus"})


result = result.content.decode()
result = json.loads(result)
pprint(result)
text = result["ParsedResults"][0]["ParsedText"]
print(text)

# Доделать регулярку
def input_corr(text):
    numbers = re.findall(r'\d+([\-\+]\d+)*\s[а-я]+(\/([а-я])+)*\d*')
