from bank import value
def main():
    testing_value1()
    testing_value2()
    testing_value3()

def testing_value1():
    assert value("HELLO gi")==0
    assert value("hello gi ")==0
    assert value("hello")==0

def testing_value2():
    assert value("H")==20
    assert value("h")==20
    assert value("h")==20
    assert value("hey")==20
    assert value("hey")==20


def testing_value3():
    assert value("What's up?")==100
    assert value("WHAT'S UP")==100
    assert value("Goodorning")==100


if __name__=="__main__":
    main()
