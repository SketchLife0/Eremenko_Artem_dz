import time


class TrafficLight:
    __color: list = ['red', 'yellow', 'green']

    # В данной реализации что-то может сломаться только при условии что кто-то влезет в список своими кривыми руками и
    # изменит цвета поэтому и проверка порядка режимов не нужна. Режимы нарушены не будут
    def running(self):
        traffic_light_operation = True
        iteration = 0  # Ввод переменной для завершения работы согласно поставленной задачи
        while traffic_light_operation:
            for elem in self.__color:
                if elem == 'red':
                    sec_job = 4
                elif elem == 'yellow':
                    sec_job = 2
                elif elem == 'green':
                    sec_job = 3
                time.sleep(sec_job)
                print(f'{elem} {sec_job} cек')
            # если следующие строки заменить на проверку реального времени и останавливать работы в 20:30, а начинать в
            # 6:00, то будет прекрасный готовый светофор. Хоть сейчас устанавливай на улицу
            iteration += 1
            if iteration == 1:
                traffic_light_operation = False  #


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
