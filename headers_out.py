########################################################
# Paulina Panek                                        #
# Produces file with no headers or empty lines         #
########################################################
import string
counter = 0

with open("RefDB-C.db") as file:

    file_contents = file.readlines()
    print("RefDB len: ", len(file_contents))
    file1 = open("no_header_RefDB.csv", "w")
    x = True

    print("file_contents len = ", len(file_contents))

    while counter < len(file_contents):
        if not (file_contents[counter].startswith('#') or file_contents[counter].startswith('>') or file_contents[counter].startswith('\n')):

            file1.write(file_contents[counter])

        counter = counter + 1

