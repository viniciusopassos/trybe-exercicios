import json  # json é um modulo que vem embutido, porém precisamos importá-lo

with open("pokemons.json") as file:  # dentro do gerenciador de contexto with
    content = file.read()  # leitura do arquivo
    pokemons = json.loads(content)["results"]  # o conteúdo é transformado em
    # estrutura python equivalente, dicionário neste caso. acessamos a chave
    # results que é onde contém nossa lista de pokemons   
print(type(pokemons[4]))


# A leitura pode ser feita diretamente do arquivo, utilizando o método load ao
# invés de loads. O loads carrega o JSON a partir de um texto e o load carrega
# o JSON a partir de um arquivo.

with open("pokemons.json") as file:
    pokemonsList = json.load(file)["results"]
    for pokemon in pokemonsList:
        print(pokemon["name"])


# A escrita de arquivos no formato JSON é similar à escrita de arquivos
# comuns, porém temos que transformar os dados primeiro.

# Leitura de todos os pokemons
with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]

# Separamos somente os do tipo grama
grass_type_pokemons = [
    pokemon for pokemon in pokemons if "Grass" in pokemon["type"]
]

# Abre o arquivo para escrevermos apenas o pokemons do tipo grama
with open("grass_pokemons.json", "w") as file:
    # conversão de Python para o formato json (str)
    json_to_write = json.dumps(grass_type_pokemons)
    file.write(json_to_write)


# Assim como a desserialização, que faz a transformação de texto em
# formato JSON para Python, a serialização (caminho inverso) possui um
# método equivalente para escrever em arquivos de forma direta.

# leitura de todos os pokemons
with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]

# separamos somente os do tipo grama
grass_type_pokemons = [
    pokemon for pokemon in pokemons if "Grass" in pokemon["type"]
]

# Abre o arquivo para escrita
with open("grass_pokemons.json", "w") as file:
    # escreve no arquivo já transformado em formato json a estrutura
    json.dump(grass_type_pokemons, file)

# Arquivos JSON não seguem a nomenclatura habitual de leitura e escrita
# (write e read), pois são considerados formatos de serialização de dados.
# Seguem então as mesmas nomenclaturas utilizadas em módulos como marshal e
# pikle, que também são formatos de serialização.
