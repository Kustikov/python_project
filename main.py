import requests
# Реализовать получение курсов по API
def get_rates_from_api():
    result = requests.get('https://www.cbr-xml-daily.ru/latest.js').json().setdefault('rates')
    return result
    
 #Добавить RUB ключ со значением ???

EXCHANGE_RATES = get_rates_from_api()

# Приводим СЛОВАРЬ к строке (исправляем отображение списка валют), удаляем пробелы.
def rates_for_input():  
    dict_a = EXCHANGE_RATES
    result = ''
    
    for key in dict_a:
        result += f' {key}'
        
    return result.strip()
    
def main():
    exchange_rates = get_rates_from_api()
    rates_input = rates_for_input()
    base_currency = input(f'Введите валюту, которую хотите обменять =>\n{rates_input}\n')
    base_currency = base_currency.upper()
    # Исправить отображение списка валют
    # Проверять, действительную ли валюту ввел пользователь и отрицательные значения
    # Обрезать лишние пробелы при вводе, проверять регистр ввода
    target_currency = input(f'Введите валюту, на которую хотите обменять =>\n{rates_input}\n')
    target_currency = target_currency.upper()
    # Исправить отображение списка валют
    # Проверять, действительную ли валюту ввел пользователь и отрицательные значения
    # Обрезать лишние пробелы при вводе, проверять регистр ввода
    currency_amount = float(input('Введите количество валюты\n'))

    cross_course = exchange_rates[base_currency] / exchange_rates[target_currency]
    result = round(cross_course * currency_amount, 2)
    print(f'Вы получите = {result} {target_currency}')  # добавить валюту в вывод  - done


main()

