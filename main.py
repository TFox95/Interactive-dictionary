import translator

def main(): # <--- created a main class for the items that were just floating, this is better etiquette
    answer = input("Do you want to use voice?\n y/n: ")
    if "y" in answer:
        translator.vtranslation()
    elif "n" in answer:
        translator.wtranslation()
if __name__ == "__main__": # <--- this is generally used to kick off running the program
    main()