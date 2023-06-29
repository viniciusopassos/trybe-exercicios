def analyse(text):
    report = ""
    # qtd palavras
    count_words = len(text.split(" "))
    report += f"Número de palavras = {count_words}\n"

    # qtd caracteres
    char_count = dict()
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    report += f"Números de caracteres = {char_count}"

    return report


text_to_analyzer = (
    "Lorem ipsum dolor sit amet"
    "consectetur adipiscing elit. Sed egestas aliquam ultricies"
    "Duis vel elit ut dolor mollis sodales"
    "Praesent venenatis id nisl sed lacinia"
    "Praesent vel facilisis augue."
)

print(type(text_to_analyzer))

print(analyse(text_to_analyzer))
