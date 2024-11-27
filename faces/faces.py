#this function converts file to emoji
def convert(str):
    str = str.replace(":(", "😊")
    str = str.replace(":)","😄")
    return str
def main():
    user_input = input("enter any text")
    converted = convert(user_input)
    print(converted)
if __name__=="__main__":
    main()
