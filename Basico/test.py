

my_condition = 0
while my_condition < 20:
    print(my_condition)
    my_condition += 2
    
    
print('espacio')

count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1
    
    
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out
    
my_dic = {'name':'Roberto','surename':'Mercado','city':'grecia','state':'alajuela'}
print(my_dic['surename'])

my_dic['name']

my_newdict={'flower':'flor','tree':'arbol','water':'agua','first':'primero'}
print(my_newdict)
print(my_newdict['flower'])
 


