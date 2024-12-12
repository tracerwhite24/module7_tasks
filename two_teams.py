# Переменные для команд
team1_num = 5  # Количество участников команды Мастера кода
team2_num = 6  # Количество участников команды Волшебники данных

# Переменные для результатов соревнования
score_1 = 40  # Количество задач, решенных командой Мастера кода
score_2 = 42  # Количество задач, решенных командой Волшебники данных
team1_time = 18015.2  # Время, за которое команда Мастера кода решила задачи
team2_time = 20000.0   # Время, за которое команда Волшебники данных решила задачи

print("В команде Мастера кода участников: %d !" % team1_num)

print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num))

print("Команда Волшебники данных решила задач: {} !".format(score_2))

print("Волшебники данных решили задачи за {:.1f} с !".format(team2_time))

print(f"Команды решили {score_1} и {score_2} задач.")

if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = "Победа команды Мастера кода!"
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = "Победа команды Волшебники Данных!"
else:
    challenge_result = "Ничья!"

print(f"Результат битвы: {challenge_result}")

tasks_total = score_1 + score_2  # Общее количество задач
time_avg = (team1_time + team2_time) / 2  # Среднее время решения

print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!")