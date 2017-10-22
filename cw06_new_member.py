"""
Kata: Categorize New Member
Best Practice by taw and others:
def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]
"""

def openOrSenior(data):
    # Hmmm.. Where to start?
    newList = []
    for item in data:
        if item[0] >= 55 and item[1] > 7:
            newList.append("Senior")
        else:
            newList.append("Open")
    return newList