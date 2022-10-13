
with open("5letterlist.txt", "r") as file:

    content = file.read()


words = content.split("\n")

print(f"Total words: {len(words)}")
