import random

def load_words(path):
    with open(path,"r",encoding="utf-8") as f:
        result_list=[]
        for line in f:
            partss=line.strip().split()
            if len(partss)==2:
                result_list.append(tuple(partss))
            else:
                print(f"跳过格式错误行:{line.strip()}")
    return result_list


def pick(words,n):
    if len(words)<=n:
            return words
    return random.sample(words,n)