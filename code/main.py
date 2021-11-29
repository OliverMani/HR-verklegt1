def main():
    # user = input("Nafn: ")
    user = "Jan Jacobsen"
    user_pos  = type_of_user(user)

def type_of_user(user):
    open_file = open("code/staff.csv", "r", encoding="UTF-8")
    for line in open_file:
        print(line)
if __name__ == "__main__":
    main()