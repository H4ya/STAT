##chi
total=0
x=int(input(" num of cells (without totals): "))
for i in range (x):
    ob = int(input("observed = "))
    ex = float(input("expected = "))
    total = ((ob - ex)**2)/ ex + total
print(total)
