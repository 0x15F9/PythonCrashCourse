def read_file(filename):
    try:
        with open(filename, 'r') as file_object:
            contents = file_object.read()
            print(contents)
    except IOError as e:
        print('An error occurred. File not found.')
    except Exception as ex:
        print('A general exception occurred.\n {}'.format(ex))

read_file('cats.txt')
read_file('dogs.txt')
read_file('dogs.tx')