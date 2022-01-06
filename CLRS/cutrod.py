import sys

def cutrod(n, price):
    val = [0 for x in range(n+1)]
    val[0] = 0
    INT_MIN = -34567
    print("price[0]", price[0])
    # Build the table val[] in bottom up manner and return
    # the last entry from the table
    for i in range(1, n+1):
        max_val = INT_MIN
        print("i",i)
        for j in range(i):
            print("j", j)
            print("val:",val)
            print("val", val[i-j-1])
            print("price", price[j])
            max_val = max(max_val, price[j] + val[i-j-1])
            print("max", max_val)
        val[i] = max_val
        
 
    return val






   


price = [1, 5, 8, 9, 10, 17, 17, 20]
print(cutrod(4, price))