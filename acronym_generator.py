input_phrase = input("Enter a phrase:\n")
phrase_list = input_phrase.split()
output = ""
for word in phrase_list:
    output += word[0].upper()

print(output)
