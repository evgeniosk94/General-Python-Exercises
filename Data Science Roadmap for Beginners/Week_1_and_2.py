import numpy as np

# Exercise 1: Calculate the multiplication and sum of two numbers # Function
def exercise_1():
    def multiplication(number1,number2):
        product = number1 * number2
        if product <= 1000:
            print(f"The multiplication result is: {product}")
            return product
        else:
            print(f"The multiplication result is greater than 1000, so the result is: {number1 + number2}")
            return number1 + number2
    
    number1 = 30
    number2 = 30    
    result = multiplication(number1,number2)      

# Exercise 2: STRINGS
def exercise_2():
    # a)
    street = "5 Caxton Street"
    city = "London"
    country = "United Kingdom"
    address = street + ', ' + city + ', ' + country
    print("Address using '+' operator:", address)
    address = f'\n{street},\n {city},\n {country}'
    print("Address using 'f-string':", address)

    # b)
    s ="Earth revolves around the sun"
    print("print using 'slice operator':", s[6:14])
    print("print using 'negative index':", s[-3:])

    # c)
    num_fruits = 10
    num_veggies = 5
    print(f"I eat {num_fruits} fruits and {num_veggies} veggies daily")

    # d)
    s = 'maine 200 banana khaye'
    s=s.replace('banana','samosa')
    s=s.replace('200','100')
    print(s)
 
# Exercise 3: LISTS
def exercise_3():
    # a) All values in the lists have the same meaning, same type  (homogeneous)
    exp = [2200,2350,2600,2130,2190]
    
    print(f"In February I Spent {exp[1]-exp[0]} dollars more than January")
    print(f"My total expense in 1st quarter was {exp[0]+exp[1]+exp[2]}")
    print("Did I spent exactly 2000 dollars in any month?", 2000 in exp)
    
    exp.append(1980)
    print("Expenses at the end of June is:", exp[-1])
    
    exp[3] = exp[3]-200
    print("Expenses after 200 refund in April is:", exp[3])
    
    # b)
    heros=['spider man','thor','hulk','iron man','captain america']
    print("The lenght of the list is:",len(heros))
    heros.append("black panther")
    print(heros)
    heros.remove("black panther")
    print(heros)
    heros.insert(3,"black panther")
    print(heros)
    
    # c)
    heros[1:3] = ["doctor strange"]
    print(heros)
    
    # d)
    heros.sort()
    print(heros)

# Exercise 4: IF statements
def exercise_4():
    # a)
    num = input("Enter a number: ")    
    num = int(num)
    
    if num % 2==0:
        print("Number is even")
    else:
        print("Number is odd")
        
    # b)
    indian = ["samosa","daal","naan"]
    chinese = ["egg role", "pot sticker", "fried rice"]
    italian = ["pizza","pasta","risotto"]
    
    dish = input("Enter a dish name: ")
    
    if dish in indian:
        print("This dish is Indian")
    elif dish in chinese:
        print("This dish is Chinese")
    elif dish in italian:
        print("This dish is Italian")
    else:
        print(f"I dont know which cuisine '{dish}' is")
        
    # c)
    sugar_level = input("Enter your sugar level: ")
    sugar_level = float(sugar_level)
    if sugar_level < 80:
        print("Your sugar level is low")
    elif sugar_level >= 100:
        print("Your sugar level is high")
    else:
        print("Your sugar level is normal")                        

# Exercise 5: FOR LOOP statements
def exercise_5():
    # a)
    exp = [2340, 2500, 2100, 3100, 2980]
    # total = sum(exp)
    total = 0
    for i in exp:
        total = total + i
    print(total)
    
    # b)
    total = 0
    for i in range(len(exp)):   # this is equal to len(5), range() starts from zero by default
        print("Month:", i+1, "Expense:", exp[i])    # i+1 as we want month to start from 1
        total = total + exp[i]
    print("Total expense is:", total)
    
    # c)
    for i in range(1,11):
        print(i)
        
    # d)
    key_location = "chair"
    locations = ["garage","living room", "chair", "closet"] 
    for i in locations:
        if i==key_location:
            print("Key is found in:", i)
            break   # If i == chair, the operation will stop, no need to search further
        else:
            print("Key is not found in:", i)   
            
    # e)
    for i in range(1,6):
        if i %2==0:
            continue # if the number is even, continue the For-Loop, so that will skip the print section
        print(i*i)        
        
    # f)
    i = 1
    while i<=5:
        print(i)
        i = i + 1
        
    # assignment 1
    result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"] 
    heads = 0
    for i in result:
        if i=="heads":
            heads = heads + 1
    print("Heads count:", heads)   
    
    # assignment 2
    expense_list = [2340, 2500, 2100, 3100, 2980]
    num = input("Enter an expense amount:")
    num = int(num)
    
    for i in range(len(expense_list)):
        if num == expense_list[i]:
            print("Month is:",i+1)
            break
        else:
            print("This expense is not found in month", i+1)   
    
# Exercise 6: FUNCTIONS
def exercise_6():
    # a)
    def calcualte_total(exp):
        total=0
        for i in exp:
            total = total + i
        return total

    tom_exp_list = [2100,3400,3500]
    joe_exp_list = [200,500,700]

    toms_total = calcualte_total(tom_exp_list)
    joes_total = calcualte_total(joe_exp_list)

    print("Tom's total expenses:", toms_total)
    print("Joe's total expenses:", joes_total)
    
 # b)
    def calculate_area(dimension1,dimension2,shape="triangle"):
        if shape == "triangle":
            area = 1/2*dimension1*dimension2
        elif shape == "rectangle":
            area = dimension1*dimension2
        else:
            print("Error: Input shape is neither triangle nor rectangle")
            area = None 
        return area           
    
    # Calculate area of triangle 
    base=10
    height=5
    triangle_area = calculate_area(base,height,"triangle")
    print("area of triangle is:", triangle_area)
    
    # Calculate area of rectangle 
    lenght=20
    width=30
    rectangle_area = calculate_area(lenght,width,"rectangle")
    print("area of rectangle is:", rectangle_area)
    
# Exercise 7: DICTIONARIES & TUPLES 

# Also known as maps, hashtables, associate arrays
# In dictionaries you retrieve values with keys, oposite to lists where you retrieve with index
# All values in the tuples have different meaning, different type  (heterogeneous)
def exercise_7():
    # a)
    d = {"tom": 7326789820, "rob": 7325730239, "joe": 7320923203}
    d["sam"] = 7395679879
    print(d)
    del d["sam"]
    
    for key in d:
        print("key:",key,"value:",d[key])
    
    # for k,v in d.items():
    #     print("key:",key,"value:",v)    
    
    # d.clear() # Clears the dictinary 
    
    address_tuple = ("1 purple street", "new york", 10001)
    print(address_tuple)
    
    # b) - Exercise 1
    dic = {"China": 143,
           "India": 136,
           "USA": 32,
           "Pakistan": 21
           }
    
    user_input = input("Enter input: 'print', 'add', 'remove' ")
    
    if user_input == "print":
        for key in dic:
            print(key,"==>",dic[key])
    elif user_input == "add":
        country_add_input = input("Add country name to add:")
        if country_add_input in dic:
            print(f"Country '{country_add_input}' already exists in the dictionary")
        else:
            population_input = input("Enter the population:")
            dic[country_add_input] = population_input
            for key in dic:
                print(key,"==>",dic[key])
    elif user_input == "remove":
        country_remove_input = input("Enter country name to remove:")    
        if country_remove_input in dic:
            del dic[country_remove_input]
            for key in dic:
                print(key,"==>",dic[key])
        else:
            print(f"The country '{country_remove_input}' does not exist!")
    else:
        print("Non of the permitted inputs were given")        
 
    user_input_2 = input("Enter which country you want population info:")
    if user_input_2 in dic:
        print(user_input_2,"==>",dic[user_input_2])
   
    # c) - Exercise 2
    stocks = {"info": [600, 630, 620],
              "ril": [1430, 1490, 1567],
              "mtl": [234, 180, 160]
              }
    def print_operation():
        input_operation = input("Enter the kind of operation:")
        if input_operation == "print":
            for key in stocks:
                print(key,"==>",stocks[key],"==>","avg:", round(np.mean(stocks[key]),2))
        elif input_operation == "add":
                input_stock = input("Enter stock ticker:")
                if input_stock in stocks:
                        input_price = input(f"Enter price for the stock '{input_stock}':")
                        stocks[input_stock].append(float(input_price))
                        for key in stocks:
                            print(key,"==>",stocks[key])
                else:
                    input_price = input("Enter price for the new stock:")
                    stocks[input_stock] = [float(input_price)]
                    for key in stocks:
                            print(key,"==>",stocks[key])
        else:
            print("Incorrect input given by the user")
    
    print_operation()
    
   # d) - Exercise 3
    def circle_calc(radius):
        area = np.pi * radius**2
        diameter = 2*radius
        circumference = 2*np.pi*radius
        #print(f"The area of the circle is: {round(area,2)}, The diameter of the circle is: {round(diameter,2)}, The circumference of the circle is: {round(circumference,2)}")
        return area, diameter, circumference
    
    radius = input("Enter the radius of a circle:")
    radius = float(radius)       
    area, diameter, circumference = circle_calc(radius)   
    print(f"area: {round(area,2)}, circumference: {round(circumference,2)}, diameter: {round(diameter,2)}")

# Exercise 8: JSON file

# JSON is a way of storing data, recognised by all programming lagnuages, python, java, C,C++ etc.
# Dictionaries is only for python, similar to JSON
# JSON accepts only string values   
import json
import csv
def exercise_8():
    book = {}
    book['Evgenios'] = {
        'name': 'Evgenios',
        'address': '5 Caxton Street, UK',
        'phone': 7748702606
    }
    book['Tom'] = {
        'name': 'Tom',
        'address': '1 red street, NY',
        'phone': 98989898
    }
    
    s = json.dumps(book) # this will dump the dictionary and create a json, practically converts everything to string s means string     
    with open("C://Users//eugen//Desktop//Repo//General Python Exercises\\Data Science Roadmap for Beginners//book.txt", "w") as f: # to write the json file in a txt file 
        f.write(s)
        
    # f = open("C://Users//eugen//Desktop//General Python Exercises\Data Science Roadmap for Beginners//book.txt", "r") # to read a json from a txt file
    # s = f.read()
    # book = json.loads(s) # This is loading strings    
    # print(book['Evgenios']['phone'])
    
    for person in book:
        print(book[person])
        
    # Exercise 1
    word_stats = {} # initialises the dictionary
    with open("C://Users//eugen//Desktop//Repo//General Python Exercises\\Data Science Roadmap for Beginners//poem.txt", "r") as f:
        for line in f:
            words = line.split(' ') # separate the lines into list of words, ererytime a space character is found
            #print(words)
            for word in words:
                if word in word_stats:
                    word_stats[word] +=1 # increments by 1
                else:
                    word_stats[word] = 1 # if not existed, initial count of 1
    
    print(word_stats)
    
    word_occurances = list(word_stats.values())
    print(word_occurances)
    max_count = max(word_occurances)
    print("Max occurances of any word is:", max_count)
    
    print("Words with max occurances are: ")
    for word, count in word_stats.items():
        if count==max_count:
            print(word)
            
    # Exercise 2
    with open("C://Users//eugen//Desktop//Repo//General Python Exercises\\Data Science Roadmap for Beginners//stocks.csv", 'r') as file:
        csvFile = csv.reader(file)
        for row in csvFile:
            print(row)
            
    with open("C://Users//eugen//Desktop//Repo//General Python Exercises\\Data Science Roadmap for Beginners//Output.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Company Name", "PE Ratio", "PB Ratio"])
        
# Exercise 9: EXCEPTIONS
def exercise_9():
    x = input("Enter number 1: ")
    y = input("Enter number 2: ")
    try: # line thats will possibly generate an exemption we put them inside exception blocks
        z = int(x) / int(y)
    except ZeroDivisionError as e:
        print("Division by zero exception")
        z = None
    print("Division is: ", z)
    
    
    x = input("Enter number 1: ")
    y = input("Enter number 2: ")
    try: # line thats will possibly generate an exemption we put them inside exception blocks
        z = x / int(y)
    except Exception as e:
        print("Exception type:", type(e).__name__)
        z = None
    print("Division is: ", z)
    
    
    x = input("Enter number 1: ")
    y = input("Enter number 2: ")
    try: # line thats will possibly generate an exemption we put them inside exception blocks
        z = x / int(y)
    except TypeError as e:
        print("Type error exception")
        z = None
    print("Division is: ", z)

# Exercise 10: CLASSES & OBJECTS
# Properties & methods 
# Object is a specific instance of a class
def exercise_10():
    class Human:
        def __init__(self, name, occupation): # 1st step - Initialises the PROPERTIES of the class, definition of properties of the class
            self.name = name
            self.occupation = occupation
        
        def do_work(self): # 2nd step - define the METHODS - method 1
            if self.occupation == "tennis player":
                print(self.name, "plays tennis")
            elif self.occupation == "actor":
                print(self.name, "shoots a film")
                
        def speaks(self): # Define the METHODS - method 2
            print(self.name, "says how are you?")
        
    tom = Human("Tom Cruise", "actor") # Create instance of the class - Instance 1
    tom.do_work()
    tom.speaks()
    
    maria = Human("Maria Sharapova", "tennis player") # Instance 2
    maria.do_work()
    maria.speaks()
    
    # Exercise 1
    class Employee:
        def __init__(self, id, name):
            self.id = id
            self.name = name
            
        def display(self):
            print(f"ID: {self.id} \nName: {self.name}")
            
    emp = Employee(1,"coder")
    emp.display()
    
    del emp.id
    try:
        print(emp.id)
    except AttributeError as e:
        print("Attribute error exception, 'emp.id' is not defined")
        
    del emp.name
    try:
        print(emp.name)
    except AttributeError as e:
        print("Attribute error exeption, 'emp.name' is not defined")
            
            
if __name__ == "__main__":
    #exercise_1()
    #exercise_2()
    #exercise_3()
    #exercise_4()
    #exercise_5()
    #exercise_6()
    #exercise_7()     
    #exercise_8()
    #exercise_9()
    exercise_10()