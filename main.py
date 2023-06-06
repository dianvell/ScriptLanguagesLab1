import requests
from bs4 import BeautifulSoup

#Слово, которое должно содержаться в статье
word=input("Enter keyword: ")

# Загрузка страницы
url = 'https://www.thesun.co.uk/news/'
response = requests.get(url)

#Создание файла для записи статей
file = open("articles.txt", 'w', encoding="utf-8")

# Парсинг HTML-кода страницы
soup = BeautifulSoup(response.content, 'html.parser')

#Заголовки статей
title=soup.findAll("span", class_="teaser__headline t-p-color")

#Аннотации статей
annotation=soup.findAll("h3", class_="teaser__subdeck")

#Заголовок и аннотация первой(главной) статьи(она отличается от остальных)
firstArticleTitle=soup.find("span",class_="splash-teaser-kicker")
firstArticleAnnotation=soup.find("span",class_="css-sozy86")

#Объединение первой статьи с остальными
title.insert(0,firstArticleTitle)
annotation.insert(0,firstArticleAnnotation)

#Массив статей
for i in range(len(title)):
    print("Title: ", title[i].text)
    print("Annotation: ", annotation[i].text)
    print(" ")

#Объединение аннотации и заголовка
    text=title[i].text+annotation[i].text

    if word in text.casefold():
        file.write("Title: " + title[i].text + "\n")
        file.write("Annotation: " + annotation[i].text + "\n")
        print(" ")

file.close()




