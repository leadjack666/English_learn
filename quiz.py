__all__ = ["run_quiz"] 

#用来判断单词是否写对，给run_quiz调用
def ask_once(word :tuple[str,str])->bool:
    origin_english,correct_chinese = word
    user_input_text = input("请作答：")

    if user_input_text == correct_chinese :
        print("暴力炸")
        return True
    else:
        print(f"充满鲜花的世界到底在哪里，major冠军是：{correct_chinese}")
        return False

#传进单词表，问答的核心程序，依次返回正确数，错题表和准确率 
def run_quiz(word_list)-> tuple[int, list[tuple[str, str]], float]:
    """依次提问，返回 (正确数, 错题表, 准确率)。"""
    total = len(word_list)
    if total==0 :
        raise ValueError("word_list不能为空")
    right_cnt = 0
    wrong_list = []

    for idx,(eng,chn) in enumerate(word_list,start=1):
        print(f"第{idx}/{total}题：{eng}是何意味？",end="")
        jieguo = ask_once((eng,chn))
        if jieguo:
            right_cnt+=1
        else:
            wrong_list.append((eng,chn))

    return right_cnt,wrong_list,right_cnt/total

if  __name__=="__main__" :
    demo = [("apple", "苹果"), ("banana", "香蕉")]
    print(run_quiz(demo))