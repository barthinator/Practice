
count = 0

a = "ana"
b = "a"

#Grabs unicode char values 97='a' to 123='z'
for i in range(97, 123):
    aTotals = a.count(chr(i))
    bTotals = b.count(chr(i))
    count += abs(aTotals - bTotals)
print(count)
