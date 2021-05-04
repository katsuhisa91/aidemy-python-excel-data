with open('sample.csv', 'r', newline='') as f:
    replaced_text = f.read().replace('株式会社', '')
    print(replaced_text)
