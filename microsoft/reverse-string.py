# Prompt : "Given an input string, reverse the string word by word."
# input == str
# strings == immutable
# GOAL is to return reversed string by word 
# ex: "Hello World"  => "World Hello" 

def reverseString(word):
    reversedStr = ""
    wordList = word.split(" ")
    listLen = len(wordList)
    for idx in range(listLen):
        if idx == listLen - 1:
            reversedStr += wordList.pop()
        else:
            reversedStr += wordList.pop() + " "
        
    return reversedStr
    
        
    # temp = ""

    # for char in word:
    #     if char != " ":
    #         temp += char
    #     else:
    #         print(temp)
    #         if len(reversedStr) == 0:
    #             reversedStr += temp
    #         else:
    #             reversedStr = temp + " " + reversedStr

    #         temp = ""

    # if len(temp) > 0:
    #     reversedStr = temp + " " + reversedStr

    # print(reversedStr)

print(reverseString("Hello World It's me"))