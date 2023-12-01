def array_diff(a, b):
    returnstring = a
    a_str = ''.join([str(i) for i in a])
    b_str = ''.join([str(i) for i in b])
    start = None
    indexes = []
    if b == []:
        return returnstring
    while a_str.find(b_str, start) != -1:
        indexes.append(a_str.find(b_str, start))
        start = a_str.find(b_str, start)+len(b)
        if start >= len(a_str):
            break
    while indexes:
        i = indexes.pop()
        for j in range(len(b)):
            returnstring.pop(i)
    return returnstring

print(array_diff([1,2,3], [1,2]))