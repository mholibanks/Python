def multiplication():
    a=int(input("Enter number to start at: "))
    if a+6>12:
        print("Your input is invalid, try again witth a value that doesn't exceed 12")
    elif a+6<=12:
        print("Table from",a,"to",a+6)
        print("*    |","{0:>3}".format(a),"{0:>3}".format(a+1),"{0:>3}".format(a+2),"{0:>3}".format(a+3),"{0:>3}".format(a+4),"{0:>3}".format(a+5),"{0:>3}".format(a+6),sep=' ')
        print("-"*34)
        for i in range(a,a+7):
            print("\n","{0:<2}".format(i),"{0:>2}".format("|"),"{0:>3}".format((i*(a))),"{0:>3}".format(i*(a+1)),"{0:>3}".format(i*(a+2)),"{0:>3}".format(i*(a+3)),"{0:>3}".format(i*(a+4)),"{0:>3}".format(i*(a+5)),"{0:>3}".format(i*(a+6)),end='\n')
            print()
multiplication()