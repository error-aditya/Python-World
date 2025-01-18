# file i/o opearations


f = open('java_info.txt','r+')
data = f.read()
print(data,type(data))
f.close()