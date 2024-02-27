import requests
from bs4 import BeautifulSoup

url = "https://as.com/futbol/internacional/luis-enrique-cambia-al-psg-n/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

titulo = soup.title.text.strip()
paragraphs = soup.find_all('p')
autor = input("Andrés Onrubia:")


print(f"Título del artículo: {titulo},{paragraphs},{autor}")