
# text = open("data.txt",  'r', encoding='utf-8')
# text.write("hello\n")

# text.close()
# data = text.read()
# data2 = text.readline()
# print(data)

# print(text.readline(5))
# text.seek(2)
# print(text.readline(3))
# print(text.tell())
# print(text.readline())

# print(text.readlines())


# words = []
# for word in text:
#     words.append(word.strip())
# print(words)


md = open('modified_data.txt', 'w', encoding='utf-8')

data = open('data.txt', 'r', encoding='utf-8')
i = 1
for line in data:
    md.write(f'{i}. {line}')
    i += 1

