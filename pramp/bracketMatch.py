def bracketMatch(brackets):
    countOpen = 0 
    countClose = 0
    for char in brackets:
        if char == '(':
            countClose += 1
        elif char == ')':
            countClose -= 1
            if(countClose < 0):
                countClose += 1
                countOpen += 1
                
    return countOpen +  countClose

brackets = '()()(((('
print(bracketMatch(brackets))