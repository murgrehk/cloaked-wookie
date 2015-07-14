# Tabulate Results

## Determines overall performance on a specified deck of flashcards

def tabulate(file_name):
    ''' Compiles the number of attempts, correct responses, and peeks
        from a results file.
    '''

    results = []

    with open(file_name) as f:
        for line in f:
            result = [int(elem) for elem in line.split('\t')]
            results.append(result)
    f.close()

    if len( results ) > 0:
        [attempts, correct, incorrect, peeks] = list(map(sum, zip(*results)))
    else:
        [attempts, correct, incorrect, peeks] = [0, 0, 0, 0]

    return { 'attempts' : attempts, 'correct' : correct, 'incorrect' : incorrect, 'peeks' : peeks }
