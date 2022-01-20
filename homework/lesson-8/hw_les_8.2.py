import re

with open('nginx_logs.txt', encoding='utf-8') as f:
    lines = f.read().splitlines()
    for raw in lines:
        result = []
        remote_addr = re.findall(r'(?P<addr>^.+\b) - -', raw)
        result.append(remote_addr[0])
        request_datetime = re.findall(r'(\w+/\w+/\d{4}:\d{2}:\d{2}:\d{2}\s\+\d{4})', raw)
        result.append(request_datetime[0])
        request_type = re.findall(r']\s"(?P<r_type>\w{3,4})\s', raw)
        result.append(request_type[0])
        requested_resource = re.findall(r'(?P<resource>/\w+/\w+_\d)', raw)
        result.append(requested_resource[0])
        response_code = re.findall(r'" (?P<code>\d+)\s', raw)
        result.append(response_code[0])
        response_size = re.findall(r'\d+\s(?P<size>\d+)\s', raw)
        result.append(response_size[0])
        print(tuple(result))
