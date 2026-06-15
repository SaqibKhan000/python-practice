

### Data Type ###

# 1) Numeric DataTypes
# a) Integer b) Float c) 

# 2) Sequence DataTypes
# a) String b) List c) Tuple

# 3) Boolean DataType
# a) True b) False

# 4) Set DataType
  
# 5) Dictionary DataType

# 6) None DataType


# input() function is used to take input from user


# Conditional Statements


## Function ##


## Decission making with If..else




## Decorator: Esa function jo ksi dosre function k kaam ko enhance ya modify kre bina os function
# k code ko change kye
# def logger(login):
#     def wrapper():
#         print("Start")
#         login()
#         print("End")
#     return wrapper

# def login():
#     print("User logged in")
# logger(login())



## Generator: Ek esa function jo values ko sequene mein generate kre. Aur yeild keyword k through
# hm es function se at a time ek he value return kr skte hai. 

# import time
# def counter(max_num):
#     num = 1
#     while num <= max_num:
#         yield num
#         num += 1

# for number in counter(10):
#    print(number)
#    time.sleep(1)



## Iterator: Ye ek esa object(list, tuple, string, set) hota hai jo values ko ek ek krke return krta hai.



# Built in Decorators: 
# 1) @property: Ek esa decortor hota hai jo ksi method mein property ki trah behavior peda krta hai.
class User:
    name = "Saqib"
    @property
    def my_name(self):
        return "M Saqib Khan"

obj = User()
print(obj.my_name)



# 2) @staticmethod: Aisa method jo class ya object ki state use nhi karta.
class Add:
    @staticmethod
    def addition(a, b):
        return a + b
result = Add()
print(result.addition(4, 5))



# 3) @classmethod: Aisa method js mein first parameter cls hota hai jo class ko refer karta hai. Yni wo method class k attributes pr kaam krta hai.
class School:
    sch_name = "ABC"
    @classmethod
    def school_name(cls):
        return cls.sch_name
result = School()
print(result.school_name())
