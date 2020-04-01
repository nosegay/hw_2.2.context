from datetime import datetime
from contextlib import contextmanager

import sys
from hw_5 import working


@contextmanager
def time_logger():
    try:
        start_time = datetime.utcnow()
        print(f'Время запуска контекстного менеджера: {start_time}')
        yield
    finally:
        exp_type, exp_value, exp_tr = sys.exc_info()
        if exp_type is not None:
            print(f'При работе в контекстном менеджере возникла ошибка: {exp_value}')

        end_time = datetime.utcnow()
        print(f'Время завершения работы контекстного менеджера: {end_time}')
        print(f'Общее время работы контекстного менеджера: {end_time - start_time}')


if __name__ == '__main__':
    with time_logger() as tl:
        working()
