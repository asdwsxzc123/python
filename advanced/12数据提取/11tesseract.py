from PIL import Image
import pytesseract
file_path = '/user/local/img/1.png'
img = Image.open(file_path)
print(pytesseract.image_to_string(img))
