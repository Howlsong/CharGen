def choose_class(stat1, stat2):
    """
    Select a D&D 5e class based on the two highest stats.
    
    Parameters:
    - stat1: Tuple containing the name and value of the highest stat (e.g., ('str', 18)).
    - stat2: Tuple containing the name and value of the second highest stat (e.g., ('dex', 16)).
    
    Returns:
    - A string representing the recommended D&D class.
    """
    # Unpack stat names
    top_stat, second_stat = stat1[0], stat2[0]

    # Dictionary mapping stat priorities to classes
    class_choices = {
        ("str", "con"): "Barbarian",
        ("str", "dex"): "Fighter",
        ("str", "wis"): "Cleric",
        ("str", "cha"): "Paladin",
        ("str", "int"): "Paladin",
        ("dex", "int"): "Rogue",
        ("dex", "wis"): "Monk",
        ("dex", "cha"): "Bard",
        ("dex", "con"): "Rogue",
        ("int", "wis"): "Wizard",
        ("int", "cha"): "Warlock",
        ("int", "con"): "Sorceror",
        ("wis", "cha"): "Druid",
        ("wis", "con"): "Cleric",
        ("cha", "con"): "Bard",
    }

    # Match the stats to a class
    # Use both (top_stat, second_stat) and (second_stat, top_stat) for flexibility
    chosen_class = (
        class_choices.get((top_stat, second_stat))
        or class_choices.get((second_stat, top_stat))
        or "Fighter"  # Default class if no match is found
    )

    return chosen_class