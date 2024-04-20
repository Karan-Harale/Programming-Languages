def freq(str,check):
    str_list=str.split()
    unique_words=set(str_list)

    for words in unique_words:
        if(str_list.count(words)>=check):
            print(words , end=" ")

str=input()
check=int(input())
freq(str,check)