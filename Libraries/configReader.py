import configparser

def readConfigData(section, key):
    config = configparser.ConfigParser()
    config.read("./ConfigurationFiles/Config.cfg")
    return config.get(section, key)

def readElementLocators(section, key):
    config = configparser.ConfigParser()
    config.read("./ConfigurationFiles/Elements.cfg")
    return config.get(section, key)

def readData(section, key):
    config = configparser.ConfigParser()
    config.read("./ConfigurationFiles/Data.cfg")
    return config.get(section, key)
