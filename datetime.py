import datetime

# Текущая дата и время
now = datetime.datetime.now()
print("Сейчас:", now)  # Вывод: Сейчас: 2023-10-05 14:30:00.123456

# Текущая дата
today = datetime.date.today()
print("Сегодня:", today)  # Вывод: Сегодня: 2023-10-05

# Создание конкретной даты
custom_date = datetime.date(2023, 12, 31)
print("Кастомная дата:", custom_date)  # Вывод: Кастомная дата: 2023-12-31

# Создание конкретного времени
custom_time = datetime.time(14, 30, 45)
print("Кастомное время:", custom_time)  # Вывод: Кастомное время: 14:30:45

# Создание конкретной даты и времени
custom_datetime = datetime.datetime(2023, 12, 31, 23, 59, 59)
print("Кастомная дата и время:", custom_datetime)  # Вывод: Кастомная дата и время: 2023-12-31 23:59:59

# Разница между датами (timedelta)
future_date = custom_date + datetime.timedelta(days=10)
print("Дата через 10 дней:", future_date)  # Вывод: Дата через 10 дней: 2024-01-10

# Разница между двумя датами
date1 = datetime.date(2023, 1, 1)
date2 = datetime.date(2023, 12, 31)
difference = date2 - date1
print("Разница между датами:", difference.days, "дней")  # Вывод: Разница между датами: 364 дней

# Форматирование даты и времени
formatted_date = now.strftime("%d.%m.%Y %H:%M:%S")
print("Форматированная дата:", formatted_date)  # Вывод: Форматированная дата: 05.10.2023 14:30:00

# Парсинг строки в дату
date_string = "2023-10-05"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
print("Распарсенная дата:", parsed_date)  # Вывод: Распарсенная дата: 2023-10-05 00:00:00