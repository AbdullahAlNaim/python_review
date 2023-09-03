# f = open('test.txt', 'a')
# f.write('This was written within and by python')
# f.close()

# f = open('test.txt', 'r')
# print(f.read())

# s = open('made.txt', 'x')
# s = open('made.txt', 'a')
# s.write('hello there. this was created in python')
# s.close()
# s = open('made.txt', 'r')
# print(s.read())

names = ['one', 'two', 'three']

for x in range(len(names)):
    f = open(f'{names[x]}.txt', 'x') 
    f.close()

    f = open(f'{names[x]}.txt', 'a')
    f.write(f'This is file {names[x]}')
    f.close()

    f = open(f'{names[x]}.txt', 'r')
    print(f.read())


'''
1 - python servers?
2 - pdf generator
3 - sending emails?
4 - 
'''