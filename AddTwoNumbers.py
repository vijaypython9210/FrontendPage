size=int(input('Enter List Size'))
numbers=[]
print('Enter Your Numbers:')
for i in range(0,size):
    numbers.append(int(input()))
first=int(input('Enter a First Number Index:'))
second=int(input('Enter a second number index'))
print(numbers[first]+numbers[second])