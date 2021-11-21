import os


class Numbergame:
    def __init__(self, *args: set):
        self.args=args

        self.lst=[]
        self.iter=10

    
    def groupten(self):
        groups=[None]*(max(self.args)//10+1)
        for number in self.args:
            idx=number//10
            if groups[idx] is None:
                groups[idx]=[]
            groups[idx].append(number)
        return groups
        
       
        


    
if __name__ == "__main__":
  oset = Numbergame( 10, 12, 10,28,4,1,3)
  #print(oset.addtolist())
  print(oset.groupten())


  # serches = Search(os.getcwd(), 1)
        
