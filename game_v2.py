"""
Игра угадай число
Компьютер сам загадывает и сам же угадывает
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно загадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count+=1
        predict_number = np.random.randint(1, 101) #предполагаемое число
        if number == predict_number:
            break #выходим из цикла если угадали
    return count

def score_game(random_predict) -> int:
    """За какое кол-во попыток угадывает наш алгоритм (в среднем 1000 подходов)

    Args:
        random_predict (_type_): Ф-ция угадывания

    Returns:
        int: Среднее кол-во попыток
    """
    count_ls = []
    np.random.seed(1) #фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) #задали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток.")
    return(score)

# #RUN
# score_game(random_predict)

#RUN
if __name__ == "main":
    score_game(random_predict)