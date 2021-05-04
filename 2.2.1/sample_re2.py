import re

with open('sample.txt', 'r', encoding='UTF-8') as f:
    word = re.findall('^株式会社.*', f.read())
    print(word)
