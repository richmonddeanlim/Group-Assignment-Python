from function import accountant
from function import student
from function import lecture
from function import administrator

try:
    while True:
        # Creating program menu
        print("="*50)
        print(f"{"University Management System":^50}")
        print("="*50)
        print("1.Administrator")
        print("2.Lecturer")
        print("3.Student")
        print("4.Registrar")
        print("5.Accountant")
        print("6.Exit")
        print("="*50)

        # Getting user choice
        while True:
            try:
                function_choice = int(input("Input your option: "))
                break
            except ValueError:
                print("Pls Input an Interger")

        # Calling admin main function
        if function_choice == 1:
            print("\n")
            administrator.main()

        # Calling lecturer main function
        elif function_choice == 2:
            print("\n")
            lecture.main()
            
        # Calling student main function
        elif function_choice == 3:
            print("\n")
            student.main()
        
        # Calling registrant main function
        elif function_choice == 4:
            # copy paste the main here
            pass
        
        # Calling Accountant main function 
        elif function_choice == 5:
            print("\n")
            accountant.main()
        
        elif function_choice == 6:
            print("\nExiting the program")
            break

        else:
            print("That option is not available")

except KeyboardInterrupt:
    pass