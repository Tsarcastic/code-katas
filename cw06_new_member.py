"""

Kata: Categorize New Member.
Best Practice by taw and others:
def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]

"""


def open_or_senior(data):
    """Hmmm.. Where to start. Open or senior."""
    new_list = []
    for item in data:
        if item[0] >= 55 and item[1] > 7:
            new_list.append("Senior")
        else:
            new_list.append("Open")
    return new_list
