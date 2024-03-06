mystr = input()
def c(s): 
    upper = sum(1 for i in s if i.isupper())
    lower = sum(1 for k in s if k.islower())
    return upper, lower
u, l = c(mystr)
print("Uc num:", u, "\nLC num:", l)
