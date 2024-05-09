totalCell=int(input("T total = "))
x= int (input("num of COLUMNS = "))
expected=0
tr = int(input("total row = "))
for i in range (x):
    tc = int(input("total column = "))
    expected = ( tr * tc ) / totalCell
    print(expected)
    print("\n-------\n")
