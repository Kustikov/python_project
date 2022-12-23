import requests
# Реализовать получение курсов по API
def get_rates_from_api():
    result = requests.get('https://www.cbr-xml-daily.ru/latest.js').json().setdefault('rates')
    result['RUB'] = 1
    return result

EXCHANGE_RATES = get_rates_from_api()
print(EXCHANGE_RATES)
# В выгруженном API словаре нет RUB:1. Нужно ли добавить его туда вручную через  d[key] = value

# Приводим СЛОВАРЬ к строке для отображения списка валют без скобок, удаляем пробелы по краям.
def rates_for_input():  
    dict_a = EXCHANGE_RATES
    result = ''
    for key in dict_a:
        result += f' {key}'    
    return result.strip()
    
def main():
    exchange_rates = get_rates_from_api()
    main_currency = exchange_rates['RUB']
    print(main_currency)
    rates_input = rates_for_input()
    base_currency = input(f'Введите валюту, которую хотите обменять =>\n{rates_input}\n')
    base_currency = base_currency.upper() #приводим к UPPER если пользователь ввел не тот регистр
    check_key = base_currency in EXCHANGE_RATES.keys()
    print(check_key)
    if check_key:
            'Валюта верна'
    else:
        print(f'Введена несуществующая валюта')
    # Исправить отображение списка валют
    # Проверять, действительную ли валюту ввел пользователь и отрицательные значения
    # Обрезать лишние пробелы при вводе, проверять регистр ввода
    target_currency = input(f'Введите валюту, на которую хотите обменять =>\n{rates_input}\n')
    target_currency = target_currency.upper() #приводим к UPPER если пользователь ввел не тот регистр
    # Исправить отображение списка валют
    # Проверять, действительную ли валюту ввел пользователь и отрицательные значения
    # Обрезать лишние пробелы при вводе, проверять регистр ввода
    currency_amount = float(input('Введите количество валюты\n'))
    #Если одна из выбранных валют: рубль (как основная)
    if base_currency == 'RUB':
    	cross_course = exchange_rates[base_currency] * exchange_rates[target_currency]
    elif target_currency == 'RUB':
         cross_course = (exchange_rates[target_currency] / exchange_rates[base_currency])
    else:
    	cross_course = exchange_rates[base_currency] / exchange_rates[target_currency]
    result = round(cross_course * currency_amount, 2)
    print(f'Вы получите = {result} {target_currency}')  # добавить валюту в вывод  - done


main()

