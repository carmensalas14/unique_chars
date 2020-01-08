"""
PEDAC 
P -
checking every element of any input that is a string 
if the element repeats itself then it is not a unique string and returns false 
if the string is comprised of unique characters it will return true 

input - string 
output - boolean 

E - 
'abcdefg' == true
'abbcdefg' == false 
'carmen' == true
'omarr' == false
'' == None

D - 
string

A -
if input is empty return None
iterate through every element of the string

loop through string to check every elemtent

at every element loop through all indexes again to check if they match

if they match return false 

if they do not match continue the first loop until it is done 
 
if all characters in the first did not match return true 
~~~
create an empty obj
loop through str

 ~~ for element of the str see if it matches the key in the object 
if it does return false 
if it does not create a property with the element and set it to 1 

"""
def unique_chars(str):
    if len(str) == 0:
        return None
        
    dic = {}
    for char in str:
        if char in dic:
            return False 
        else:
            dic[char] = 1
    return True
    
print(unique_chars("abcdefg"))
print(unique_chars("abbcdefg"))
print(unique_chars(""))


def naive_unique_chars(str):
    if len(str) == 0:
        return None
        
    for char in str:
        for letter in str:
            if char == letter:
                return False
                
    return True  
    
# print(unique_chars("abcdefg"))
# print(unique_chars("abbcdefg"))
# print(unique_chars(""))
    