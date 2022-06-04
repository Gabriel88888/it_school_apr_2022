#4) Make list of dictionaries, each dictionaries contains the following attributes: name, age, gender; Read those info from keyboard input.

dictionari = [{'name' : 'Alex', 'age' : 25, 'gender' : 'M'},
{'name' : 'Gabi', 'age' : 29, 'gender' : 'M'},
{'name' : 'Mihai', 'age' : 30, 'gender' : 'M'}
]




for dict in dictionari:
    print('name:', dict['name'],'||', 'age:', dict['age'],'||', 'gender:', dict['gender'])