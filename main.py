import translator
import history

def main(): # <--- created a main class for the items that were just floating, this is better etiquette

    answer = input("Do you want to use voice,text, or view history?: ")
    if ("voice") in answer:
        translator.vtranslate()
    elif ("text") in answer:
        translator.translate()
    elif ("history") in answer:
        history.history()
if __name__ == "__main__": # <--- this is generally used to kick off running the program
    main()
