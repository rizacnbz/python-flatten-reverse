#flatten

liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

new_liste = []

def flatten(x):
    for i in x:
        if isinstance(i, list):
            flatten(i)
        else:
            new_liste.append(i)

flatten(liste)
print(new_liste)

#****************************************************

#reverse

def reverse_list(x):
    x.reverse()
     
    for i in x:
        if type(i) == list:
            reverse_list(i)
    return x

liste = [[1, 2], [3, 4], [5, 6, 7]]

print(reverse_list(liste))
