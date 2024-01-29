def greet(name, age, gender):
    print(f'Hi {name}, you are {age} years old and you are a {gender}')

greet(gender= 'male', name= 'John', age= 23)   # here I have used keyword arguments to pass the arguments
                                                # that way no matter how we order it the code will run