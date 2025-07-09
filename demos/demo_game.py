#!/usr/bin/env python3
"""
Demo script for AWS CloudBurst - shows the game running for a few seconds.
"""

import sys
import os
import time

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import aws_cloudburst
import pygame

def demo_game():
    """Run a brief demo of the game."""
    print("🎮 Starting AWS CloudBurst Demo...")
    
    # Create game instance
    game = aws_cloudburst.Game()
    
    # Start the game
    game._start_new_game()
    
    print("📊 Game Statistics:")
    print(f"   • Resolution: {game.screen.get_size()}")
    print(f"   • Initial Lives: {game.lives}")
    print(f"   • Level 1 Blocks: {len(game.level.blocks)}")
    print(f"   • Ball Speed: {game.balls[0].speed} px/s")
    print(f"   • Paddle Size: {game.paddle.width}x{game.paddle.height}")
    
    # Show block types in level 1
    block_types = {}
    for block in game.level.blocks:
        block_name = block.block_type.value[0]
        block_types[block_name] = block_types.get(block_name, 0) + 1
    
    print("\n🧱 Level 1 AWS Services:")
    for service, count in block_types.items():
        print(f"   • {service}: {count} blocks")
    
    # Show available power-ups
    print("\n⚡ Available Power-ups:")
    for powerup in aws_cloudburst.PowerUpType:
        name, duration, color = powerup.value
        print(f"   • {name}: {duration}s duration")
    
    # Run a brief simulation
    print("\n🎯 Running 5-second simulation...")
    
    start_time = time.time()
    frames = 0
    
    # Simulate game loop for 5 seconds
    while time.time() - start_time < 5.0 and game.running:
        dt = game.clock.tick(60) / 1000.0
        frames += 1
        
        # Handle events (just quit events)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
        
        # Update game
        if game.state == aws_cloudburst.GameState.PLAYING:
            # Simulate some paddle movement
            keys = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_a: False, pygame.K_d: False}
            if frames % 120 < 60:  # Move right for 1 second, then left
                keys[pygame.K_RIGHT] = True
            else:
                keys[pygame.K_LEFT] = True
            
            game.paddle.update(dt, keys)
            
            # Update balls
            for ball in game.balls:
                ball.update(dt)
        
        # Draw everything
        game._draw_game()
        pygame.display.flip()
    
    print(f"✅ Demo completed! Rendered {frames} frames")
    print(f"   • Average FPS: {frames / 5.0:.1f}")
    print(f"   • Ball position: ({game.balls[0].position.x:.1f}, {game.balls[0].position.y:.1f})")
    print(f"   • Paddle position: ({game.paddle.position.x:.1f}, {game.paddle.position.y:.1f})")
    
    pygame.quit()
    print("\n🎮 AWS CloudBurst Demo Complete!")
    print("To play the full game, run: python aws_cloudburst.py")

if __name__ == "__main__":
    try:
        demo_game()
    except KeyboardInterrupt:
        print("\n⏹️  Demo interrupted by user")
        pygame.quit()
    except Exception as e:
        print(f"❌ Demo error: {e}")
        pygame.quit()
        sys.exit(1)
