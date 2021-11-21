class add:
    def __init__(self,num:int):
        self.num=num
    def __call__(self,num ):
        a=0
        self.num+=num
        return self
    def __repr__(self):
        return str(self.num) 


if  __name__ == "__main__":
    print(add(1)(2)(4))        