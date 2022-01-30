import re


class Date:
    def __init__(self, inp_date):
        Date.val(inp_date)
        self.date = inp_date

    @staticmethod
    def val(date):
        if re.fullmatch('\d{2}-\d{2}-\d{4}', date):
            pass
        else:
            raise 'Формат не соответствует, введите в соответствии с дд-мм-гггг'

    @classmethod
    def date_to_int(cls, date):
        a = date.split('-')
        result = []
        for el in a:
            result.append(int(el))
        return result


f_date = Date('01-04-1994')
print(f_date.date_to_int('01-04-1994'))
print(Date.date_to_int('01-03-1994'))
