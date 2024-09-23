contacts = {
    'number' : 3,
    'students' : 
    [
        {'name' : 'Raja Jaiswal', 'email':'raja_jaiswal@gmail.com'},
        {'name' : 'Roshini Gajendra', 'email':'ros_gaj@yahoo.com'},
        {'name' : 'Sonali Kaur', 'email':'sonali_kaur00@outlook.com'}
    ]
}

print("Get all email ids:")
for stud in contacts['students']:
    print(stud.get('email'))
    