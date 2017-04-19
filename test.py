depend = open("file.txt", "w")

f=21212151.36582
g=21212151.36582
print(file=depend,'%.2f %.2f' % (f, g),"test")
print('%.2f %.2f' % (f, g),"test", file=depend)