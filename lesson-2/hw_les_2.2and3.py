test_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in range(len(test_list)):
    try:
        is_num = int(test_list[i])
        if test_list[i].isdigit():
            print(f'"{is_num:02}"', end=' ')
        else:
            split_degree = test_list[i]
            split_degree = str(split_degree)
            split_degree = list(split_degree)
            sing = split_degree[0]
            num_degree = ''.join(split_degree[1:])
            num_degree = int(num_degree)
            print(f'"{sing}{num_degree:02}"', end=' ')
    except ValueError:
        print(test_list[i], end=' ')
