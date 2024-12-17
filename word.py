def match_word(words):
    c=0
    l=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            c=+1
            l.append(word)
    print("list of words with same char same/n",l)
    return c
count=match_word(['acb','dps','nps','esp','12221'])
print(count)
