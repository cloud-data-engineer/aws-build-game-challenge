#!/usr/bin/env python3
"""
Test script to verify AWS CloudBurst initializes correctly.
"""

import sys
import os

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    # Import the game module
    import aws_cloudburst
    
    print("✅ Successfully imported aws_cloudburst module")
    
    # Test pygame initialization
    import pygame
    pygame.init()
    print(f"✅ Pygame initialized successfully (version {pygame.version.ver})")
    
    # Test game class instantiation
    game = aws_cloudburst.Game()
    print("✅ Game class instantiated successfully")
    
    # Test game state
    print(f"✅ Initial game state: {game.state}")
    print(f"✅ Screen resolution: {game.screen.get_size()}")
    print(f"✅ Initial lives: {game.lives}")
    print(f"✅ Initial level: {game.current_level}")
    print(f"✅ Number of blocks in level 1: {len(game.level.blocks)}")
    
    # Test ball physics
    ball = game.balls[0]
    print(f"✅ Ball initial position: ({ball.position.x:.1f}, {ball.position.y:.1f})")
    print(f"✅ Ball initial speed: {ball.speed}")
    
    # Test paddle
    paddle = game.paddle
    print(f"✅ Paddle position: ({paddle.position.x:.1f}, {paddle.position.y:.1f})")
    print(f"✅ Paddle size: {paddle.width}x{paddle.height}")
    
    # Test level generation
    level2 = aws_cloudburst.Level(2)
    print(f"✅ Level 2 generated with {len(level2.blocks)} blocks")
    
    # Test block types
    block_types = list(aws_cloudburst.BlockType)
    print(f"✅ Available block types: {len(block_types)}")
    
    # Test power-up types
    powerup_types = list(aws_cloudburst.PowerUpType)
    print(f"✅ Available power-up types: {len(powerup_types)}")
    
    # Test audio manager
    audio = aws_cloudburst.AudioManager()
    print(f"✅ Audio manager initialized (sounds enabled: {audio.sounds_enabled})")
    
    pygame.quit()
    print("\n🎮 AWS CloudBurst is ready to play!")
    print("Run: python aws_cloudburst.py")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error during testing: {e}")
    sys.exit(1)
