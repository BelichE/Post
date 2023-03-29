import requests

# Установить URL и путь к изображению
url = 'http://ramilsaf.ru/'
image_path = './test_image.jpg'

# Создать POST-запрос с изображением в формате multipart/form-data
response = requests.post(url, files={'file': open(image_path, 'rb')})

# Проверить статус-код и формат ответа
if response.status_code == 200:
    results = response.text
    print(f"Results: {results}")
else:
    print(f"Error: {response.text}")
