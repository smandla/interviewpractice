def findDuplicates(arr1, arr2):
    ht = {}
    duplicates = []
    for i in range(len(arr1)): 
        ht[arr1[i]] = 1
    for i in range(len(arr2)): 
        if arr2[i] in ht: 
            ht[arr2[i]] += 1
        for key,val in ht.items():
          if val == 2 a: 
                duplicates.append(key)
    return duplicates



    print(ht)

arr1 = [1, 2, 3]
arr2 = [3, 6, 7, 3, 3, 20]
print(findDuplicates(arr1, arr2))