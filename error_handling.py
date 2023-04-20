# try catch block - try except block
# throwing errors - raise errors
# custom errors

class NegativeError(Exception):
    pass

try:
    n = int(input("Enter a numerator: "))

    d = int(input("Enter a denominator: "))

    # let us suppose that we don't accept negative numbers
    if n < 0 or d < 0:
        raise NegativeError("No negative numbers please")

    q = n / d

    print(q)
except ValueError as e:
    print(e)
    print(type(e))
    print("Please type in numbers only")
except ZeroDivisionError:
    print("Denominator cannot be zero")
except NegativeError as e:
    print(e)
except Exception as e:
    print(e)
    print("Something went wrong")
finally:
    print("Finally")


print("The end of the program")