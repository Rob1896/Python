

#1 Use for, .split(), and if to create a Statement that will print out words that start with 's':


st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':  # el 0 es la primer letra de cada palabra por indexing
        print(word)
        
#2 Use range() to print all the even numbers from 0 to 10.

list1 = list(range(0,11,2)) # los numeros pares van de 2 en 2 por eso el 2 al final 
print(list1)
print(type(list1))

list2 = list(range(0,24,2))
print(list2)

print([num for num in range(1,11) if num % 2 == 0])# se crea la lista al hacer el print por eso lleva []
print([num for num in range(0,24) if num % 2 == 0])

lista3 = [[num for num in range(0,16) if num % 2 == 0]]
print(lista3)

#3 Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3

list4 = [x for x in range(1,51) if x%3 == 0]
print(list4)

list0 = list(range(0,51,3))
print(list0)

#3 Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word)%2 == 0:
        print(word+" <-- has an even length!")
        

#Use a List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'
[word[0] for word in st.split()] # shit + enter

  














  
    
        
        
        
        
    
        
    



    