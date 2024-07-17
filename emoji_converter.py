message = input(">")
words = message.split(" ")

emoji_mapping = {
    ":)": "😀",
    ":(": "☹️",
    "<3": "❤️"
}
output = ""
for word in words:
    output += emoji_mapping.get(word, word) + " "
print(output)