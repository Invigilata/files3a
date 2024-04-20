team1_num = 5
team2_num = 6

str1 = "В команде Мастера кода участников: %d ! " % team1_num
str2 = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)

print(str1)
print(str2)

score_2 = 42
team1_time = 18015.2
team2_time = 20033.65

str3 = "\nКоманда Волшебники данных решила задач: {} !".format(score_2)
str4 = "Волшебники данных решили задачи за {} с !".format(team1_time)

print(str3)
print(str4)

score_1 = 40
score_2 = 42
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = "Победа команды Мастера кода!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = "Победа команды Волшебники Данных"
else:
    challenge_result = "Ничья!"

tasks_total = score_1 + score_2

time_avg = 350.4


str5 = f"\nКоманды решили {score_1} и {score_2} задач."
str6 = f"Результат битвы: {challenge_result}"
str7 = f"Сегодня было решенно {tasks_total} задач, в среднем по {time_avg} секунды на задачу!"

print(str5)
print(str6)
print(str7)
