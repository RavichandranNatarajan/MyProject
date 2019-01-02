inp = int(input("Give me a number\n"))
nType = "odd"
msg = ""
if inp % 4 == 0:
    nType = "even"
    msg = "You gave me {} which is {} & divisible by 4!\n".format(inp,nType)
elif inp % 2 == 0:
    nType = "even"
if msg == "": msg = "You gave me {} which is {}\n".format(inp,nType)
print(msg)

num = int(input("Okay so give me another number\n"))
check = int(input("One more number please\n"))

if num % check == 0:
    print("{} is divisible by {}!".format(num,check))
else:
    print("{} is not divisible by {}!".format(num,check))