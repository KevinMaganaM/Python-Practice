message = input(">")
words = message.split(" ")

emojie_mapping = {
    ":)": "😀",
    ":(": "☹️",
    "<3": "❤️"
}
output = ""
for word in words:
    output += emojie_mapping.get(word, word) + " "
print(output)