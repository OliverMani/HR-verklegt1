def main():
    user = input("Nafn: ")
    # user = "Nanna Daema"
    user_pos  = type_of_user(user)
    print(user_pos)

def type_of_user(user):
    open_file = open("csv_files/staff.csv", "r", encoding="UTF-8")
    for line in open_file:
        line = line.split(",")
        if user in line:
           return (line[7])
        

            
if __name__ == "__main__":
    main()