import speech_recognition, random, time
from voice import speach



selected_level = input('Веберите уровень сложности (easy/medium/hard)').lower()

levels = {

    "easy": ["dairy", "mouse", "computer"],

    "medium": ["programming", "algorithm", "developer"],

    "hard": ["neural network", "machine learning", "artificial intelligence"]
}

def play_game(level):
    score = 0
    words = levels.get(level,[])
    if not words:
        print('Не верный уровень сложности ')
        return

    for i in range(len(words)):
        random_word = random.choice(words)
        print(f'Скажите слово {random_word}')
        record_word = speach()

    if random_word == record_word():
        print('Верно')
        score += 1

    else:
        print('Не верно')

    time.sleep(2)

    print(f'Игра завершена! Ваш счет: {score}/{len(words)}')

play_game(selected_level)
