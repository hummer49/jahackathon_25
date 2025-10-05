# game/missions.py

# A list of image paths for non-target moles
CIVILIAN_MOLES = [
    "assets/civilian_1.png",
    "assets/civilian_2.png",
    "assets/civilian_3.png",
    "assets/civilian_4.png",
    "assets/civilian_5.png",
    "assets/civilian_6.png",

]

# A dictionary defining the target for each level
TARGETS = {
    # Level 1 (index 0)
    0: {
        "name": "The Tycoon",
        "image_path": "assets/target_level_1.png",
        "hint": "Your target is known for his flashy top hat."
    },
    # Level 2 (index 1)
    1: {
        "name": "The Conspirator",
        "image_path": "assets/target_level_2.png",
        "hint": "Intel suggests the target wears thick glasses to hide his identity."
    },
    # Add more targets for levels 2, 3, etc.
    2: {
        "name": "The Veteran",
        "image_path": "assets/target_veteran.png",
        "hint": "He is never seen without his military-grade helmet."
    },
    # ...and so on
}