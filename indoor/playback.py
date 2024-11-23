#add three dots to the end of each word from an input
#using slpit and join string methods
playback = input()


def main():
    words = playback.split()
    print('...'.join(words))
 
if __name__ == "__main__":
    main()




# playbackoutput='...'.join([i + '...' for i in playbackinput.split()])
# print(playbackoutput)
