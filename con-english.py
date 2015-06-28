#!/usr/bin/env python3
import random
import os

dic = []
#for str in open(os.path.dirname(__file__) + '/db/dic.txt'):
for str in open('db/dic.txt'):
  line = str.split('#')
  if len(line) == 2:
    dic.append([line[0].strip(), line[1].strip()])

counts = len(dic)
print ('{0}\nCount of questions: {1}\n{0}'.format('-' * 80, counts))
i = 0
err = 0
answer = ''

while answer != 'end':
  num = random.randint(0, counts)
  answer = input('{0} ({1})\nTranslate - '.format(dic[num][0], num))
  if answer != 'end':
    i += 1
    if answer.lower() == dic[num][1].lower():
      print ('  +')
    else:
      err += 1
      print ('  -  Error. - {0}'.format(dic[num][1]))

print ('{0}\nResult:\nAnswer: {1}\nErrors: {2}\n{0}'.format('-' * 80, i, err))
