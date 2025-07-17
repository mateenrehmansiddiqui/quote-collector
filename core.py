def add_quote(quote, file_path = "quotes.txt"):
    with open(file_path, "a") as file:
        file.write(quote + "\n")
    print("[+] Quote Added!")

