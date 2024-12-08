submit50 cs50/problems/2022/python/emojize

from emoji import emojize

emoji = input("enter your emoji name: ")
output = emojize(emoji,language='alias')
print(output)
