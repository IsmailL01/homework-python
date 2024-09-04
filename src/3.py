from enum import Enum


class Numbers(Enum):
    NEGATIVE_EVEN_NUMBER = "отрицательное четное число"
    NEGATIVE_ODD_NUMBER= "отрицательное нечетное число"
    ZERO_NUMBER = "нулевое число"
    POSITIVE_ODD_NUMBER = "положительное нечетное число"
    POSITIVE_EVEN_NUMBER = "положительное четное число"
    
    
def defineTextForEachNumber(number:int | str) -> str:
    convertedStringToNumber = number

    if(isinstance(number,str)):
        try:
            convertedStringToNumber = int(number)
        except ValueError:
            raise ValueError("Передано неправильное значение")

        
    if convertedStringToNumber == 0:
        return Numbers.ZERO_NUMBER.value
    elif convertedStringToNumber % 2 == 0:
          if convertedStringToNumber < 0:
             return Numbers.NEGATIVE_EVEN_NUMBER.value
          else:
            return Numbers.POSITIVE_EVEN_NUMBER.value
    
    elif convertedStringToNumber % 2 != 0:
        if convertedStringToNumber < 0:
            return Numbers.NEGATIVE_ODD_NUMBER.value
        else:
             return Numbers.POSITIVE_ODD_NUMBER.value


# Примеры    
    
print(defineTextForEachNumber(-5))  
print(defineTextForEachNumber(2))   
print(defineTextForEachNumber(7))   
print(defineTextForEachNumber(0))   
print(defineTextForEachNumber("0"))
