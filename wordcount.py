
with open("words.txt", "r") as file:

    content = file.read()


words = content.split("\n")

print(f"Total words: {len(words)}")
