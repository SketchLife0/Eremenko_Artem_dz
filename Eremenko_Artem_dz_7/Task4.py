import os


def project_statistics(name_folder: str) -> dict:
    base_dir = os.path.abspath(name_folder)
    size_10 = []
    size_100 = []
    size_1000 = []
    size_10000 = []
    size_over_10000 = []
    result = {}
    for path, folders, files in os.walk(base_dir):
        for file in files:
            if os.stat(path).st_size <= 10:
                size_10.append(file)
            elif os.stat(path).st_size > 10 and os.stat(path).st_size <= 100:
                size_100.append(file)
            elif os.stat(path).st_size > 100 and os.stat(path).st_size <= 1000:
                size_1000.append(file)
            elif os.stat(path).st_size > 1000 and os.stat(path).st_size <= 10000:
                size_10000.append(file)
            else:
                size_over_10000.append(file)
    result.update({10: len(size_10)})
    result.update({100: len(size_100)})
    result.update({1000: len(size_1000)})
    result.update({10000: len(size_10000)})
    result.update({'over10000': len(size_over_10000)})
    return result


if __name__ == '__main__':
    print(project_statistics('my_project'))
