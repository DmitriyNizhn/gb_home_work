from requests import get
from re import findall


def currency_rates(valute):
    valute = valute.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    date = str(findall(r'\d{2}.\d{2}.\d{4}', content)[0])
    for el in content.split(f'{valute}</CharCode><Nominal>')[0:]:
        text = el.split('</Value>')[0]
        nominal = text.split('<')[0]
        value = text.split('>')[-1]
    if nominal == '':
        return 'None'
    else:
        nominal = float(nominal)
        value = float(value.replace(',', '.'))
        value = value / nominal
        return value, date


if __name__ == '__main__':
    print(currency_rates('usd'))
