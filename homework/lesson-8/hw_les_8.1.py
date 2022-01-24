import re


def email_parse(mail):
    if not re.findall(r'[~!#$%^?&*,(){}><"№:`\[\]\\А-яёЁ]', mail):
        patern = re.compile(r'(?P<username>.+)[@](?P<domain>\w+\.\w+)')
        result = patern.finditer(mail)
        for el in result:
            return el.groupdict()
    else:
        msg = f'ValueError: wrong email: {mail}'
        raise ValueError(msg)


print(email_parse('as12929fa@kandfkj.com'))
