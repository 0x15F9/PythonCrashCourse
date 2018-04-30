def read_file(filename):
    try:
        with open(filename, 'r') as file_object:
            contents = file_object.read()
            print(contents)
    except IOError as e:
        pass
    except Exception as ex:
        pass

read_file('cats.txt')
read_file('dogs.txt')
read_file('dogs.tx')