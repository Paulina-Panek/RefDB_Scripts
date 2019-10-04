###############################################################
# Paulina Panek                                               #
# Leaves only columns 1,2,4,6                                 #
# That is: aa code, COIL/HELIX/SHEET, Calpha ppm, CO ppm      #
###############################################################
whateva = open("tabs_columns.txt", "w")
counter2 = 0

with open("no_header_RefDB.csv") as file2:
    file_contents2 = file2.readlines()

    size = len(file_contents2)

    print("file_contents2 len = ", size)

    while counter2 < size:
        sentence = file_contents2[counter2]
        ListOfShifts = sentence.split()

        if ListOfShifts[0].isspace():
            print("break", counter2)
            break
        else:
            print("Counter2: ", counter2)
            new_sentence = ListOfShifts[1] + "\t" + ListOfShifts[2] + "\t" + ListOfShifts[4] + "\t" + ListOfShifts[6] + "\n"
            whateva.write(new_sentence)

            counter2 = counter2 + 1




