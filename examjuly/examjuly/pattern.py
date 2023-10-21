"""3.print following pattern
    * * * * * * * * *
      * * * * * * *
       * * * * *
         * * *
           *

"""


n = int(input("enter the number"))
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for j in range(n, i, -1):
        print("*", end=" ")
    print()

