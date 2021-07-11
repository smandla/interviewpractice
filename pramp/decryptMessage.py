def encryptMessage(message):
    prevNumber = 1
    encrypted = ""
    j = 0 
    for char in range(len(message)):
        asciiVal = ord(message[char])
        newVal = asciiVal + prevNumber
        prevNumber = newVal
        while(prevNumber > ord('z')):
            prevNumber -= 26
        encrypted += chr(prevNumber)

        #message[char] += convert
    
    return(encrypted)
        #message[char] = convert
        
        #print(prevNumber)

        #print(char)
        # newVal = asciiVal + prevNumber
        # prevNumber = newVal
        # #print(prevNumber)
        # while(prevNumber > ord('z')):
        #     prevNumber -= 26
        # convert = chr(prevNumber)
    ##return message

message = "encyclopedia"
print(encryptMessage(message))

def decryptMessage(encryptMessage):
    encryptMessage = encryptMessage(message)
    decryptedMessage = ""
    prevNumber = 1
    for char in range(len(encryptMessage)):
        asciiVal = ord(encryptMessage[char])
        #print("asciiVal", asciiVal)
        asciiVal -= prevNumber
        
        while (asciiVal< ord('a')):
            asciiVal += 26
        decryptedMessage += chr(asciiVal)
        #print("decryptMessage", decryptedMessage)
        prevNumber += asciiVal
        #print(asciiVal)
    return decryptedMessage

       


print(decryptMessage(encryptMessage))