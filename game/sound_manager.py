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
        }
        
        self.load_sounds()
    
    def load_sounds(self):
        """Load all sound files with fallback handling"""
        for sound_name, file_path in self.sound_files.items():
            try:
                if os.path.exists(file_path):
                    self.sounds[sound_name] = pygame.mixer.Sound(file_path)
                    logger.debug(f"Loaded sound: {sound_name}")
                else:
                    logger.warning(f"Sound file not found: {file_path}")
                    self.sounds[sound_name] = None
            except pygame.error as e:
                logger.warning(f"Failed to load sound {sound_name}: {e}")
                self.sounds[sound_name] = None
    
    def play_sound(self, sound_name):
        """Play a sound effect if available and enabled"""
        if not self.sound_enabled:
            return
            
        if sound_name in self.sounds and self.sounds[sound_name]:
            try:
                self.sounds[sound_name].play()
                logger.debug(f"Played sound: {sound_name}")
            except pygame.error as e:
                logger.warning(f"Failed to play sound {sound_name}: {e}")
    
    def toggle_sound(self):
        """Toggle sound on/off"""
        self.sound_enabled = not self.sound_enabled
        logger.info(f"Sound {'enabled' if self.sound_enabled else 'disabled'}")
    
    def set_volume(self, volume):
        """Set volume for all sounds (0.0 to 1.0)"""
        for sound in self.sounds.values():
            if sound:
                sound.set_volume(volume)