import sys
import linecache
if len(sys.argv) > 2:
    for elem in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
        result = linecache.getline('bakery.csv', elem)
        result = result.strip()
        print(result)
elif len(sys.argv) > 1:
    result = linecache.getline('bakery.csv', int(sys.argv[1]))
    result = result.strip()
    print(result)
else:
    with open('bakery.csv', 'r', encoding='utf-8') as fr:
        file_list = fr.readlines()
        for line in file_list:
            line = line.strip()
            print(line)