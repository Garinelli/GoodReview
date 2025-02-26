from pathlib import Path
from random import choice, randint

START = "«"
END = "»"

mas = []

path = Path(__file__).parent
with open(f"{path}./text.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        a = line.strip()
        if START in a and END in a:
            b = a[a.find(START) + len(START) : a.find(END)]
            mas.append(b)

with open(f"{path}./reviews.txt", "w", encoding="utf-8") as f:
    for review in mas:
        d = {
            "user_review": f"{review}",
            "reviews_date": f"202{randint(0, 9)}-{randint(0, 11):02}-{randint(0, 11):02}",
            "star_review": 5,
            "text_len": len(review),
            "written_by_bot": 1,
            "has_media": choice([True, False]),
        }
        f.write(f"{d},\n")

# flag = False
# mas = []
# for symb in a:
#     if symb == START:
#         flag = True
#     if flag is True:
