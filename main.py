from translator import translate

def main(): # <--- created a main class for the items that were just floating, this is better etiquette
    word = input("Enter a Word: ") # <--- changed the value from w to word, try to have variables be as descriptive as possible, but at the same time simple
    output = translate(word)
    if type(output) == list:                        # if it's a list then this will execute if it isn't then the elif will execute
        for i in output:
            print(f"\n{i}", sep="\n")
    elif type(output) == str:
        print(output)
    else:
        print("Error 404")                          # Just here to check for errors


if __name__ == "__main__": # <--- this is generally used to kick off running the program
    main()