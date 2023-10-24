# Open numbers file 
# bug introduced on line 9 doesn't check for even number: NBH
with open("numbers.html", "w") as f:
    # Create the header
    f.write("<html>\n<head>\n<title>List of Numbers</title>\n</head>\n<body>\n")
    f.write("<table>\n<tr><th>Even Numbers</th><th>Odd Numbers</th></tr>\n")
    # Determine if numbers 1-50 are even or odd and write them into the corresponding column 
    for i in range(1, 50):
        if i % 2 != 0:
            f.write("<tr><td>{}</td><td></td></tr>\n".format(i))
        else:
            f.write("<tr><td></td><td>{}</td></tr>\n".format(i))
    f.write("</table>\n</body>\n</html>")
     
# Print the contents of the file
with open("numbers.html", "r") as f:
    print(f.read())
    
