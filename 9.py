

# ----------------- დავალება 9 -----------------
# 1. დაწერეთ პითნის ფუნქცია, რომელიც იღებს პარამეტრად ერთი დაიგივე ზომის სიას (list) და zip ფუნქციის გამოყენებით დააჯგუფეთ სიების ელემენტები.
#     params: [1, 2, 3], ['a', 'b', 'c']  
#     outputs: ["(1, 'a')", "(2, 'b')", "(3, 'c')"]

# def zipall(arr1,arr2):
#     return list(zip(arr1,arr2))
# print(zipall([1, 2, 3], ['a', 'b', 'c']))

# 2. დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს. ფუნქციაში გაითვალისწინეთ 
    # გამონაკლისები (Exceptions), 
    # თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError).ფუქნციის დასაწერად გამოიყენეთ lambda და functools-ის reduce მეთოდი.
# params:[1, 2, 3, 4, 5] 
# output: 120


# from functools import reduce
# params = [1, 2, 3, 4, 5] 
# try:    
#     namravli = reduce(lambda x,y: x * y, params)
# except Exception as e:
#     print(e)
# else:
#     print(namravli)
    


# 3. დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების სიას (list) და აბრუნებს მხოლოდ სიის კენტ ელემენტებს.
#     params: [1, 2, 3, 4, 5, 6, 7]
#     outputs: [1, 3, 5, 7]

# params =  [1, 2, 3, 4, 5, 6, 7]
# odd = list(filter( lambda x: x % 2 == 1, params ))
# print(odd)
    
# 4.დაწერეთ პითნის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს (ending). დააბრუნეთ მხოლოდ სიის ის ელემენტები 
    # რომელიც მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით. გამოიყენეთ lambda და filter ფუნქცია. გაითვალისწინეთ გამონაკლისები (TypeError),
    #  თუ სხვა გამონაკლისიც აღმოჩნდა ისიც გაითვალისწინეთ.
#     მინიშნება: გადაავლეთ თვალი string მეთოდებს, მონახეთ ისეთი მეთოდი, რომელიც აბრუნებს სიტყვას, რომელიც მთავრდება რაღაც სიმბოლოებით...

#     params: ['hello', 'world', 'coding', 'nod'], 'ing'  
#     outputs: ['coding']
    

# params = ['hello', 'world', 'coding', 'nod']
# ending = 'ing'
# try:
#     res = list(filter(lambda x: x.endswith(ending), params ))
#     print(res)
# except Exception as e:
#     print(e)



# /----------------- დავალება 9 -----------------