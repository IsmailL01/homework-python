def findTens(number:int):
    strNumber = str(number)
    copyNumber = number
    numberLen = len(strNumber)
    lenForTens = numberLen - 1
    dividedNumber =  (10**lenForTens)
    strNumber = str(copyNumber / dividedNumber)
    strNumber = strNumber[::-1]
    strNumber = strNumber[2]
    return strNumber
 
    
# Примеры    
print(findTens(3534))
print(findTens(2535))
print(findTens(10013))
    