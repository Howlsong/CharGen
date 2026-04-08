import random
vowels = ["a", "e", "i", "o", "u"]
consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

def gen_name():
    name = []
    for _ in range(random.randint(3,7)):
        if len(name) >= 2:
            if name[-1] in vowels and name[-2] in vowels:
                name.append(random.choice(consonants))
            elif name[-1] in consonants and name[-2] in consonants:
                name.append(random.choice(vowels))
            else:
                name.append(random.choice(vowels + consonants))
        else:
            name.append(random.choice(vowels + consonants))
    return ''.join(name).capitalize()

def gen_names(N):
    names = []
    for _ in range(N):
        names.append(gen_name())
    return names
#generated_names = gen_names(int(input(">>> ")))
#for item in generated_names:
#    print(item)