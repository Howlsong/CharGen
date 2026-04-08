import random
import languages as lang

def gen_info(dnd_class, race="Human"):
    """
    Generates various stats for a D&D 5e character at level 1.
    
    Parameters:
    - dnd_class: The D&D class of the character (e.g., "Barbarian", "Wizard").
    - race: The race of the character (default is "Human").
    
    Returns:
    - A dictionary with the generated stats.
    """
    
    # Base hit points (HP) at level 1
    hit_dice = {
        "Barbarian": 12, "Fighter": 10, "Monk": 8, "Rogue": 8, "Bard": 8,
        "Cleric": 8, "Paladin": 10, "Ranger": 10, "Warlock": 8, "Wizard": 6,
        "Druid": 8, "Sorcerer": 6
    }
    
    # Spell slots at level 1
    spell_slots = {
        "Cleric": 2, "Druid": 2, "Sorcerer": 2, "Warlock": 2, "Wizard": 3,
        "Bard": 2, "Paladin": 0, "Barbarian": 0, "Fighter": 0, "Monk": 0,
        "Rogue": 0, "Ranger": 0
    }

    # Proficiencies based on class
    proficiencies = {
        "Barbarian": 3, "Fighter": 3, "Monk": 3, "Rogue": 4, "Bard": 4,
        "Cleric": 3, "Paladin": 4, "Ranger": 3, "Warlock": 2, "Wizard": 2,
        "Druid": 2, "Sorcerer": 2
    }

    # Movement Speed based on race (default to Human 30 feet)
    race_speeds = {
    "Human": 30, "Elf": 30, "Dwarf": 25, "Halfling": 25,
    "Gnome": 25, "Half-Elf": 30, "Half-Orc": 30, "Tiefling": 30, "Dragonborn": 30,
    "Wood Elf": 35, "Lightfoot Halfling": 25, "High Elf": 30, "Aasimar": 30,
    "Satyr": 40, "Firbolg": 30, "Goliath": 30
    }
    
    # Possible alignments
    alignments = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", 
                  "True Neutral", "Chaotic Neutral", "Lawful Evil", "Neutral Evil", "Chaotic Evil"]
    
    # Calculate Hit Points (HP)
    hd = hit_dice.get(dnd_class, 8)
    
    # Get number of spell slots for the class (default to 0 if none)
    spell_slots_count = spell_slots.get(dnd_class, 0)
    
    # Get number of proficiencies for the class
    proficiency_count = proficiencies.get(dnd_class, 2)
    
    # Movement Speed (based on race, default 30 feet for Human)
    movement_speed = race_speeds.get(race, 30)
    
    # Randomly select alignment
    alignment = random.choice(alignments)
    
    # Randomly select languages
    languages = " ".join(lang.gen_langs(race,dnd_class))
    
    # Compile the information
    character_info = {
        "Hit Die": hd,
        "Spell Slots at Level 1": spell_slots_count,
        "Proficiencies": proficiency_count,
        "Movement Speed": movement_speed,
        "Alignment": alignment,
        "Known Languages": languages
        }
    
    return character_info