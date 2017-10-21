def openOrSenior(data):
    # Hmmm.. Where to start?
    newList = []
    for item in data:
        if item[0] >= 55 and item[1] > 7:
            newList.append("Senior")
        else:
            newList.append("Open")
    return newList