def add_quote(quote, file_path = "quotes.txt"):
    with open(file_path, "a") as file:
        file.write(quote + "\n")
    print("[+] Quote Added!")

def list_quotes(file_path = "quotes.txt"):
    print("-----SAVED QUOTES-----")
    with open(file_path, "r") as file:
        quotes = file.readlines()
        for line in quotes:
            print("•", line.strip())
