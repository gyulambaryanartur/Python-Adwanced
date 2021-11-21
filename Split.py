import pandas


class Split:
    def __init__(self):

        self.lst=[]
    def Split(self,string:str,seperator:str):
          firstindex=string.find(seperator)
          if firstindex>=0:

           self.lst.append(string[:firstindex])
          secondind=firstindex+len(seperator)
          if len(string[secondind:])>0 and firstindex>=0:
              string=string[secondind:]
              self.Split(string,seperator)
          else:
             self.lst.append(string)
          
             
   

          return self.lst

            
        
   

if __name__ == "__main__":
  spl=Split()
  print(spl.Split('artsakorhhasanat','sa'))

  


  # serches = Search(os.getcwd(), 1)
        
