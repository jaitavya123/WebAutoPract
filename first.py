print("hi")
# exception handling
'''try:
    a=2/0
    print(a)
except ArithmeticError as d:
    print(d)'''                               # exception handling simple example end

try:
 a1=open("start.txt","w")                    # open("start.txt","w") create an empty file
 data=input("type somethng")                 # taking user data into files
 a1.write(data)
 a1.close()
 print("read mode ")
 a2 = open("start.txt", "r")
 #a2.seek(3)                                  # move cursor to any desired position
 #a2.tell()                                   # give current location of cursor
 print(a2.read())
 a2.close()
 print("APPEND mode ")
 a3=open("start.txt", "a+")
 a3.write(" appended txt")
 a3.seek(0)
 print("after appending ==", a3.read())
except FileExistsError as excep1:
    print(">>>>>>>>>Exception",excep1)
except FileNotFoundError as except2:
    print(">>>>>>>>>Exception",except2)



