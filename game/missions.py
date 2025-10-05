# game/missions.py

# Level themes with background-civilian-target relationships
LEVEL_THEMES = {
    0: {
        "name": "School Infiltration",
        "background_image": "assets/backgrounds/school_classroom.png", # OK
        "civilian_images": [
            "assets/moles/school/student_1.png",
            "assets/moles/school/student_2.png", 
            "assets/moles/school/teacher_1.png",
            "assets/moles/school/student_3.png", # OK
        ],
        "target": {
            "name": "The Corporate Spy",
            "image_path": "assets/moles/targets/businessman_suit.png",  # Doesn't fit school
            "hint": "He's overdressed for a classroom environment." #OK
        }
    },
    1: {
        "name": "Hospital Operation", 
        "background_image": "assets/backgrounds/hospital_ward.png", # OK
        "civilian_images": [
            "assets/moles/hospital/doctor_1.png",
            "assets/moles/hospital/nurse_1.png",
            "assets/moles/hospital/patient_1.png",
            "assets/moles/hospital/doctor_2.png", # OK
        ],
        "target": {
            "name": "The Street Thug",
            "image_path": "assets/moles/targets/gang_member.png",  # Doesn't fit hospital # OK
            "hint": "His tattoos and leather jacket seem out of place here."
        }
    },
    2: {
        "name": "Office Building",
        "background_image": "assets/backgrounds/corporate_office.png", 
        "civilian_images": [
            "assets/moles/office/manager_1.png",
            "assets/moles/office/secretary_1.png",
            "assets/moles/office/businessman_1.png",
            "assets/moles/office/executive_1.png",
        ],
        "target": {
            "name": "The Beach Bum",
            "image_path": "assets/moles/targets/surfer_casual.png",  # Doesn't fit office
            "hint": "His flip-flops and hawaiian shirt don't match the dress code."
        }
    },
    3: {
        "name": "Fine Dining Restaurant",
        "background_image": "assets/backgrounds/restaurant_kitchen.png",
        "civilian_images": [
            "assets/moles/restaurant/chef_1.png",
            "assets/moles/restaurant/cook_1.png",
            "assets/moles/restaurant/waiter_1.png",
            "assets/moles/restaurant/manager_1.png",
        ],
        "target": {
            "name": "The Construction Worker",
            "image_path": "assets/moles/targets/samurai.png",  # Doesn't fit restaurant
            "hint": "His hard hat and work boots are very out of place here."
        }
    }
}

# Backward compatibility - convert to old TARGETS format
TARGETS = {level: theme["target"] for level, theme in LEVEL_THEMES.items()}

# Legacy CIVILIAN_MOLES kept for backward compatibility (though now unused)
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
        "name": "The Tycoon",
        "image_path": "assets/target_level_1.png",
        "hint": "Your target is known for his flashy top hat."
    },
    3: {
        "name": "The Tycoon",
        "image_path": "assets/target_level_1.png",
        "hint": "Your target is known for his flashy top hat."
    },
    4: {
        "name": "The Tycoon",
        "image_path": "assets/target_level_1.png",
        "hint": "Your target is known for his flashy top hat."
    },
}