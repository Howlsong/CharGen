import random

# Predefined list of common languages in D&D 5e
all_languages = [
    "Common", "Elvish", "Dwarvish", "Draconic", "Giant", "Goblin", 
    "Halfling", "Orc", "Infernal", "Celestial", "Sylvan", "Abyssal", 
    "Primordial", "Gnomish", "Aquan", "Terran", "Ignan", "Celestial", 
    "Fey", "Undercommon", "Deep Speech", "Thieves' Cant"
]

# Function to generate languages based on race and class
def gen_langs(race, char_class):
    # Default languages based on race
    race_languages = {
        "Human": ["Common"],
        "Elf": ["Common", "Elvish"],
        "Dwarf": ["Common", "Dwarvish"],
        "Half-Elf": ["Common", "Elvish", "Sylvan"],
        "Dragonborn": ["Common", "Draconic"],
        "Halfling": ["Common", "Halfling"],
        "Gnome": ["Common", "Gnomish"],
        "Tiefling": ["Common", "Infernal"],
        "Half-Orc": ["Common", "Orc"],
        "Aasimar": ["Common", "Celestial"],
        "Firbolg": ["Common", "Sylvan"],
        "Satyr": ["Common", "Sylvan"],
        "Goliath": ["Common", "Giant"]
    }
    
    # Default languages based on class (usually 1 extra language)
    class_languages = {
        "Wizard": 1,
        "Sorcerer": 1,
        "Cleric": 1,
        "Bard": 2,
        "Druid": 1,
        "Ranger": 1,
        "Paladin": 1,
        "Warlock": 1,
        "Fighter": 0,
        "Monk": 0,
        "Rogue": 1
    }
    
    # Start with the race's languages
    languages = race_languages.get(race, ["Common"])  # Default to "Common" if race not found

    # Add extra languages based on class
    extra_languages = class_languages.get(char_class, 0)
    
    # Randomly pick extra languages if necessary
    for _ in range(extra_languages):
        available_languages = list(set(all_languages) - set(languages))  # Remove already chosen languages
        new_language = random.choice(available_languages)
        languages.append(new_language)
    
    # Make sure to return the final list of languages
    return languages