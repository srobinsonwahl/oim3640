while True:
    try:
        number = int(input('enter a number:'))
        result = 2023 / number
        print(result)
        break
    except ValueError as e:
        print('You should enter an integer!')
        print(e)
    except ZeroDivisionError:
        print('You cannot divide by 0!')
    except:
        print('I do not know what you just did but it is wrong.')
    finally:
        print('No matter what happens, we will get here finally.')

print('Hello, world!') # I still want to print this no matter what