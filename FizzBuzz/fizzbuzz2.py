fizzbuzz = ['Fizz'*(i%3==0)+'Buzz'*(i%5==0) or str(i) for i in range(1,101)]
print('\n'.join(fizzbuzz))
