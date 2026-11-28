#以下为拉取txt文件读出单词英文和中文和保存错题的函数
def load_mistakes(path):
    result_list1=set()
    try:
        with open(path,"r",encoding="utf-8") as f1:
            for line1 in f1:
                parts=line1.strip()
                if parts:
                    result_list1.add(parts)
    except FileNotFoundError:
        pass
    return result_list1

def save_mistakes(path,wrong_words):
    with open(path,"w",encoding="utf-8") as f3:
        for partss in wrong_words:
            f3.write(partss+"\n")