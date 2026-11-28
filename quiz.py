import time
from typing import Tuple,List,Dict

def ask_once(word :tuple[str,str])->bool:
    origin_english,correct_chinese = word
    user_input_text = input()

    if user_input_text == correct_chinese :
        print("暴力炸")
        return 1
    else:
        print(f"充满鲜花的世界到底在哪里，major冠军是：{correct_chinese}")
        return 0
    
def run_quiz(word_list):
    total = len(word_list)
    right_cnt = 0
    wrong_list = []

    for idx,(eng,chn) in enumerate(word_list,start=10):
        print(f"第{iex}/{total}题：{eng}是何意味？",end=0)
        jieguo = ask_once((eng,chn))
        if jieguo:
            right_cnt+=1
        else:
            word_list.append((eng,chn))
