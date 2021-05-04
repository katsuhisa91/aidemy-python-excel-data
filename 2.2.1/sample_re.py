import re

sample_text = '株式会社アイデミー'
sample_text2 = 'アイデミー株式会社'

word = re.findall('^株式会社.*', sample_text)
print(word)

word = re.findall('^株式会社.*', sample_text2)
print(word)
