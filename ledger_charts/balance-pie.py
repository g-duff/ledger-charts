import json

from matplotlib import pyplot as plt

category = 'expenses'

with open('./test.json') as openfile:
    balances = json.load(openfile)

accounts = [b['sub_accounts'] for b in balances if b['category']==category][0]

account_names = [a['account'] for a in accounts]
amounts = [a['amount'] for a in accounts]

fig, ax = plt.subplots()
ax.pie(amounts, labels=account_names, autopct='%1.1f%%')
plt.show()
