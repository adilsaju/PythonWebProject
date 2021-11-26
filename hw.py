



class Int_list(list):
    def __init__(self):
        pass

    def append(self, __object) -> None:
        # if isinstance(__object,int) == True:
        #     return super().append(__object)
        # else:
        #     raise Exception("type not allowed")
        if isinstance(__object,int) == False:
            raise Exception("type not allowed")


a=Int_list()
print(type(a))
print(a)
a.append(22)
print(a)