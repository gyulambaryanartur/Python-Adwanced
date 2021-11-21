import configparser
import urllib.request
import json
import string


class Quiz:
    def __init__(self, configfile, filename):
        self.letters = string.ascii_uppercase
        self.questioairstr = ""
        self.configfile = configfile
        self.filename = filename

    def jsonparser(self) -> dict:
        config = configparser.ConfigParser()
        config.read(self.configfile)
        # print(config.sections())
        url = config['quiz']['url']
        print(url)
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        return data

    def jsontostring(self) -> str:
        data = self.jsonparser()
        for number, i in enumerate(data['questions'], 1):
            question = f'{number}). {i["question"]}\n'
            self.questioairstr += f'{question}'
            print(question)
            answerletter = []
            answerlist=[]

            for let, text in zip(self.letters, i['answers']):

                print(f' { let})', text)
                answerletter.append(f'{let}) {text}')
                answerlist.append(let)

    # print(answerletter)
            while True:
                answer = input("Input answer option:")
                #answertext = f'{answer}){text}'

                print(answer,answerletter)

                if answer in answerlist:
                    getind = answerlist.index(answer)
                    answerletter[getind] = f'*{answer}){text}'
                    self.questioairstr += "\n".join(answerletter)
                    self.questioairstr += '\n'

                    # print(questioairstr)
                    break
                else:
                    # print(answer,answerletter)
                    print('Input Correct answer')

        return self.questioairstr

    def writetofile(self):
        data = self.jsontostring()
        with open(self.filename, 'w+') as rd:
            rd.write(data)


if __name__ == "__main__":
    test = Quiz('config.ini', 'Artur_Gyulambaryan')
    # To print given anserws
    # print(test.jsontostring())
    # To write into a File
    test.writetofile()
