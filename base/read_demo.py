import yaml


data_list=list()
with open("../data/data_login.yaml","r",encoding="utf-8")as f:
    data_read=yaml.load(f)
    print(data_read)