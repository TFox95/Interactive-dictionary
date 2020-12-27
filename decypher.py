def decypher(output):
    if type(output) == list:
        for item in output:
            print(f"\n{item}", sep="\n")
    elif type(output) == str:
        print(output)
    else:
        print("error code 404")