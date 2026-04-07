names = input("Enter the names:").split()
years = input("Enter the years:").split()
symbols = input("Enter the symbols:").split()
passlenthuL = int(input("Enter the password lower length:")) 
passlenthuU = int(input("Enter the password lower length:"))
file_name = input("Enter the file name: ")
for name in names:
    for year in years:
        for sym in symbols:
            with open(file_name, "a") as f:
                passowrds = name + sym + year + sym 
             

                x = len(passowrds)
                if x>=passlenthuL and x<=passlenthuU:
                    f.write(passowrds + "\n")
                    
