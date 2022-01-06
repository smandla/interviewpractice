def sumOfSubArrays(arr, n):
    temp = 0 
    result = 0 
    for i in range(0,n):
        temp = 0
        print("i", i)
        for j in range(i, n):
            print("j", j)
            temp += arr[j]
            print("temp", temp)
            result += temp
            print("result", result)
    return(result)


arr = [1, 2, 3, 4]
n = len(arr)
print(sumOfSubArrays(arr, n))