def TensAndUnitsChangePlaces(number:int):
    strNumber = str(number)
    numberLength = len(strNumber)
    tens =  strNumber[numberLength - 2]
    units = strNumber[ numberLength -1]
    current = strNumber
    newNumber = current[0] + units + tens
    return int(newNumber)
    
# Примеры    

print(TensAndUnitsChangePlaces(424)) 
print(TensAndUnitsChangePlaces(335)) 
print(TensAndUnitsChangePlaces(535)) 