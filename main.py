import mistakes
import quiz
import words

print("你现在是做题区（家中无富贵，口袋无财宝） 在前往成王之路")
kskbl = input("请按回车键继续")
if kskbl != "":
    print("一直烦，串不串？")
    exit(1)

print("你已成功加入异地籍，通关整个单词表还是指定个数？")
st_m = input("输入1为通关整个单词表，输入2为指定个数：")
if st_m == "1":
    word_list = words.load_words("words.txt")
elif st_m == "2":
    num = input("请输入要抽取的单词数：")
    word_list = words.pick(words.load_words("words.txt"), int(num))

score,wrong_list,correct_rate = quiz.run_quiz(word_list)
print(f"得分：{score}")
print(f"错误列表：{wrong_list}")
print(f"正确率：{correct_rate}")