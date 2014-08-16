# Tabulate results
## Determine overall performance on a specified deck of flashcards

def tabulate(file_name):
    ''' Compiles the number of attempts, correct reponses, and peeks
        from a results file.
    '''
    attempts = 0
    correct = 0
    peeks = 0
    with open(file_name) as f:
        for line in f:
            result = line.split('\t')
            a = int(result[0])
            c = int(result[1])
            p = int(result[2])

            attempts += a
            correct += c
            peeks += p
    f.close()

    return attempts, correct, peeks
