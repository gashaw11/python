#submit50 cs50/problems/2022/python/twttr
#using join and list comprehnssion



Input = input("Input: ")
Output = ''.join(c for c in Input if c not in "aeiouAEIOU")
print(Output)
