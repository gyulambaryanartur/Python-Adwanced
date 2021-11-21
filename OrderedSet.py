import os


class OrderedSet:
    def __init__(self, *args: set):
        self.args=args

        self.lst=[]

    def add(self,item:str):
        for arg in  self.args:
            self.lst.append(arg)
        self.lst.append(item)    
        return set(self.lst)   
    def __getitem__(self,key):
        return list(set(self.lst))[key]     
    def __repr__(self):
        return f'OrderedSet:{set(self.lst)}'
    def remove(self,item:str) :
           self.lst.remove(item)
           return set(self.lst)

if __name__ == "__main__":
  oset = OrderedSet('meta', 10, 12, 10)
  oset.add(31)
  oset.remove(31)
  print(oset,"  ",oset[2])
  print(12 in oset)
  for item in oset:
      print(item)


  # serches = Search(os.getcwd(), 1)
        
