# If num % 3 = true print fizz
# If num % 5 = true print buzz
# If num % 5 = true and num % 5 = true print fizzbuzz
# for and while loops



#-----------------#
range 100 > (101)
for fizzbuzz in range(1, 101):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)



#-----------------#

Make it one line
for i in range(1, 101): 
    print("Fizz"*(i % 3 == 0)+"Buzz"*(i % 5 == 0) or str(i)) # str(i) required to print the numbers

#-----------------#



 count = 0
while count < 101:
    if (count % 5) == 0 and (count % 3) == 0:
        print("FizzBuzz")
        count +=1
    elif (count % 3) == 0:
        print ("Fizz")
        count +=1
    elif (count % 5) == 0:
        print ("Buzz")
        count +=1
    else:
        print (count)
        count +=1
#-----------------#