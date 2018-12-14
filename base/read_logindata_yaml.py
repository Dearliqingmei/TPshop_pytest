import os
import yaml


class Readlogindatayaml():

    def __init__(self,filename):
        self.path=os.getcwd()+os.sep+"data"+os.sep+filename

    def read_logindata_yaml(self):
        with open(self.path,"r",encoding="utf-8")as f:
            data_read=yaml.load(f)
            return data_read