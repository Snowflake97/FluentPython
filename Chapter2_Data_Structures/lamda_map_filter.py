example_string = "aAzZ"

onlySmallLetters = list(map(chr, list(filter(lambda x: x >= 97 and x <= 122, map(ord, example_string)))))

print(onlySmallLetters)