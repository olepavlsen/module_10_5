import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name) as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]
# time_sart = datetime.now()
# for name in filenames:
#     read_info(name)
# time_end = datetime.now()
# print(f'', time_end - time_sart, 'линейный')

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        time_sart = datetime.now()
        pool.map(read_info, filenames)
        time_end = datetime.now()
        print(f'', time_end - time_sart, 'многопроцессный')
