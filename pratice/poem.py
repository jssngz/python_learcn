'''
前两天看到一道还蛮有意思的题目，今天就拿来挖坑吧：
把一段字符串用“右起竖排”的古文格式输出，并且拿竖线符号作为每一列的分割符。
比如这段文字：
"静夜思 李白床前明月光，疑似地上霜。举头望明月，低头思故乡。"
输出结果：
低┊举┊疑┊床┊静
头┊头┊似┊前┊夜
思┊望┊地┊明┊思
故┊明┊上┊月┊
乡┊月┊霜┊光┊李
。┊，┊。┊，┊白

'''
poem = ['静夜思 李白', '床前明月光，', '疑是地上霜。', '举头望明月，', '低头思故乡。']
poem.reverse()
for i in range(len(poem[0])):
    outstr = ''
    for j in range(len(poem)):
        outstr += poem[j][i] + '|'
    outstr = outstr[:-1]
    print(outstr)
