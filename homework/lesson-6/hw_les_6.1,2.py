with open('nginx_logs.txt', encoding='utf-8') as file:
    count_dict = {}
    for line in file:
        line = file.readline()
        remote_addr = line.split(' ')[0]
        text = line.split('"')[1]       # Для первой задачи
        request_type = text.split(' ')[0]       # Для первой задачи
        requested_resource = text.split(' ')[1]         # Для первой задачи
        answer = [remote_addr, request_type, requested_resource]  # Для первой задачи
        if remote_addr in count_dict:
            count_dict[remote_addr] += 1
        else:
            count_dict[remote_addr] = 1
        # print(tuple(answer))   # Для первой задачи
    spam_ip = max(count_dict, key=count_dict.get)
    print(spam_ip, count_dict.setdefault(spam_ip))
