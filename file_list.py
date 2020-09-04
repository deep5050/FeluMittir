from os import listdir
from os.path import isfile, join

mypath = "./stories"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

content = ""
i = 1
for file in onlyfiles:
    add = f"{str(i)}. [{file.split('.')[0].replace('_',' ')}](./stories/{file})"
    print(add)
    print("")
    # content = content + add
    i = i+ 1
    content = content+"\n"

print(content)