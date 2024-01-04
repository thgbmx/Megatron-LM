import os
from pandas.io import json
from tqdm import tqdm

def txtToJson(path):
    filename = os.listdir(path) #获取path路径下的所有文件的名字(eg:123.txt)
    # filename=filename[:2]
    # print(len(filename),filename)
    filejson=dict()
    for fn in tqdm(filename):
        p=os.path.join(path,fn)
        # print(fn," ;", p)
        try:
            # 大多数文件都是utf-8格式的，少数文件是gbk格式，默认使用utf-8格式读取，为了防止gbk文件使程序中断,使用 try catch 处理特殊情况
            f = open(p,mode="r",encoding="utf-8")
            savefile_name = "workspace/code/scraped/data_json/"+fn.rstrip(".txt")+".json"
            file_out = open(savefile_name, 'w', encoding='utf-8')
            for item in f:
                filejson["text"]=item
                file_out.write(json.dumps(filejson, ensure_ascii=False)+"\n")
                #print(item)
            # data=f.read().replace(" ","").replace("\n","")
            # filejson[fn.rstrip(".txt")]=data
            f.close()
        except Exception:
            f = open(p, mode="r", encoding="gbk")
            data=f.read().replace(" ","").replace("\n","")
            filejson[fn]=data
            f.close()
    return filejson,len(filejson)

def saveInJsonFile(data,path):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(filejson, ensure_ascii=False))

# 要读取的文件夹路径
readpath=r"workspace/code/scraped/data"
filejson,length=txtToJson(readpath)
# print(filejson)

#保存的文件路径 1.json可以更换成其他的名字
# save_path=r"1.json"
#saveInJsonFile(filejson, save_path)
