
# ! class work
сon = {'pi': 3.14, 'e': 2.71,'root 2': 1.14 }
print(сon)


result = {'pass': 0, 'fail': 0}
result['withdrawl'] = 1 
result['pass'] = 3
result['fail'] = result['fail'] + 1

print(result['fail'])

print(result['pass'])

print(result['withdrawl'])

c = {'pi': 2.14, 'e': 1.14, 'root 2': 225}
for k in c:
    print(c[k], end=' ')

c = {'pi': 1, 'e': 2, 'root 2': 3,  'fuck': 12}
total = 0 
for v in c.values():
    total= total + 1
print(total)