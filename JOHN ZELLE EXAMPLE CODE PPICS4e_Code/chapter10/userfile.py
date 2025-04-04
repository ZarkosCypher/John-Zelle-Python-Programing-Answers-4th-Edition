# userfile.py
#    Program to create a file of usernames in batch mode.

def main():
    print("This program creates a file of usernames from a")
    print("file of names.")

    # get the file names
    infileName = input("What file are the names in? ")
    outfileName = input("What file should the usernames go in? ")

    # open the files
    with open(infileName, "r") as infile, open(outfileName, "w") as outfile:
        # process each line of the input file
        for line in infile:
            # get the first and last names from line
            first, last = line.split()
            # create the username
            uname = (first[0]+last[:7]).lower()
            # write it to the output file
            print(uname, file=outfile)

    print("Usernames have been written to", outfileName)


if __name__ == "__main__":
    main()
