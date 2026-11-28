def save_mistakes(path,wrong_words):
    with open(path,"w",encoding="utf-8") as f:
        for eng,chn in wrong_words:
            f.write(f"{eng} {chn}\n")