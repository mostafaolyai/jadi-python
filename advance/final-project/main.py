import requests
import re
from bs4 import BeautifulSoup
from insert import create_car

url = "https://bama.ir/car"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=20)

soup = BeautifulSoup(response.text, "html.parser")

car_elements = soup.find_all(
    "div",
    class_="flex justify-between gap-4 h-full"
)

cars = []

for car in car_elements:
    spans = car.find_all("span")
    print(spans)
    name = spans[0].get_text(strip=True)
    model = spans[1].get_text(strip=True)
    year = int(spans[2].get_text(strip=True).split(".", 1)[0])
    kilometer_text = car.find("span", dir="ltr").get_text(strip=True)
    kilometer = int(
        kilometer_text.replace("کارکرد", "").replace("صفر", "0").replace("کیلومتر", "").replace(",", "").strip()
    ) if kilometer_text or kilometer_text!='' else 0

    price_element = car.select_one("p span.text-base.font-semibold")
    price_text = price_element.get_text(strip=True).replace("صفر", "") if price_element else ""
    price = int(price_text.replace(",", "")) if price_text else 0
    cars.append({
        "name": name,
        "model": model,
        "year": year,
        "kilometer": kilometer,
        "price": price
    })

print(cars)

for car in cars:
    create_car(car["name"], car["model"], car["year"], car["kilometer"], car["price"] )
