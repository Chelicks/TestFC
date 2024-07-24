import phonenumbers
import pandas as pd
from collections import Counter

def verify_number(number, call_int):
    n = phonenumbers.parse("+" + str(number))
    v = phonenumbers.is_possible_number(n)

    if call_int > 1 or not v:
        spam_numbers.append(number)
        return None

def extract_substring(phone_number):
    return str(phone_number)[4:10]


def analyze_patterns(phone_numbers):
    substrings = []

    for number in phone_numbers:
        substring = extract_substring(number)
        if substring:
            substrings.append(substring)

    # Анализ частоты подстрок
    substring_counts = Counter(substrings)
    # Вывод самых частых подстрок
    substrings = substring_counts.most_common()

    return substrings






df = pd.read_csv("Flash call.csv", sep=";")
spam_numbers = []

#Обход строк DataFrame и проверка номеров
for i in range(len(df)):
    info_from_row = df.loc[i]
    number, call_int = info_from_row
    verify_number(number, call_int)

# Создание копии DataFrame без спам-номеров
df_copy = df.copy()
df_copy = df_copy[~df_copy.iloc[:, 0].isin(spam_numbers)]

# Анализ паттернов на основе очищенного DataFrame
clean_numbers = df_copy.iloc[:, 0].tolist()
substrings = analyze_patterns(clean_numbers)


# Вывод результатов анализа и очищенного DataFrame
print(f"Подстроки: {substrings}")
print(df_copy)