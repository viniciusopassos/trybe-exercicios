import json

# Manipulação de arquivos sem o gerenciador de escopo with

# file = open("video_games.json", "r")
# video_games = json.load(file)
# file.close()

# ----------------------------------------------------------

# tratamento de exceções em manipulação de arquivos

# try:
#     with open("video_game.json", "r") as file:
#         video_games = json.load(file)
# except FileNotFoundError as Erro:
#     print(Erro)
# except json.decoder.JSONDecodeError:
#     print("Arquivo incorreto")
# finally:
#     print("Tentativa de abrir o arquivo")

# ----------------------------------------------------------

# extrair e imprimir informações do arquivo JSON

# with open("video_games.json", "r") as file:
#     video_games = json.load(file)

# print(video_games[0]["Metadata"]["Genres"])
# print(video_games[0]["Metrics"]["Sales"])

# ----------------------------------------------------------

with open("video_games.json", "r") as file:
    video_games = json.load(file)

# Genres
game_genres = set()  # set é o conjunto que não repete dados iguais

for game in video_games:
    # print(game['Title'])
    # print(len(video_games))
    for genre in game["Metadata"]["Genres"].split(","):
        game_genres.add(genre)

# Console
consoles = set()

for game in video_games:
    for console in game:
        consoles.add(game["Release"]["Console"])

print(game_genres)
print(consoles)
print(len(consoles))
