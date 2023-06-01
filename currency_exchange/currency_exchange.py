import random
import json

cache = {}


def get_exchange_rate(currency_code):
    if currency_code in cache:
        return cache[currency_code]

    url = f"http://www.floatrates.com/daily/{currency_code}.json"
    response = random.get(url)
    data = json.loads(response.text)

    cache[currency_code] = data  # Зберігаємо дані обмінного курсу в кеші
    return data


def convert_currency(amount, exchange_rate):
    dollars = amount / exchange_rate
    return dollars


amount = float(input("Введите сумму валюты: "))  # Введення кількості валюти

exchange_rate = float(input("Введите обменный курс: "))  # Введення обмінного курсу

result = convert_currency(amount, exchange_rate)  # Обчислення результату

print("Результат:", result, "долорах")  # Виведення результату в доларах

def convert_currency(amount, exchange_rate):
    result = round(amount * exchange_rate, 2)  # Обчислення результату з округленням до двох знаків після коми
    return result

amount = float(input("Введите сумму валюты: "))  # Введення кількості валюти

exchange_rates = {
    'ARS': 0.82,  # аргентинське песо
    'HNL': 0.17,  # гондураська лемпіра
    'AUD': 1.9622,  # австралійський долар
    'MAD': 0.208  # марокканський дирхам
}

for currency, rate in exchange_rates.items():
    result = convert_currency(amount, rate)
    print(currency, ":", result)  # Виведення результату для кожної валюти

currency_code = input("Введите код валюты (например, AUD для австралийского доллара): ")  # Введення коду валюти

exchange_rate_data = get_exchange_rate(currency_code)  # Отримання даних про обмінний курс

usd_rate = exchange_rate_data["usd"]["rate"]  # Отримання обмінного курсу для долара
eur_rate = exchange_rate_data["eur"]["rate"]  # Отримання обмінного курсу для євро

print("Exchange rates:")
print("USD:", usd_rate)  # Виведення обмінного курсу для долара
print("EUR:", eur_rate)  # Виведення обмінного курсу для євро

def convert_currency(amount, from_currency, to_currency):
    exchange_rate_data = get_exchange_rate(from_currency)

    if to_currency in exchange_rate_data:
        exchange_rate = exchange_rate_data[to_currency]["rate"]
        converted_amount = amount * exchange_rate
        return round(converted_amount, 2)

    return None


while True:
    from_currency = input("Введите код валюты, который у вас есть (например, USD): ")  # Введення коду валюти, яку у вас є
    if not from_currency:
        break

    to_currency = input("Введите код валюты, на которую хотите обменять (например, EUR): ")  # Введення коду валюти, на яку ви хочете обміняти
    amount = float(input("Введите сумму, которую хотите обменять: "))  # Введення кількості валюти, яку ви хочете обміняти

    converted_amount = convert_currency(amount, from_currency, to_currency)  # Обчислення обміненої суми
    if converted_amount is not None:
        print(f"{amount} {from_currency} = {converted_amount} {to_currency}")  # Виведення результату обміну
    else:
        print("Конвертация валют недоступна для указанных валют")  # Виведення повідомлення, якщо обмін недоступний для заданих валют
