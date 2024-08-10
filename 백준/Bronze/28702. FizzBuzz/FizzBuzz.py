for i in range(3):
    temp=input()
    if temp != 'FizzBuzz' and temp != 'Fizz' and temp != 'Buzz':
        target=int(temp)+3-i
if target%3==0 and target%5==0:
    print('FizzBuzz')
elif target%3==0:
    print('Fizz')
elif target%5==0:
    print('Buzz')
else:
    print(target)