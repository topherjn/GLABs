word1 = "hello"
word2 = "hello"

# they automatically have the same mem address
print(word1==word2)
print(word1 is word2)

# try to force the issue - it doesn't work
word3 = str(word1)
print(word1 == word3)
print(word1 is word3)

a = 4
b = 4
c = a

print(a==b)
print(a is b)
print(c is a)

b = 5
print(a==b)
print(a is b)
print(c is a)
