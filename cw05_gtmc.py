def get_middle(s):
    #your code here
    size = len(s)
    if size % 2 != 0:
        return s[int(size /2)]
    else: 
        return s[int(round(size /2) - 1)] + s[int(round(size /2))]


