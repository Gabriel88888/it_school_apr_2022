user_info = {
    "name" : "Alex",
    "age" : 28,
    "email" : "alex.radu@emil.com",
    "gender" : "m",

}

#lista  cheilor


u_i_keys1 = user_info.keys()
for key in user_info.keys():
    print(key)

user_info['adress'] = "Bucuresti"

print("-" * 30)

for key in u_i_keys1:
        print(key)

if len(u_i_keys1) == len(user_info.keys()):
    print("dictionar nemodificat")
else:
    print("dictionar modificat")
