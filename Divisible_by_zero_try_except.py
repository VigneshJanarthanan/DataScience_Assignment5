a = 0.0
b = 5.0
try:
    c = b/a
except ZeroDivisionError:
    print("A ZeroDivisionError! But we know how to handle this....")
    c = float('Inf')
except:
    print("We don't know this type of error!")
    raise
else: 
    print("We encountered no errors!")
print(c)