# Nikita Moseichuk - RPG Nested Dictionaries
# This program simulates an RPG scenario using nested dictionaries.
# It contains dictionaries for characters, inventory, and locations.
# Each dictionary item includes properties and descriptions.
# The program prints out each character with their descriptions, each inventory item with their descriptions,
# and each location with its description.

# Characters dictionary containing details of different characters
characters = {
    'hero': {
        'name': 'Hero',
        'class': 'Warrior',
        'level': 10,
        'health': 100,
        'attack': 20,
        'defense': 15
    },
    'villain': {
        'name': 'Villain',
        'class': 'Wizard',
        'level': 8,
        'health': 80,
        'attack': 25,
        'defense': 10
    }
}

# Locations dictionary containing details of different locations
locations = {
    'forest': {
        'name': 'Forest',
        'description': 'A dense forest with towering trees.',
        'enemies': ['goblin', 'wolf'],
        'loot': ['health potion', 'gold coin']
    },
    'cave': {
        'name': 'Cave',
        'description': 'A dark and damp cave with mysterious sounds echoing.',
        'enemies': ['spider', 'skeleton'],
        'loot': ['magic scroll', 'gemstone']
    }
}

# Inventory dictionary containing details of characters' inventories
inventory = {
    'hero': {
        'weapons': ['sword', 'shield'],
        'potions': {
            'health': 3,
            'mana': 2
        }
    },
    'villain': {
        'weapons': ['staff', 'spellbook'],
        'potions': {
            'health': 1,
            'mana': 4
        }
    }
}

# Printing each dictionary item separately with descriptions
print("Characters:")
for character, details in characters.items():
    print(f"{details['name']} ({details['class']}) - Level {details['level']}")
    print(f"Health: {details['health']}, Attack: {details['attack']}, Defense: {details['defense']}\n")

print("Locations:")
for location, details in locations.items():
    print(f"{details['name']}: {details['description']}")
    print(f"Enemies: {', '.join(details['enemies'])}")
    print(f"Loot: {', '.join(details['loot'])}\n")

print("Inventory:")
for character, items in inventory.items():
    print(f"{character.capitalize()}'s Inventory:")
    print("Weapons:", ', '.join(items['weapons']))
    print("Potions:")
    for potion, quantity in items['potions'].items():
        print(f"- {potion.capitalize()}: {quantity}")
    print()
