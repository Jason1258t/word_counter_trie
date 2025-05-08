from stats import *

def read_text(text: str):
    text = text.strip()
    for x in '.,!?—':
        text = text.replace(x, '')
    return text.split()

test_text = """Надеюсь теперь твоя проверка будет более точной и ты найдешь все возможные баги в его работе
если что-то сломается или посчитается неправильно дай знать — будем разбираться вместе
кстати вот еще парочка строк для увеличения объема текста вдруг твоему счетчику нужно больше данных для анализа"""

stats = WordStatistics()
for w in read_text(test_text):
    stats.push_word(w)
print(stats.get_stats())