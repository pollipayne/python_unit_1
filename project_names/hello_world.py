
#create a function that: 

# makes aa list that contains all the differences/
# between the two sequences

#find each difference and add to the list 

#sequences: 
#    1.  GAGCCTACTAACGGGAT
#    2.  CATCGTAATGACGGCCT


def find_list_diff(sequence_a, sequence_b):
    differences = []
    n = 0
    for letter in sequence_a:
        if letter == sequence_b[n]:
            pass 
        else:
            differences.append(letter)
        n = n + 1
    print(differences)

sequence_a = 'GAGCCTACTAACGGGAT'

sequence_b = 'CATCGTAATGACGGCCT'

find_list_diff(sequence_a, sequence_b)



