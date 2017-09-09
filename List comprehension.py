a = [1, 2, 3]
b = [n * 2 for n in a]
print (b)

c = ["Mohit", "Menita", "Siddharth", "Riya", "Donna", "Ted"]
d = [name for name in c if (len(name) <= 5)]
print(d)

dict = {"Jamuna": 80, "Nenumal": 85, "Mohit": 20}
items = dict.items()
print( items)
a1, b1, c1 = items
print(a1[1])

for key in dict:
    print (key),
n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
zip = zip(c, a)
print("\n", zip)

# zdict = dict(zip)
# print "lala ", zdict

print(n[::4])
