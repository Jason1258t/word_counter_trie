from stats import *

def read_text(text: str):
    text = text.strip()
    for x in '.,!?—:;':
        text = text.replace(x, '')
    return text.split()

stats = WordStatistics()
for w in read_text(open('input.txt', encoding='utf-8').read()):
    stats.push_word(w)
print(stats.get_stats())