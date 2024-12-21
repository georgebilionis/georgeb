#Got List Index out of range error, fixed the range
#SyntaxError: didn't properly orientate the semi-colon within brackets
#IndentationError: improper indentation on method separation

#2.1
whateverNameYouWant = list(range(21))
print(whateverNameYouWant)

#2.2
def squareList(input_list):
    return [x ** 2 for x in input_list]


whateverNameYouWant = list(range(21))
anotherNameYouWant = squareList(whateverNameYouWant)
print(anotherNameYouWant)  

#2.3
def first_fifteen_elements(input_list):
    return input_list[:15]


first_fifteen = first_fifteen_elements(anotherNameYouWant)
print(first_fifteen)  


#2.4
def every_fifth_element(input_list):
    return input_list[4::5] 


every_fifth = every_fifth_element(anotherNameYouWant)
print(every_fifth)  

#2.5
def fancy_function(input_list):
    
    last_30_elements = input_list[-30:]
   
    result = last_30_elements[::-1][::3]
    return result





