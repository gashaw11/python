
#submit50 cs50/problems/2022/python/grocery
#using get,sorted methods for {}[]respectively


grocery = {}

while True:

    try:
        item = input().strip().upper()
        grocery[item]=grocery.get(item,0)+1
        
    except EOFError:
        break

for item in sorted(grocery):
    print(grocery[item],item)
