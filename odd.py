numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print([num for num in numbers if num%2==1])
   
items = [1, 2, 3, 4, 5]
squares = map((lambda x: x ** 2), items)
print(list(items))
print(list(squares))

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7] 
print([num for num in numbers if num<0])

numbers = [12, 54, 33, 67, 24, 89, 11, 24, 47]
print([num for num in numbers if num%2==0])
