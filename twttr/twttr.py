#submit50 cs50/problems/2022/python/twttr

def main():

    user_input = input("Input: ")
    output = shorten(user_input)
    print(f"Output: {output}")



def shorten(user_input):
    output = ''.join(c for c in user_input if c not in "aeiouAEIOU")
    return output


if ___name__=="__main__":
    main()
