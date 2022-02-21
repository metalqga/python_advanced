# import os
#
# file=open("example.txt")
# file=open("inner/inner.txt")
# #file=open("../inner.txt") - edna dir nagore
# #file=open("../../inner.txt") - dve dir nagore
# print(file.readlines())
# absolute_path=os.path.abspath(__file__)
# file_path=os.path.join(absolute_path, "inner", "inner.txt")
# print(file_path)


import os
absolute_path=os.path.dirname(os.path.abspath(__file__))

file_path=os.path.join(absolute_path,"inner","inner.txt")
print(file_path)
file=open(file_path)
#print(file.readlines())
print(file.read(100))
file.close()