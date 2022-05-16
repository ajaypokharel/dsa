# -------------------------------------------------
# CSC 211 - hashing with strings
# ------------------------------------------------- 

def h(key,m):
    value=0
    for ch in key:
        value+=ord(ch)
    return value%m

myString="Good morning"
m=100

print(h(myString,m))

