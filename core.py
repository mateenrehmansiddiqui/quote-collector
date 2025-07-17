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

def delete_quote(index, file_path = "quotes.txt"):
    with open(file_path, "r") as file:
        quotes = file.readlines()

    if index >= 0 and index < len(quotes):
        deleted_quote = quotes.pop(index)
        with open(file_path, "w") as file:
            file.writelines(quotes)

        print(f"[x] Removed: {deleted_quote.strip()}")

    else:
        print("[!] Invalid Index.")

