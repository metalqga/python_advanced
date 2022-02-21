def age_assignment(*args, **kwargs):
    dict={}


    for name in args:
        print(name[0])
        dict[name]=kwargs[name[0]]

    return(dict)
print(age_assignment("Peter", "George", G=26, P=19))
#print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))