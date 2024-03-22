def menu():
    while(True):
        print("_" * 35)
        print("1. Tax")
        print("2. Monthly Pay for Sales Employees")
        print("3. Water Charges")
        print("4. Property Tax")
        print("5. School Transport")
        print("0. Exit")
        print("_" * 35)
        option = input("Choose an option (0-5): ")

        match option:
            case "1":
                print("CALL FUNCTION HERE")
            case "2":
                print("CALL FUNCTION HERE")
            case "3":
                print("CALL FUNCTION HERE")
            case "4":
                print("CALL FUNCTION HERE")
            case "5":
                print("CALL FUNCTION HERE")
            case "0":
                break
            case other:
                print("Sorry, this option does not exist!")

if __name__ == "__main__":
    menu()