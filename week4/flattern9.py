

inplist=[1,[1,2],[[1,2],1]]   

def flatten(arrays:list):   
            
            #create empty list
            flatlist=[]
            while True:
                i=0   
                for i in arrays:
                    if isinstance(i,list):

                        flatten(i)
                    else:
                        flatlist.append(i)

                else:
                    break
                flatlist+=flatlist
            return  flatlist
print(flatten(inplist))        

