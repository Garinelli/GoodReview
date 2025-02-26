from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Инициализация драйвера (например, для Chrome)
driver = webdriver.Chrome()

# Открытие сайта
driver.get(
    "https://www.wildberries.ru/catalog/220155638/feedbacks?imtId=13718599&size=350041043"
)

# Пауза для загрузки начального контента
time.sleep(5)

# Получение начальной высоты страницы
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Прокрутка страницы до конца
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Пауза для загрузки нового контента
    time.sleep(5)

    # Получение новой высоты страницы после прокрутки
    new_height = driver.execute_script("return document.body.scrollHeight")

    # Если высота страницы не изменилась, значит, мы достигли конца
    if new_height == last_height:
        print("ВЫСОТА ОСТАЛАСЬ НЕИЗМЕННОЙ!")
        break

    # Обновление последней высоты страницы
    last_height = new_height


print("СЕЙЧАС ЗАКРОЮСЬ")
time.sleep(5)
# Закрытие браузера
driver.quit()
