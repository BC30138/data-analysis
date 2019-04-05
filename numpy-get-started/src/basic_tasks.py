import numpy as np

class basic_tasks:
    def __init__(self):
        pass
        
    def task1(self):
        print(np.__version__)
        np.show_config()

    def task2(self):
        np.info(np.add)

    def task3(self):
        array = np.array([0,1,2,25])
        print(array)
        print('Check if each element of array is true (when element equals 0 - it\'s False)')
        print(np.all(array))
        array = np.array([1,1,2,25])
        print(array)
        print('Check if each element of array is true (when element equals 0 - it\'s False)')
        print(np.all(array))