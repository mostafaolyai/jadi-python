import requests
import re
from bs4 import BeautifulSoup

url = "https://divar.ir/s/tehran"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=20)

soup = BeautifulSoup(response.text, "html.parser")

ads = {}

# پیدا کردن تمام عناصری که عبارت نردبان دارند
ladder_elements = soup.find_all(
    string=lambda text: text and "نردبان" in text
)

for element in ladder_elements:

    parent = element.parent

    # حرکت به سمت والدها برای پیدا کردن کارت آگهی
    for _ in range(8):

        if parent is None:
            break

        link = parent.find(
            "a",
            href=re.compile(r"/v/")
        )

        if link:
            href = link.get("href")

            title = link.get_text(strip=True)

            ads[href] = {
                "title": title,
                "url": "https://divar.ir" + href
            }

            break

        parent = parent.parent


# چاپ نتایج
print(f"تعداد آگهی‌های نردبان: {len(ads)}")

for ad in ads.values():

    print("-" * 50)

    print("Title:", ad["title"])

    print("URL:", ad["url"])