import translator

def main(): # <--- created a main class for the items that were just floating, this is better etiquette
    answer = input("Do you want to use voice or text?\n v/t: ")
    if "v" in answer:
        translator.vtranslation()
    elif "t" in answer:
        translator.wtranslation()
if __name__ == "__main__": # <--- this is generally used to kick off running the program
    main()
