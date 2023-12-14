a = open('file1.txt', 'r', encoding='UTF-8')
b = open('file2.txt', 'r', encoding='UTF-8')

for i in a:
    if i not in b:
        print(i)
