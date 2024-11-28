#check50 cs50/problems/2022/python/extensions
submit50 cs50/problems/2022/python/extensions
file_name = input("File Name: ").lower()
extensions = [".gif",".jpg",".jpeg",".png",".pdf",".txt",".zip"]

for extension in extensions:
    if file_name.endswith(extension):

        if extension in [".gif", ".jpg", ".jpeg", ".png"]:
            print("image/"+extension)
        elif extension in ["pdf", "txt", "zip"]:
            print("document/"+extension)
else:
    print("non")
