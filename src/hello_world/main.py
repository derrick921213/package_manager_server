#!/usr/bin/python3
def main():
    from mods.mod1 import sayHi
    from test.test1 import sayHello
    print('Hello World')
    sayHi('derrick')
    sayHello()

if __name__ == '__main__':
    main()