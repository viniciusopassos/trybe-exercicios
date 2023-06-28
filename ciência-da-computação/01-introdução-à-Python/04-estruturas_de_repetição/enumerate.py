languages = ['Python', 'Java', 'JavaScript']

enumerate_prime = enumerate(languages)

print(list(enumerate_prime))


# desestruturar (unpack)

for index, language in enumerate(['Python', 'Java']):
    print(f'{index} - {language}')
