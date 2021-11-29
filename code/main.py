from uilayer.UIScreen import UIScreen

def main():
    user = input("Nafn: ")
    # user = "Nanna Daema"
    user_pos  = type_of_user(user)
    print(user_pos)
    UIScreen.render_header()
    print("\nPrófíll\n")
    UIScreen.render_footer()
    do = input("Slá inn aðgerð: ")
    while do != "q":
        screen = choose_screen(do)
        do = input("Slá inn aðgerð: ")


def choose_screen(screen):
    inp = screen.lower()
    if inp == "p":
        UIScreen.render_header()
        print("\nPrófíl\n")
        UIScreen.render_footer()
    if inp == "v":
        UIScreen.render_header()
        print("\nVerkefni\n")
        UIScreen.render_footer()



def type_of_user(user):
    open_file = open("csv_files/staff.csv", "r", encoding="UTF-8")
    for line in open_file:
        line = line.split(",")
        if user in line:
           return (line[7])
        

            
if __name__ == "__main__":
    main()