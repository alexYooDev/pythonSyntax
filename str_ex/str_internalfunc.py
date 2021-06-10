#count function
a = 'hobby'
print(a.count('b')) #return the number of certain str inside the str

#find function
a = "Python is the best choice"
print(a.find('b')) #locates the first-found index of 'b'
#print(a.find('k')) #means nope

#index function
a = "life is short"
print(a.index('t')) #locates the first-found index of 't'
#print(a.index('k')) #Error if there is no such str

#join function 
print(",".join('abcd')) #insert ',' btwm each char in str

print(','.join(['a','b','c','d']))  # make a single str with each elements in list

#upper
a ='hi'
print(a.upper()) #to Upper case

#lower 
b = 'HI'
print(b.lower()) #to lower case

#lstrip

a = ' hi '
print(a.lstrip()) #gets rid of blanks on the left
print(a.rstrip()) #gets rid of blanks on the right
print(a.strip())  #remove blanks on the both sides

#replace 
a = 'life is too short'
print(a)
print(a.replace('life', 'your hair'))
#replace the designated str with new str

#split 
print(a.split()) #divides the str and make str list of chars


