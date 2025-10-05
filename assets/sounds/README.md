# Sound Effects

This folder contains sound effect files for the Hit-A-Mole game.

## Current Sound Files

All sound files are in WAV format and are currently silent placeholder files. Replace them with actual sound effects for better gameplay experience:

- **`target_hit.wav`** - Played when player successfully hits a target mole
- **`civilian_hit.wav`** - Played when player accidentally hits a civilian mole  
- **`level_complete.wav`** - Played when player completes a level successfully
- **`level_start.wav`** - Played when starting a new mission/level
- **`game_over.wav`** - Played when player runs out of lives
- **`button_click.wav`** - Played for all UI button interactions

## Adding Real Sound Effects

To replace the placeholder sounds with actual audio:

1. Find or create appropriate sound effects in WAV format
2. Replace the corresponding files in this directory
3. Keep the same file names for automatic loading
4. Recommended: Keep sounds short (0.1-2 seconds) for responsive gameplay

## Technical Notes

- The SoundManager automatically loads all sound files on game startup
- Missing files will log warnings but won't crash the game  
- Sound can be toggled on/off via the SoundManager (future UI feature)
- All sounds use pygame.mixer for playback