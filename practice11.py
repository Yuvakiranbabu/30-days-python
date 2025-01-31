#getting list and dictionaries as arguments in fuctions

def students(*studet_names):
    print(studet_names)


def students_powers(**their_powers):
    print(their_powers)

    
students("peter","ben tennyson","bakugo")
students_powers(peter="spiderman",ben_tennyson="omnitrix",bakugo="qurik")