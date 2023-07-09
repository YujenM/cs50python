def main():
    answer = input("Time? ")
    time = convert(answer.upper())
    if time >= 7 and time <= 8:
        print("breakfast time")

    if time >= 12 and time <= 13:
        print("lunch time")

    if time >=  18 and time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(':')
    new_minute = float(minutes)/60
    new_hour = float(hours)
    new_time = new_hour + new_minute
    return new_time

if __name__ == "__main__":
    main()