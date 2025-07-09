#!/usr/bin/env python3
"""
Improved 30-Second AWS CloudBurst Demo
Shows all features with proper block destruction and visual effects
"""

import sys
import os
import time
import math
import random

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import aws_cloudburst
import pygame

def demo_30_seconds_improved():
    """Improved 30-second demo with proper feature showcase."""
    print("🎮 Starting Improved 30-Second AWS CloudBurst Demo...")
    print("🎯 Features: Proper block destruction, all power-ups, complete showcase")
    
    # Create game instance
    game = aws_cloudburst.Game()
    
    # Set up impressive demo scene
    game.paddle.position.x = 512
    game.paddle.position.y = 650
    game.score = 5000  # Start with some score
    game.lives = 3
    game.current_level = 2
    
    # Create multiple balls for dynamic action
    game.balls.clear()
    
    # Main ball with good trajectory
    main_ball = aws_cloudburst.Ball(512, 500, 280)
    main_ball.velocity.x = 180
    main_ball.velocity.y = -220
    game.balls.append(main_ball)
    
    # Second ball for multi-ball effect (will be added later)
    
    # Create strategic block arrangement for good destruction showcase
    game.level.blocks.clear()
    
    # Top rows - easier to hit blocks
    easy_blocks = [
        # Row 1 - Tier 1 blocks
        (aws_cloudburst.BlockType.S3, 200, 150),
        (aws_cloudburst.BlockType.LAMBDA, 320, 150),
        (aws_cloudburst.BlockType.CLOUDWATCH, 440, 150),
        (aws_cloudburst.BlockType.S3, 560, 150),
        (aws_cloudburst.BlockType.LAMBDA, 680, 150),
        (aws_cloudburst.BlockType.CLOUDWATCH, 800, 150),
        
        # Row 2 - Tier 2 blocks
        (aws_cloudburst.BlockType.EC2, 260, 200),
        (aws_cloudburst.BlockType.RDS, 380, 200),
        (aws_cloudburst.BlockType.API_GATEWAY, 500, 200),
        (aws_cloudburst.BlockType.EC2, 620, 200),
        (aws_cloudburst.BlockType.RDS, 740, 200),
        
        # Row 3 - Tier 3 blocks
        (aws_cloudburst.BlockType.EKS, 320, 250),
        (aws_cloudburst.BlockType.SAGEMAKER, 440, 250),
        (aws_cloudburst.BlockType.BEDROCK, 560, 250),
        (aws_cloudburst.BlockType.EKS, 680, 250),
        
        # Special blocks row
        (aws_cloudburst.BlockType.Q_DEVELOPER, 380, 300),
        (aws_cloudburst.BlockType.CLOUDFORMATION, 500, 300),
        (aws_cloudburst.BlockType.AUTO_SCALING, 620, 300),
    ]
    
    # Add all blocks
    for block_type, x, y in easy_blocks:
        block = aws_cloudburst.Block(x, y, block_type)
        game.level.blocks.append(block)
    
    # Prepare power-ups to drop during demo
    demo_powerups = []
    
    # Track demo phases
    blocks_destroyed = 0
    multi_ball_triggered = False
    power_ups_shown = False
    
    print("\n🎬 Recording improved 30-second demo...")
    print("   📊 Phase 1 (0-5s): AWS Branding & Setup")
    print("   🎮 Phase 2 (5-10s): Block Destruction Showcase")
    print("   ⚡ Phase 3 (10-15s): Power-ups & Multi-ball")
    print("   🏗️ Phase 4 (15-20s): Advanced Features")
    print("   🎯 Phase 5 (20-25s): Intense Action")
    print("   🏆 Phase 6 (25-30s): Final Showcase")
    
    start_time = time.time()
    frames = 0
    last_block_hit_time = 0
    
    while time.time() - start_time < 30.0:
        current_time = time.time() - start_time
        dt = game.clock.tick(60) / 1000.0
        frames += 1
        
        # Handle quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        # Determine current phase
        if current_time < 5.0:
            phase = "BRANDING"
            phase_color = aws_cloudburst.AWS_ORANGE
        elif current_time < 10.0:
            phase = "DESTRUCTION"
            phase_color = aws_cloudburst.AWS_RED
        elif current_time < 15.0:
            phase = "POWER-UPS"
            phase_color = (255, 215, 0)  # Gold
        elif current_time < 20.0:
            phase = "ADVANCED"
            phase_color = aws_cloudburst.AWS_GREEN
        elif current_time < 25.0:
            phase = "INTENSE"
            phase_color = (255, 100, 100)  # Bright red
        else:
            phase = "FINALE"
            phase_color = aws_cloudburst.AWS_WHITE
        
        # Smart paddle movement for optimal demo
        keys = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_a: False, pygame.K_d: False}
        
        if game.balls:
            # Intelligent paddle AI
            target_x = sum(ball.position.x for ball in game.balls) / len(game.balls)
            
            # Add some prediction for better ball catching
            avg_velocity_x = sum(ball.velocity.x for ball in game.balls) / len(game.balls)
            predicted_x = target_x + avg_velocity_x * 0.3
            
            if game.paddle.position.x < predicted_x - 40:
                keys[pygame.K_RIGHT] = True
            elif game.paddle.position.x > predicted_x + 40:
                keys[pygame.K_LEFT] = True
        
        game.paddle.update(dt, keys)
        
        # Update balls with enhanced collision
        for ball in game.balls[:]:
            ball.update(dt)
            
            # Remove balls that fall off screen and respawn if needed
            if ball.position.y > game.screen.get_height():
                game.balls.remove(ball)
                # Respawn ball for continuous demo
                if len(game.balls) == 0:
                    new_ball = aws_cloudburst.Ball(game.paddle.position.x, game.paddle.position.y - 30, 280)
                    new_ball.velocity.x = random.choice([-150, 150])
                    new_ball.velocity.y = -200
                    game.balls.append(new_ball)
            
            # Ball-paddle collision
            paddle_rect = game.paddle.get_rect()
            ball_rect = pygame.Rect(ball.position.x - ball.radius, ball.position.y - ball.radius,
                                  ball.radius * 2, ball.radius * 2)
            
            if ball_rect.colliderect(paddle_rect) and ball.velocity.y > 0:
                ball.bounce_off_paddle(game.paddle.position.x, game.paddle.width)
                game.audio.play_bounce()
            
            # Ball-block collision with PROPER destruction
            for block in game.level.blocks[:]:
                if not block.destroyed and ball_rect.colliderect(block.get_rect()):
                    # Collision response
                    block_rect = block.get_rect()
                    if abs(ball.position.x - block_rect.centerx) > abs(ball.position.y - block_rect.centery):
                        ball.velocity.x = -ball.velocity.x
                    else:
                        ball.velocity.y = -ball.velocity.y
                    
                    # ALWAYS destroy blocks for demo (make it visually impressive)
                    points, destroyed = block.hit()
                    if not destroyed and current_time > 3.0:  # After branding phase
                        # Force destruction for demo purposes
                        block.hits_remaining = 0
                        block.destroyed = True
                        destroyed = True
                        points = block.points
                    
                    if points > 0:
                        game.score += points * max(1, game.score_multiplier)
                        game.audio.play_block_hit()
                        blocks_destroyed += 1
                        last_block_hit_time = current_time
                        
                        # Trigger special effects based on block type
                        if block.block_type == aws_cloudburst.BlockType.Q_DEVELOPER and not multi_ball_triggered:
                            # Add second ball for multi-ball effect
                            second_ball = aws_cloudburst.Ball(ball.position.x + 50, ball.position.y, 250)
                            second_ball.velocity.x = -ball.velocity.x * 0.8
                            second_ball.velocity.y = ball.velocity.y * 0.9
                            game.balls.append(second_ball)
                            multi_ball_triggered = True
                            
                            # Activate multi-ball power-up
                            game.active_powerups[aws_cloudburst.PowerUpType.MULTI_BALL] = 15.0
                        
                        # Drop power-ups from tier 2+ blocks
                        if block.block_type.value[1] >= 2 and len(demo_powerups) < 3:
                            powerup_types = [
                                aws_cloudburst.PowerUpType.PADDLE_EXTEND,
                                aws_cloudburst.PowerUpType.SCORE_MULTIPLIER,
                                aws_cloudburst.PowerUpType.SLOW_MOTION
                            ]
                            powerup_type = random.choice(powerup_types)
                            powerup = aws_cloudburst.PowerUp(block.position.x, block.position.y, powerup_type)
                            demo_powerups.append(powerup)
                    
                    break
        
        # Update demo power-ups
        for powerup in demo_powerups[:]:
            powerup.update(dt)
            
            if powerup.collected or powerup.position.y > game.screen.get_height():
                demo_powerups.remove(powerup)
                continue
            
            # Auto-collect power-ups for demo
            paddle_rect = game.paddle.get_rect()
            if powerup.get_rect().colliderect(paddle_rect):
                game._activate_powerup(powerup.powerup_type)
                demo_powerups.remove(powerup)
                game.audio.play_powerup()
                power_ups_shown = True
        
        # Activate power-ups at specific times for demo
        if current_time > 8.0 and not game.paddle.extended:
            game.active_powerups[aws_cloudburst.PowerUpType.PADDLE_EXTEND] = 15.0
            game.paddle.extended = True
            game.paddle.width = 180
        
        if current_time > 12.0 and game.score_multiplier == 1:
            game.active_powerups[aws_cloudburst.PowerUpType.SCORE_MULTIPLIER] = 12.0
            game.score_multiplier = 2
        
        # Update active power-up timers
        for powerup_type in aws_cloudburst.PowerUpType:
            if game.active_powerups[powerup_type] > 0:
                game.active_powerups[powerup_type] -= dt
                if game.active_powerups[powerup_type] <= 0:
                    game._deactivate_powerup(powerup_type)
        
        # Add more balls for intense action phase
        if current_time > 20.0 and len(game.balls) < 3:
            extra_ball = aws_cloudburst.Ball(400 + random.randint(-100, 100), 400, 260)
            extra_ball.velocity.x = random.choice([-180, 180])
            extra_ball.velocity.y = -180
            game.balls.append(extra_ball)
        
        # Draw everything
        game._draw_background()
        
        # Dynamic title based on phase
        title_font = pygame.font.Font(None, 52)
        title_text = title_font.render("AWS CloudBurst - Complete Demo", True, aws_cloudburst.AWS_ORANGE)
        title_rect = title_text.get_rect(center=(512, 30))
        game.screen.blit(title_text, title_rect)
        
        # Phase indicator
        phase_font = pygame.font.Font(None, 24)
        phase_text = phase_font.render(f"Phase: {phase}", True, phase_color)
        phase_rect = phase_text.get_rect(center=(512, 60))
        game.screen.blit(phase_text, phase_rect)
        
        # Draw all game elements
        for block in game.level.blocks:
            if not block.destroyed:
                block.draw(game.screen)
        
        for ball in game.balls:
            ball.draw(game.screen)
        
        game.paddle.draw(game.screen)
        
        for powerup in demo_powerups:
            powerup.draw(game.screen)
        
        # Enhanced HUD
        game.ui.draw_hud(game.screen, game.score, game.lives, game.current_level, game.active_powerups)
        
        # Phase-specific information
        info_font = pygame.font.Font(None, 18)
        
        if phase == "BRANDING":
            info_lines = [
                "🎨 Professional AWS Visual Identity",
                "🏀 Q Developer Ball with AI Branding",
                "🏓 AWS Smile Curve Paddle",
                "🧱 12 Authentic Service Icons"
            ]
        elif phase == "DESTRUCTION":
            info_lines = [
                f"💥 Blocks Destroyed: {blocks_destroyed}",
                "🎯 Realistic Physics & Collision",
                "🔊 Audio Feedback System",
                "⚡ Smooth 60 FPS Performance"
            ]
        elif phase == "POWER-UPS":
            info_lines = [
                "⚡ AWS-Themed Power-ups Active",
                "🔄 Multi-Ball Effect Triggered",
                "📊 Visual Effect Indicators",
                "⏱️ Timed Enhancement System"
            ]
        elif phase == "ADVANCED":
            info_lines = [
                "🏗️ AWS Architecture Learning",
                "📚 Service Recognition System",
                "🎓 Educational Integration",
                "💡 Professional Training Tool"
            ]
        elif phase == "INTENSE":
            info_lines = [
                f"🚀 Score: {game.score:,} Points",
                f"⚡ {len(game.balls)} Balls Active",
                "🔥 Maximum Action Mode",
                "🎮 Peak Performance Demo"
            ]
        else:  # FINALE
            info_lines = [
                "🏆 Complete Gaming Experience",
                "📈 Achievement System Ready",
                "📋 Full Menu & Help System",
                "✨ Production Quality Polish"
            ]
        
        y_offset = 90
        for info in info_lines:
            info_text = info_font.render(info, True, aws_cloudburst.AWS_WHITE)
            game.screen.blit(info_text, (30, y_offset))
            y_offset += 22
        
        # Statistics panel
        stats_font = pygame.font.Font(None, 16)
        stats = [
            f"Time: {current_time:.1f}s / 30.0s",
            f"Blocks Destroyed: {blocks_destroyed}",
            f"Active Balls: {len(game.balls)}",
            f"Score Multiplier: {game.score_multiplier}x",
            f"Power-ups Active: {sum(1 for v in game.active_powerups.values() if v > 0)}"
        ]
        
        y_offset = 90
        for stat in stats:
            stat_text = stats_font.render(stat, True, aws_cloudburst.AWS_LIGHT_GRAY)
            game.screen.blit(stat_text, (750, y_offset))
            y_offset += 18
        
        # Progress bar
        progress = current_time / 30.0
        bar_width = 600
        bar_height = 15
        bar_x = (1024 - bar_width) // 2
        bar_y = 730
        
        # Background
        pygame.draw.rect(game.screen, aws_cloudburst.AWS_DARK_BLUE, (bar_x, bar_y, bar_width, bar_height))
        # Progress
        pygame.draw.rect(game.screen, phase_color, (bar_x, bar_y, int(bar_width * progress), bar_height))
        # Border
        pygame.draw.rect(game.screen, aws_cloudburst.AWS_WHITE, (bar_x, bar_y, bar_width, bar_height), 2)
        
        # Timer
        timer_text = info_font.render(f"{30.0 - current_time:.1f}s remaining", True, aws_cloudburst.AWS_WHITE)
        game.screen.blit(timer_text, (bar_x + bar_width + 15, bar_y - 2))
        
        pygame.display.flip()
    
    print(f"\n✅ Improved demo completed! {frames} frames at {frames/30.0:.1f} FPS")
    print(f"📊 Demo Statistics:")
    print(f"   • Blocks Destroyed: {blocks_destroyed}")
    print(f"   • Final Score: {game.score:,}")
    print(f"   • Multi-ball Triggered: {'Yes' if multi_ball_triggered else 'No'}")
    print(f"   • Power-ups Shown: {'Yes' if power_ups_shown else 'No'}")
    print(f"   • Max Balls Active: {len(game.balls)}")
    
    pygame.quit()
    print("\n🎬 Improved 30-Second Demo Complete!")
    print("🚀 All features properly showcased with visual block destruction!")

if __name__ == "__main__":
    try:
        demo_30_seconds_improved()
    except KeyboardInterrupt:
        print("\n⏹️  Demo interrupted by user")
        pygame.quit()
    except Exception as e:
        print(f"❌ Demo error: {e}")
        pygame.quit()
        sys.exit(1)
