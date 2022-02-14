import os


def stat(name_folder: str):
    base_dir = os.path.abspath(name_folder)
    size_10 = []
    size_100 = []
    size_1000 = []
    size_10000 = []
    size_over_10000 = []
    size_10_mode = set()
    size_100_mode = set()
    size_1000_mode = set()
    size_10000_mode = set()
    size_over_10000_mode = set()
    result = {}
    for path, folders, files in os.walk(base_dir):
        for file in files:
            if os.stat(path).st_size <= 10:
                size_10.append(file)
                size_10_mode.add(os.path.splitext(file)[1])
            elif os.stat(path).st_size > 10 and os.stat(path).st_size <= 100:
                size_100.append(file)
                size_100_mode.add(os.path.splitext(file)[1])
            elif os.stat(path).st_size > 100 and os.stat(path).st_size <= 1000:
                size_1000.append(file)
                size_1000_mode.add(os.path.splitext(file)[1])
            elif os.stat(path).st_size > 1000 and os.stat(path).st_size <= 10000:
                size_10000.append(file)
                size_10000_mode.add(os.path.splitext(file)[1])
            else:
                size_over_10000.append(file)
                size_over_10000_mode.add(os.stat(path).st_mode)
    result.update({10: (len(size_10), list(size_10_mode))})
    result.update({100: (len(size_100), list(size_100_mode))})
    result.update({1000: (len(size_1000), list(size_1000_mode))})
    result.update({10000: (len(size_10000), list(size_10000_mode))})
    result.update({'over10000': (len(size_over_10000), list(size_over_10000_mode))})
    with open(f'{name_folder}_sumary.json', 'w', encoding='utf-8') as f:
        print(result, file=f)


if __name__ == '__main__':
    stat('my_project')