import re
word="Simple regular expression example"
result=re.findall("ex",word)#it find how many times word in present
print(result)

space=re.search('\s',word)
print("\n The first space is at:",space.start())
