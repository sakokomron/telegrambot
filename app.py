from random import randint

rand = 0
def son(kluch):
    if (kluch):
        rand = randint(1,100)
    return rand


print(son(True))
print(son(False))
