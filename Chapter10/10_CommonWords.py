# Metamorphosis-FranzKafka.txt

def read_file(filename):
    try:
        with open(filename, 'r') as file_object:
            contents = file_object.read()
            return contents
    except IOError:
        print('File not Found')
        return

def get_count(string, word):
    ''' Get the number of times word occurs in string'''
    return string.lower().count(word)

contents = read_file('Metamorphosis-FranzKafka.txt')
print(get_count(contents, 'the'))