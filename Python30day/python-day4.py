i = 0
s = str(input("Enter "+"a"+" will pass"))
i += 1
while s != 'a':
    i += 1
    print("try again")
    s = str(input("Enter "+"a"+" will pass"))


print("You Passed it!!")
print("try count: %d"%i)
