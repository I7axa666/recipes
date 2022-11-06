files_dict = {}
with open('1.txt', 'rt', encoding="utf-8") as file:
    count = 0
    file_list = []
    for line in file:
        count += 1
        file_list.append(line)
    files_dict[count] = {'1.txt': file_list}


with open('2.txt', 'rt', encoding="utf-8") as file:
    count = 0
    file_list = []
    for line in file:
        count += 1
        file_list.append(line)
    files_dict[count] = {'2.txt': file_list}


with open('3.txt', 'rt', encoding="utf-8") as file:
    count = 0
    file_list = []
    for line in file:
        count += 1
        file_list.append(line)
    files_dict[count] = {'3.txt': file_list}

sort_files_dict = {k: v for k, v in sorted(files_dict.items(), key=lambda item: item[0])}


with open('Итоговый файл.txt', 'w', encoding="utf-8") as file:
    for docs, col in sort_files_dict.items():
        for x in col.keys():
            file.write(x + '\n')
        file.write(str(docs) + '\n')
        for lines in col.values():
            for tx in lines:
                file.write(tx)
        file.write('\n')