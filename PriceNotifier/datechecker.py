def checkDate(d: int):
    if d < 0:
        print("date not valid")
    else:
        i = int(str(d)[:5])
        notLP = "not leap year"
        yesLP = "it is a leap year"
        s = notLP if i % 4 != 0 else yesLP if i % 100 != 0 else notLP if i % 400 != 0 else yesLP
        print(s)

if __name__ == "__main__":
    date = int(input("insert date:> "))
    checkDate(date)