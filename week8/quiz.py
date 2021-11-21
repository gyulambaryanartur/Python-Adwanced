import configparser
config = configparser.ConfigParser()
config.read('config.ini')
print(config.sections())
#url=config['quiz']['url']
#print(url)