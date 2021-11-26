from abc import ABCMeta
import builtins
import math


math.ceil(5.6)
dir(builtins)

class Card():
    def __init__(self,name,number,date_data, cvv) -> None:
        self.name = name
        self.number = number
        self.date_data = date_data
        self.cvv = cvv
    @classmethod
    def create_card(clss,name,number,date_data, cvv):
        if not number.isnumeric() or len(number) != 16 :
            print("can't create card")
            return None
        else:
            return clss(name,number,date_data, cvv)


cards = []
card1 = Card.create_card("ADIL SAJU" , "5640253412817199" , ( "07/20" ,  "06/27"  ) , "197"   )
print(card1)
print(type(card1))

