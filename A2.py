from math import log as ln
from time import time
from time import sleep
from random import randint


class Node:
    def __init__(self, *args):
        self.update(*args)

    def update(self, *args):
        self._access()
        self.__value, self.__weight = args

    def _access(self):
        self.last_access_time = time()

    def get_value(self):
        self._access()
        return self.__value

    def get_weight(self):
        self._access()
        return self.__weight

    def cal_score(self, current_time):
        # self._access() # ?
        # current_time = time() # ?
        if current_time != self.last_access_time:
            return self.__weight/ln(current_time-self.last_access_time)
        else:
            return self.__weight/(-100)

    def __repr__(self):
        return f'[{self.__value},{self.__weight}]'


class Cache:
    def __init__(self, capacity=3):
        self.capacity, self.amt = capacity, 0
        self.dict = {}

    def get(self, key):
        if key in self.dict:
            return self.dict[key].get_value()
        return -1

    def put(self, key, value, weight):
        if not key or (not isinstance(weight, int) and not isinstance(weight, float)):
            raise TypeError
        if key in self.dict:
            self.dict[key].update(value, weight)
        elif self.amt < self.capacity:
            self.dict[key] = Node(value, weight)
            self.amt += 1
        else:
            current_time = time()  # ?
            for k, node in self.dict.items():
                min_s_key, min_score = k, node.cal_score(current_time)
                break
            for k, node in self.dict.items():
                s = node.cal_score(current_time)
                if s < min_score:
                    min_s_key, min_score = k, s
            self.dict.pop(min_s_key, None)
            self.dict[key] = Node(value, weight)

    def __str__(self):
        return str(self.dict)


def test(c):
    TK = 5  # key
    TW = 5  # weight
    TS = 0.1  # sleep
    PS, PG, PP = 1, 2, 3 # ratios

    def test_get():
        k = randint(1, TK) + 2
        print(f'get {k}: {c.get(k)}', '\n')

    def test_put():
        k, w = randint(1, TK), randint(1, TW)
        print(f'put {k}:[v{k},{w}]')
        c.put(k, f'v{k}', w)
        print(c, '\n')

    def test_sleep():
        print('sleep', '\n')
        sleep(TS)
    r = randint(1, PS+PG+PP)
    if r <= PS:
        test_sleep()
    elif r <= PS+PG:
        test_get()
    else:
        test_put()


def main():
    NUM_TEST = 30 # test times
    NUM_CACHE = 5
    c = Cache(NUM_CACHE)
    print(c, '\n')
    for i in range(NUM_TEST):
        test(c)


if __name__ == '__main__':
    main()
   
