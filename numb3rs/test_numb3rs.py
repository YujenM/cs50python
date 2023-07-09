from numb3rs import validate
def main():
    test_ip()
def test_ip():
    assert validate("192.168.1.1")==True
    assert validate("1.2.3.4")==True
    assert validate("255.255.255.255")==True
    assert validate("127.0.0.1")==True
    assert validate("512.1.1.1")== False
    assert validate("1.512.1.1")== False
    assert validate("1.1.512.1")== False
    assert validate("1.1.1.512")== False
    assert validate("192.168.1")==False
    assert validate("75.456.76.65")==False
    assert validate("512.512.512.512")==False
    assert validate("1.2.3.1000")==False
    assert validate("cat")==False
    assert validate("0.0.0.0")==True
    assert validate("192.168.1.255")==True



if __name__=="__main__":
    main()