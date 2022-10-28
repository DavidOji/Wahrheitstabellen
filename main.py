file_name = "Wahrheitstabelle.txt"

a = False
b = True

x = not(a and b)

file = open (file_name, "wt")
file.write("        NAND     \n ")
file.write(" ================\n")
file.write(" A     | B     | C \n")
file.write("-------+-------+------\n")
a = False
b = False
x = not (a and b)
file.write(str(a) + "  |" + str(b) + "   |" + str(x) + "\n")
a = False
b = True
x = not (a and b)
file.write(str(b) + "   |" + str(a) + "   |" + str(x) + "\n")
a = True
b = False
x = not (a and b)
file.write(str(a) + "   |" + str(b) + "   |" + str(x) + "\n")
a = True
b = True
x = not (a and b)
file.write(str(b) + "   |" + str(b) + "    |" + str(x) + "\n")


file.write("        AND     \n ")
file.write(" ================\n")
file.write(" A     | B     | C \n")
file.write("-------+-------+------\n")
a = False
b = False
x = (a and b)
file.write(str(a) + "  |" + str(b) + "   |" + str(x) + "\n")
a = False
b = True
x = (a and b)
file.write(str(b) + "   |" + str(a) + "   |" + str(x) + "\n")
a = True
b = False
x = (a and b)
file.write(str(a) + "   |" + str(b) + "   |" + str(x) + "\n")
a = True
b = True
x = (a and b)
file.write(str(b) + "   |" + str(b) + "    |" + str(x) + "\n")


file.write("        OR     \n ")
file.write(" ================\n")
file.write(" A     | B     | C \n")
file.write("-------+-------+------\n")
a = False
b = False
x = (a or b)
file.write(str(a) + "  |" + str(b) + "   |" + str(x) + "\n")
a = False
b = True
x = (a or b)
file.write(str(b) + "   |" + str(a) + "   |" + str(x) + "\n")
a = True
b = False
x = (a or b)
file.write(str(a) + "   |" + str(b) + "   |" + str(x) + "\n")
a = True
b = True
x = (a or b)
file.write(str(b) + "   |" + str(b) + "    |" + str(x) + "\n")


file.write("        NOT     \n ")
file.write(" ================\n")
file.write(" A    | C \n")
file.write("-------+-------\n")
a = False
x = not a
file.write(str(a) + "  |" + str(x) + "\n")
b = True
x = not b
file.write(str(b) + "   |" + str(x) + "\n")


file.write("        NOR     \n ")
file.write(" ================\n")
file.write(" A     | B     | C \n")
file.write("-------+-------+------\n")
a = False
b = False
x = not (a or b)
file.write(str(a) + "  |" + str(b) + "   |" + str(x) + "\n")
a = False
b = True
x = not (a or b)
file.write(str(b) + "   |" + str(a) + "   |" + str(x) + "\n")
a = True
b = False
x = not (a or b)
file.write(str(a) + "   |" + str(b) + "   |" + str(x) + "\n")
a = True
b = True
x = not (a or b)
file.write(str(b) + "   |" + str(b) + "    |" + str(x) + "\n")

file.close()


