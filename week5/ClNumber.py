class Number:
    def __init__(self,num:int):
        self.num=num
    def __len__(self):
        return len(str(self.num))
    def __getitem__(self,key):
        return str(self.num)[key]
    def __add__(self,other):
        if isinstance(other,int):
            other=Number(other)
        return  Number(self.num+other.num)        
if  __name__ == "__main__":
    a=Number(156)
    b=Number(251)
    print(len(a))
    print(a[2])
    print(a+b)
    print(a+12)