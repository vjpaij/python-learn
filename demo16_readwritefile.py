# file = open('C:\Users\ga26\retek_del_date.txt')
# try:
#     #do file operations
#     pass
# finally:
#     file.close()

# better way to open file. this would close the file aitomatically even in case of exception
with open('C:/Users/ga26/retek_del.dat') as file:
    page = file.read() # -> reads full text file
    print(page)
    
    result = file.readline() # -> returns a list of Strings of all lines in the file
    for line in result:
        print(line)
    
    for line in file: # -> shorter code to read all lines in the file
        print(line)

depot_check = input("Enter the depot number to check:\n")
found=False

def main():
    try:
        with open('C:/Users/ga26/retek_del.dat') as file:
            for line in file: # -> shorter code to read all lines in the file
                if depot_check in line:
                    print(line)
                    found=True
                    break # -> as soon as match found, comes out of the loop
    except FileNotFoundError as e:
        print("File not found")
        return # -> to stop further processing of the code

    if not found:
        print("Depot number not in the file")
        with open('C:/Users/ga26/retek_del.dat','a') as file: # a-> appends, w-> overwrites
            file.write(depot_check)

main()
        



    