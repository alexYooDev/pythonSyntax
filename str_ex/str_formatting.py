print("I am %d years old" %26)

print("I got %s ninjas on my back" %"hundred")

print("I am %d years old. I got %s ninjas on my back" %(26, "hundred"))

print("I got %s ninjas on my back" %100)

print("Percentage of rain today is %d%%" %60 )

#using format() function

print("i eat {0} apples".format(3))
print("i eat {0} apples in the {1}".format(3, "morning"))
print("i go to {place} every {day}".format(place="school",day="friday")) 

print("{0:<10}".format("hi")) #hi         #
print("{0:>10}".format("hi")) #         hi#
print("{0:^10}".format("hi")) #    hi    #
print("{0:=^10}".format("hi"))  #====hi====#

y = 3.142134234
print("{0:0.4f}".format(y)) # 3.1421

print("{{ and }}".format())   #{ and }

#using f to format string 
name = 'juanito'
age = 26
print(f'My name is {name}, I am {age}')
print(f'next year I will be {age+1}')

#sort 
print(f'{"hi":<10}')
print(f'{"hi":>10}')
print(f'{"hi":^10}')
print(f'{"hi":=^10}')

