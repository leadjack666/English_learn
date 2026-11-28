import random
#以下为从txt中把单词和中文抓出来的函数
def load_words(path):
    result_list=[]
    try:
        with open(path,"r",encoding="utf-8") as f:
            
            for line in f:
                partss=line.strip().split()
                if len(partss)==2:
                    result_list.append(tuple(partss))
                else:
                    #只打印防止一行错影响全部读取
                    print(f"跳过格式错误行:{line.strip()}")
    except FileNotFoundError:
        print("文件不存在")
    return result_list

#以下为从words里随机选取n个词的函数
def pick(words,n):
    if len(words)<=n:
            return words[:]    #返回副本，避免调用方改动污染原列表
    return random.sample(words,n)