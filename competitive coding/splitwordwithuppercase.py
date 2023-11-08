word="saveChangesInTheEditor"
for i in word:
    if i!=i.upper():
        print(i.upper(),end="")
    else:
        print();
        print(i.lower(),end="")