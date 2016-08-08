while True:
    try:
        number = int(input("What's your fav number?\n"))
        print(18/number)
        break
    except ValueError:
        print("make sure and enter a number")
    except ZeroDivisionError:
        print("Don't pick zero")
    except:
        break
    finally:
        print("loop complete")