import requests
# Реализовать получение курсов по API
def get_rates_from_api():
    result = requests.get('https://www.cbr-xml-daily.ru/latest.js').json().setdefault('rates')
    return result
    
 #Добавить RUB ключ со значением ???

EXCHANGE_RATES = get_rates_from_api()


base_currency = 'BTC'

for i in EXCHANGE_RATES:
    print(i)
    if i != base_currency:
        return 'Ошибка'
    else:
        return 'Ок'



    
