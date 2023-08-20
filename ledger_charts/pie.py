import json
import re

import matplotlib.pyplot as plt


with open("./assets.json") as openfile:
    balance = json.load(openfile)

assets = [b for b in balance if re.match(r"assets(?::[\w\s]+){2}", b["account"])]

amounts = [a["balance"] for a in assets]
account_names = [a["account"] for a in assets]

fig, ax = plt.subplots()
ax.pie(amounts, labels=account_names, autopct="%1.1f%%")
plt.show()
