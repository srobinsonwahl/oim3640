def my_abs(number):
    if number < 0:
        return -number
    else:
        return number

def main():
    print(my_abs(-10))

# to avoid executing this file when it is imported in another file
if __name__ == "__main__":
    main()