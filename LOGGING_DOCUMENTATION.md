# Game Logging System Documentation

## Overview
This document describes the comprehensive logging system added to the Hit-a-Mole game to track key player events and gameplay metrics for developers.

## Logging Configuration

The logging system is configured in `app.py` with the following features:

- **Log Level**: INFO (captures all important gameplay events)
- **Format**: `%(asctime)s - %(levelname)s - %(message)s`
- **Output**: 
  - Console output (for real-time monitoring)
  - Log file: `game_events.log` (for persistent storage)

## Tracked Events

### 1. Target Hit Events
**Event**: When a player successfully hits a target mole
**Log Message**: `TARGET HIT! Player hit target mole '{target_name}' in level {level_number}`
**Location**: `app.py` - when `active_mole.mole_type == 'target'`

### 2. Score Events  
**Event**: When a player earns points
**Log Message**: `SCORE EARNED! Player scored 1 point. Total score: {total_score}`
**Location**: `app.py` - immediately after target hit

### 3. Turn Used Events
**Event**: When a player uses a turn (loses a life)
**Scenarios**:
- Hitting a civilian: `TURN USED! Player hit civilian mole in level {level}. Lives remaining: {lives}`
- Missing the target: `TURN USED! Player missed target in level {level}. Lives remaining: {lives}`
**Location**: `app.py` - in civilian hit and miss logic

### 4. Level Pass Events
**Event**: When a player completes a level
**Log Message**: `LEVEL PASSED! Player completed level {level} ({theme_name}) with {hits}/{required_hits} hits`
**Location**: `app.py` - when `current_level.is_complete()` returns True

## Additional Tracked Events

### Game Lifecycle
- **New Game Start**: `NEW GAME STARTED! Player '{player_name}' starting level 1 with {starting_lives} lives`
- **Mission Start**: `MISSION STARTED! Level {level} ({theme_name}) - Target: '{target_name}'`
- **Game Over**: `GAME OVER! Player ran out of lives in level {level}. Final score: {score}`
- **Game Won**: `GAME WON! Player completed all {max_levels} levels with final score: {score}`

### Player Actions
- **Hint Usage**: `HINT USED! Player used hint in level {level}. Hints remaining: {remaining}`
- **Level Progression**: `NEXT LEVEL! Player proceeding to level {next_level} ({theme_name})`

### Debug Events (Level: DEBUG)
- Hit count increments: `Level {level}: Hit count increased to {hits}/{required}`
- Life loss: `Level {level}: Life lost. Lives remaining: {lives}`
- Hint attempts: `Player '{name}' used/attempted to use a hint`

## File Locations

### Primary Implementation
- `app.py` - Main logging configuration and gameplay event logging
- `game/player.py` - Player action logging (hints, score tracking)
- `game/level.py` - Level state change logging

### Log Output
- **Console**: Real-time logging output visible during gameplay
- **File**: `game_events.log` - Persistent log file created in the game directory

## Usage for Developers

### Monitoring Live Gameplay
```bash
# Watch the log file in real-time
tail -f game_events.log

# Filter for specific events
grep "TARGET HIT" game_events.log
grep "LEVEL PASSED" game_events.log
grep "SCORE EARNED" game_events.log
```

### Analytics Queries
```bash
# Count target hits
grep -c "TARGET HIT" game_events.log

# Count games played
grep -c "NEW GAME STARTED" game_events.log

# Count levels completed
grep -c "LEVEL PASSED" game_events.log

# See final scores
grep "GAME WON\|GAME OVER" game_events.log
```

### Testing the Logging System
Run the test script to verify logging functionality:
```bash
python test_logging.py
```

## Log Message Format Examples

```
2025-10-05 16:06:35,172 - INFO - NEW GAME STARTED! Player 'Agent 48' starting level 1 with 3 lives
2025-10-05 16:06:35,172 - INFO - MISSION STARTED! Level 1 (School Infiltration) - Target: 'The Corporate Spy'
2025-10-05 16:06:35,172 - INFO - TARGET HIT! Player hit target mole 'The Corporate Spy' in level 1
2025-10-05 16:06:35,172 - INFO - SCORE EARNED! Player scored 1 point. Total score: 1
2025-10-05 16:06:35,173 - INFO - TURN USED! Player missed target in level 1. Lives remaining: 2
2025-10-05 16:06:35,173 - INFO - HINT USED! Player used hint in level 1. Hints remaining: 2
2025-10-05 16:06:35,173 - INFO - LEVEL PASSED! Player completed level 1 (School Infiltration) with 3/3 hits
```

## Benefits for Developers

1. **Player Behavior Analysis**: Track how players interact with the game
2. **Difficulty Assessment**: Monitor success/failure rates per level  
3. **Performance Metrics**: Measure completion rates and score distributions
4. **Bug Detection**: Identify unusual gameplay patterns or issues
5. **Feature Usage**: Track hint usage and other game features
6. **Balancing**: Data-driven game balancing decisions

## Configuration Options

The logging can be customized by modifying the `logging.basicConfig()` call in `app.py`:

- Change log level: `level=logging.DEBUG` for more verbose output
- Modify format: Adjust the format string for different timestamp/message formats
- Add file rotation: Use `RotatingFileHandler` for large log files
- Filter by logger: Use specific loggers for different game components

## Future Enhancements

Consider adding logging for:
- Mouse click coordinates and timing
- Round completion times  
- Player reaction times
- Menu navigation patterns
- Settings changes
- Performance metrics (FPS, memory usage)