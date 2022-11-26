def FizzBuzz(iterator: int= 0, iterattions: int= 0):
    result = ''
    result += 'Fizz' * (iterator % 3 == 0)
    result += 'Buzz' * (iterator % 5 == 0)
    print(iterator, result)
    FizzBuzz(iterator+1, iterattions)