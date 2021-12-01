str = input("Enter The Story ")

str2 = str.split(' ')
# print(str)
print(str2)

prep = []
f1 = open('prep.txt', "r")
for x in f1:
    prep.append(x)
    
prep2 = ''
for i in prep:
    prep2 = prep2 + i

prep3 = prep2.split('\n')

print(prep3)

for x in prep3:
    if x in str2:
        count1 = str2.count(x)
        print(x, "is", count1)