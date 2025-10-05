# Asset Management Guide

This document explains how to manage game assets for the Level-MoleImage-BackgroundImage relationship system.

## Current Asset Structure

```
assets/
├── backgrounds/           # Background images for level themes
│   ├── school_classroom.png
│   ├── hospital_ward.png
│   ├── corporate_office.png
│   └── restaurant_kitchen.png
├── moles/
│   ├── school/           # School theme civilian moles
│   │   ├── student_1.png
│   │   ├── student_2.png
│   │   ├── student_3.png
│   │   └── teacher_1.png
│   ├── hospital/         # Hospital theme civilian moles
│   │   ├── doctor_1.png
│   │   ├── doctor_2.png
│   │   ├── nurse_1.png
│   │   └── patient_1.png
│   ├── office/           # Office theme civilian moles
│   │   ├── manager_1.png
│   │   ├── secretary_1.png
│   │   ├── businessman_1.png
│   │   └── executive_1.png
│   ├── restaurant/       # Restaurant theme civilian moles
│   │   ├── chef_1.png
│   │   ├── cook_1.png
│   │   ├── waiter_1.png
│   │   └── manager_1.png
│   └── targets/          # Target moles (don't fit environments)
│       ├── businessman_suit.png
│       ├── gang_member.png
│       ├── surfer_casual.png
│       └── construction_worker.png
└── [legacy files]        # Old asset structure (kept for backward compatibility)
    ├── base.png
    ├── civilian_1.png - civilian_6.png
    ├── target_level_1.png
    └── target_level_2.png
```

## Design Philosophy

Each level creates a **"spot the impostor"** gameplay experience:

1. **Background**: Sets the environmental context
2. **Civilian Moles**: People who naturally belong in that environment
3. **Target Mole**: Someone who obviously doesn't fit the environment

### Level Themes

| Level | Theme | Civilians Fit | Target Doesn't Fit |
|-------|-------|---------------|-------------------|
| 1 | School | Students, Teachers | Businessman in suit |
| 2 | Hospital | Doctors, Nurses, Patients | Street gang member |
| 3 | Office | Managers, Executives | Beach surfer |
| 4 | Restaurant | Chefs, Servers | Construction worker |

## Adding New Levels

To add a new level theme:

### 1. Create Asset Folders
```bash
mkdir assets/moles/[theme_name]
```

### 2. Update `game/missions.py`
```python
LEVEL_THEMES = {
    # ... existing levels ...
    4: {
        "name": "New Theme Name",
        "background_image": "assets/backgrounds/new_theme.png",
        "civilian_images": [
            "assets/moles/new_theme/civilian_1.png",
            "assets/moles/new_theme/civilian_2.png",
            # ... more civilians
        ],
        "target": {
            "name": "The Target Name", 
            "image_path": "assets/moles/targets/new_target.png",
            "hint": "Describe what makes them stand out."
        }
    }
}
```

### 3. Add Image Files
- **Background**: `assets/backgrounds/new_theme.png` (800x600 recommended)
- **Civilians**: `assets/moles/new_theme/civilian_*.png` 
- **Target**: `assets/moles/targets/new_target.png`

## Image Requirements

### Technical Specs
- **Format**: PNG with transparency support
- **Background Size**: Match game window (800x600 default)
- **Mole Images**: Any size (automatically scaled and cropped to circles)

### Design Guidelines
- **Civilians**: Should visually belong in the environment
- **Targets**: Should obviously NOT belong (different clothing, style, context)
- **Backgrounds**: Should clearly establish the environment context
- **Style**: Consistent art style across all assets

## Error Handling

The game gracefully handles missing assets:

- **Missing Mole Images**: Shows red circles with warning messages
- **Missing Backgrounds**: Shows solid blue background with warning messages
- **Missing Theme Data**: Game exits with error message

Check the console for specific asset loading warnings during development.

## Backward Compatibility

The old asset structure is maintained for compatibility:
- `assets/civilian_*.png` files are kept but not used in new system
- `CIVILIAN_MOLES` list is maintained for legacy code
- `TARGETS` dictionary is auto-generated from `LEVEL_THEMES`

## Testing Assets

Run the game and check console for warnings like:
```
WARNING: Missing mole image asset 'assets/moles/school/student_1.png': [Errno 2] No such file or directory
         Using red circle fallback. Please add the missing image file.
```

This helps developers identify which assets need to be created.