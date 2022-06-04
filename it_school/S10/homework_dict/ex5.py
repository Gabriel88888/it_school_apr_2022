#5) sort list by users age


users = [
    ('Alex', 25),
    ('Gabi', 29),
    ('George', 23),
    ('Mihai', 24),
]

def sort_user(user):
    return user[1]

users.sort(key = sort_user)
print(users)