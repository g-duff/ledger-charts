import re


def top_level_expenses(account_balance):
    pattern = r"expenses(?::[\w\s]+)"
    return re.match(pattern, account_balance["account"])
