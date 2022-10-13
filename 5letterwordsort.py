
with open("words.txt", "r") as file:
    
    content = file.read()
    
    
words = content.split("\n")

newlist = ""

for word in words:
    
    
    if len(word) > 5:
        
        continue
    
    newlist = newlist + word + "\n"
    
    
with open("5letterlist.txt", "w") as file:
    
    
    file.write(newlist)
    

