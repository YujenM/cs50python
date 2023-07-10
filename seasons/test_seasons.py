from seasons import minutes_lived
def main():
    test_1()


def test_1():
    assert minutes_lived(2021, 12, 24)=="Five hundred twenty-five thousand, six hundred minutes"
    assert minutes_lived(2020, 12, 24)=="One million, fifty-one thousand, two hundred minutes"
    assert minutes_lived(23,1,2020)== "Invalid Date"


if __name__=="__main__":
    main()