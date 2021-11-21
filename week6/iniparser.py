import os
import pprint


class INIParser:
    def __init__(self):
        self.inppath = os.getcwd()
        self.fullpath = f'{self.inppath}/application.ini'
        self.fulldata = ""

    def fullparser(self):

        if os.path.isfile(self.fullpath):
            pass
        else:
            print('input val path.')
            exit()
        filelog = open(self.fullpath, "r")
        for line in filelog:
            self.fulldata += f'{line}\n'
        return self.fulldata


class MainParser(INIParser):
    def __init__(self):
        self.l = ""
        self.dat = 'tests'
        self.inppath = os.getcwd()
        self.fullpath = f'{self.inppath}/application.ini'
        self.fulldata = ""
        self.is_dictcontaining = False

      # ,str(self.iniparse())

    def __repr__(self):
        data = self.fullparser()
        return data

    def __getitem__(self, *i):
        self.l = i
        if isinstance(self.l[0], tuple):

            self.is_dictcontaining = True
        self.dat = self.iniparse()
        return self.dat

    def iniparse(self):
        dictcont={}
        if self.is_dictcontaining:
            section = f'[{self.l[0][0]}]'
        else:
            section = f'[{self.l[0]}]'

        propperty = self.l[0][1]
        is_section = 0
        if os.path.isfile(self.fullpath):
            pass
        else:
            print('input val path.')
            exit()
        filelog = open(self.fullpath, "r")
        for line in enumerate(filelog):

            if section in line[1] and not is_section:
                is_section = 1
                continue
            if line[1].strip().startswith('[') and line[1].strip().endswith(']')and is_section:
                break
            elif propperty in line[1] and is_section and self.is_dictcontaining:
                self.dat = line[1].split()[-1]
                return self.dat
            elif is_section and not self.is_dictcontaining and len(line[1].strip())>1:
                dictcont[line[1].split()[0]] = line[1].split('=')[-1].strip()

        return dictcont


a = MainParser()

print(a['test'])
print(a['test','debug'])


#pprint.pprint(a)
# print(a['test']['1'])
