class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print(color.PURPLE + 'Hello World !' + color.END)
print(color.CYAN + 'Hello World !' + color.END)
print(color.DARKCYAN + 'Hello World !' + color.END)
print(color.BLUE + 'Hello World !' + color.END)
print(color.GREEN + 'Hello World !' + color.END)
print(color.YELLOW + 'Hello World !' + color.END)
print(color.RED + 'Hello World !' + color.END)
print(color.BOLD + 'Hello World !' + color.END)
print(color.YELLOW + color.BOLD+ 'Hello World !' + color.END)