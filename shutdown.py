def shutdown(command):
    if command == "yes":
        return "Shutting down"
    elif command == "no":
        return "Shutdown stopped"
    else:
        return "Sorry"

choice = input("Do you want to shutdown (yes/no): ")
print(shutdown(choice))