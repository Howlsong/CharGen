import random
def choose_race(dnd_class):
    """
    Choose a race based on the given D&D class.
    """
    race_choices = {
        "Barbarian": ["Half-Orc", "Dwarf", "Goliath"],
        "Fighter": ["Human", "Half-Elf", "Dwarf", "Half-Orc"],
        "Monk": ["Wood Elf", "Human", "Halfling", "Half-Elf"],
        "Rogue": ["Halfling", "Lightfoot Halfling", "Wood Elf", "Human"],
        "Bard": ["Half-Elf", "Tiefling", "Human", "Satyr", "Gnome"],
        "Cleric": ["Dwarf", "Human", "Aasimar", "Half-Elf"],
        "Paladin": ["Human", "Half-Elf", "Dragonborn", "Tiefling", "Dwarf"],
        "Ranger": ["Wood Elf", "Human", "Half-Elf", "Halfling", "Half-Orc"],
        "Warlock": ["Tiefling", "Half-Elf", "Human", "Half-Orc"],
        "Wizard": ["High Elf", "Human", "Gnome", "Tiefling", "Half-Elf"],
        "Druid": ["Wood Elf", "Firbolg", "Human", "Halfling"],
        "Sorcerer": ["Dragonborn", "Tiefling", "Human", "Half-Elf"],
    }
    
    # Return the recommended races for the given class
    race = race_choices.get(dnd_class, ["No valid races found for this class"])[random.randint(0,len(race_choices.get(dnd_class))-1)]
    if race == "Human":
        race = race_choices.get(dnd_class, ["No valid races found for this class"])[random.randint(0,len(race_choices.get(dnd_class))-1)]
    return race