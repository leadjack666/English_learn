import mistakes
import quiz
import words

print("你现在是做题区（家中无富贵，口袋无财宝） 在前往成王之路")
kskbl = input("请按回车键继续")
if kskbl != "":
    print("一直烦，串不串？")
    exit(1)

print("你已成功加入异地籍，通关整个单词表还是指定个数？")
mistakess = list(dict.fromkeys(words.load_words("mistake.txt")))
length_mistakes=len(mistakess)
st_m = input("输入1为通关整个单词表，输入2为指定个数：")
if st_m == "1":
    word_list = words.load_words("words.txt")
elif st_m == "2":
    num = int(input("请输入要抽取的单词数："))
    if num//2>=length_mistakes:
        word_list = words.pick(words.load_words("words.txt"), int(num-length_mistakes))
        word_list2 = words.load_words("mistake.txt")
        for item in word_list2:
            word_list.append(item)
    else:
        word_list = words.pick(words.load_words("words.txt"), int(num-num//2))
        word_list2 = words.pick(words.load_words("mistake.txt"), int(num//2))
        for item in word_list2:
            word_list.append(item)
            
score,wrong_list,correct_rate = quiz.run_quiz(word_list)
print(f"得分：{score}")
print(f"错误列表：{wrong_list}")
print(f"正确率：{correct_rate}")
mistakess = list(dict.fromkeys(mistakess + wrong_list))
mistakes.save_mistakes("mistake.txt",mistakess)
print("错题已记入 mistake.txt")