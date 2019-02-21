# coding: utf8 
import time
from singletonscript import SingletonScript


def main():
    print('main is running')
    time.sleep(10)
    print('main finished')

if __name__ == '__main__':
    SingletonScript()
    main()
