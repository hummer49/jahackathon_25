import pygame
import os
import logging

logger = logging.getLogger(__name__)

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}
        self.sound_enabled = True
        
        # Define sound file paths
        self.sound_files = {
            'button_click': 'assets/sounds/1_computer-mouse-click.mp3',
            'civilian_hit': 'assets/sounds/2_hit_civilian_wrong.mp3',
            'game_over': 'assets/sounds/3_game-over-sound-effect-331435.mp3',
            'target_hit': 'assets/sounds/4_correct-choice.mp3',
            'level_complete': 'assets/sounds/5_level_complete.mp3',
            'level_start': 'assets/sounds/6_level_start.mp3',
            'typing': 'assets/sounds/7_keyboard-typing-sound-effect.mp3',
        }
        
        self.load_sounds()
    
    def load_sounds(self):
        """Load all sound files with fallback handling"""
        logger.info(f"Loading {len(self.sound_files)} sound files...")
        loaded_count = 0
        for sound_name, file_path in self.sound_files.items():
            try:
                if os.path.exists(file_path):
                    self.sounds[sound_name] = pygame.mixer.Sound(file_path)
                    logger.info(f"✅ Loaded sound: '{sound_name}' from {file_path}")
                    loaded_count += 1
                else:
                    logger.warning(f"❌ Sound file not found: {file_path}")
                    self.sounds[sound_name] = None
            except pygame.error as e:
                logger.warning(f"❌ Failed to load sound '{sound_name}': {e}")
                self.sounds[sound_name] = None
        logger.info(f"Sound loading complete: {loaded_count}/{len(self.sound_files)} sounds loaded successfully")
    
    def play_sound(self, sound_name):
        """Play a sound effect if available and enabled"""
        if not self.sound_enabled:
            logger.info(f"Sound '{sound_name}' requested but audio is disabled")
            return
            
        if sound_name in self.sounds and self.sounds[sound_name]:
            try:
                self.sounds[sound_name].play()
                logger.info(f"🔊 Playing sound: '{sound_name}'")
            except pygame.error as e:
                logger.warning(f"Failed to play sound {sound_name}: {e}")
        else:
            logger.warning(f"Sound '{sound_name}' not found or not loaded")
    
    def toggle_sound(self):
        """Toggle sound on/off"""
        self.sound_enabled = not self.sound_enabled
        status = "🔊 ENABLED" if self.sound_enabled else "🔇 DISABLED"
        logger.info(f"Sound system {status}")
    
    def set_volume(self, volume):
        """Set volume for all sounds (0.0 to 1.0)"""
        for sound in self.sounds.values():
            if sound:
                sound.set_volume(volume)