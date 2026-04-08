import statgen as sg
import namegen as ng
import classchoice as cc
import racechoice as rc
import moreinfo as mi

# My stats IRL
b=0
str=0
dex=0
con=0
int=0
wis=0
cha=0

# Initialize stats
stats_list = ["str", "dex", "con", "int", "wis", "cha"]
stats_values = []

# Generate and assign stats
for a in range(6):  # Loop through 6 times
    b = sg.gen_stat()  # Generate a stat
    stats_values.append(b)  # Append to the list

# Unpack the stats into variables
str, dex, con, int, wis, cha = stats_values

# Print the stats
print("str","dex","con","int","wis","cha")
print(str, dex, con, int, wis, cha)
print((str-10)//2,(dex-10)//2,(con-10)//2,(int-10)//2,(wis-10)//2,(cha-10)//2)

# Create a dictionary for stats
stats = {"str": str, "dex": dex, "con": con, "int": int, "wis": wis, "cha": cha}

# Find the two largest stats
sorted_stats = sorted(stats.items(), key=lambda item: item[1], reverse=True)
stat1 = sorted_stats[0]  # Largest stat
stat2 = sorted_stats[1]  # Second largest stat
charClass=cc.choose_class(stat1,stat2)

# Print the largest stats
print(charClass,sorted_stats[0],sorted_stats[1])

# Print race
race=rc.choose_race(charClass)
print(race)

char_info = mi.gen_info(charClass, race)
for stat, value in char_info.items():
    print(f"{stat}: {value}")

# Generate and print names
print(" ".join(ng.gen_names(4)))