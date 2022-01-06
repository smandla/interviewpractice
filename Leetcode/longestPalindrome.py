def longestPalindrome(string):
    result = ""
    resLength = 0
    for i in range(len(string)):
        l, r = i, i
        print("outer L", l)
        print("outer R", r)
        while( l >= 0 and r < len(string) and string[l] == string[r]):
            if(r - l + 1) > resLength: 
                result = string[l:r + 1]
                resLength = r - l + 1
                print("result,", result)
                print("resLength,", resLength)
            l -= 1
            print("L: ",l)

            r += 1
            print("R: ",r)
    
        l, r = i, i + 1
        
        while (l >= 0 and r < len(string) and string[l] == string[r]):
            if(r - l + 1 > resLength):
                result = string[l:r+1]
                resLength = r - l + 1
            l -= 1
            r += 1
    return result
    
        

string = ''
print(longestPalindrome(string))