def login():
    os.system("clear")
    print("\033[1;36;49m")
    print("\033[1;36;49m")
    print("")
    usr = input("Ingresa tu nombre de usuario : ")
    usr1 = "raj"
    psw = getpass("Ingresa tu contraseña : ")
    psw1 = "5898"
    if usr == usr1 and psw == psw1:
        print("\033[1;92mlogin successfully")
        os.system("clear")
        print("\033[1;36;49m")
    else:
        print("\033[1;91m Wrong")
        login()


# This is main function
if __name__ == "__main__":
    login()
