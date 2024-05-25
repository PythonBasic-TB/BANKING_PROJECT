def view_file(file_name):
    try:
        with open(file_name, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("File not found.")