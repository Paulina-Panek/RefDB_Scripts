counter = 0

with open("RefDB-C.db") as file:

    file_contents = file.readlines()
    file1 = open("no_header_RefDB.txt", "w")
    x = True

    while counter < len(file_contents):
        if not (file_contents[counter].startswith('#') or file_contents[counter].startswith('>')):
            print(file_contents[counter])
            print(counter)
            file1.write(file_contents[counter])

        counter = counter + 1
