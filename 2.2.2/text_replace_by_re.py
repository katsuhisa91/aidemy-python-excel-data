import re
text = '東京タワーと東京スカイツリー'
text_mod = re.sub('^東京', 'Tokyo', text)
print(text_mod)
