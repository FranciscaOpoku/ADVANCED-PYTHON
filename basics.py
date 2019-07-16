names = ["sam", "john", "james"]
print (list(map(len,names)))

words = ["hello", "my", "name", "is", "Sam"]
print ([((word.upper()),len(word)) for word in words if len(word)])