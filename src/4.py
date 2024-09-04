


from enum import Enum

class MathActions(Enum):
    PLUS = 1
    MINUS = 2
    MULTI = 3
    DIVIDE = 4
    
def byActionNumberDoSomething(actionNumber:int, numberA:int,numberB:int) -> int:
    if actionNumber == MathActions.PLUS.value:
        return numberA + numberB
    elif actionNumber == MathActions.MINUS.value:
        return numberA - numberB
    elif actionNumber == MathActions.MULTI.value:
        return numberA * numberB
    elif actionNumber == MathActions.DIVIDE.value:
        if numberB != 0:
            return numberA / numberB
        else: 
            raise ValueError("На ноль делить нельзя")
    else:
        raise ValueError("Неизвестное математическое действие")
    
    


# Примеры    

print(byActionNumberDoSomething(1,2,2))
print(byActionNumberDoSomething(2,2,2))
print(byActionNumberDoSomething(3,2,2))
print(byActionNumberDoSomething(4,2,2))