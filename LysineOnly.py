##########################
# Paulina Panek
# Keep only Lys data
#########################

file = open("Lysine_Only_Calpha.csv", "w")
ffile = open("Lysine_Only_CO.csv", "w")
counter = 0

with open("tabs_columns.txt") as file2:
    file_contents = file2.readlines()

    size = len(file_contents)

    while counter < size:
        sentence = file_contents[counter]
        ListOfShifts = sentence.split()

        if ListOfShifts[0] == 'K':     #filter for amino acid K
            new_calpha = ListOfShifts[0] + "," + ListOfShifts[1] + "," + ListOfShifts[2] + "\n"
            file.write(new_calpha)

            new_carbonyl = ListOfShifts[0] + "," + ListOfShifts[1] + "," + ListOfShifts[3] + "\n"
            ffile.write(new_carbonyl)

        counter = counter + 1
