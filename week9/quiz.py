import configparser
import urllib.request, json
import string
#class Quiz:
    
letters = string.ascii_uppercase

config = configparser.ConfigParser()
config.read('config.ini')
#print(config.sections())
url=config['quiz']['url']
print(url)
response = urllib.request.urlopen(url)

data = json.loads(response.read())

totext=""
for number,i in enumerate(data['questions'],1):
    question=f'{number}). {i["question"]}\n'
    totext+=f'{question}'
    print(question)
    answerletter=[]
    
    for let,text in zip(letters,i['answers']):
       
       print(f' { let})',text)
       answerletter.append(f'{let})')

    #print(answerletter)
    while True:
     answer=f'{input("Input answer option:")})'
     
     
     if  answer in answerletter:
         getind=answerletter.index(answer)
         answerletter[getind]=f'*{answer}'
         totext+="\n".join(answerletter)
         totext+='\n'

         #print(totext)
         break
     else :
         #print(answer,answerletter)
         print('Input Correct answer')   
with open('artur_gyul.txt','w+') as rd:
        rd.write(totext)