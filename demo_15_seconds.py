#!/usr/bin/env python3
"""
15-Second Comprehensive Demo of AWS CloudBurst
Showcases all features: branding, gameplay, power-ups, and visual effects
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

def demo_15_seconds():
    """15-second comprehensive feature showcase."""
    print("🎮 Starting 15-Second AWS CloudBurst Feature Demo...")
    print("📺 Showcasing: Branding, Gameplay, Power-ups, Visual Effects")
    
    # Create game instance
    game = aws_cloudburst.Game()
    
    # Set up demo scene with enhanced visuals
    game.paddle.position.x = 512
    game.paddle.position.y = 650
    
    # Create multiple balls for visual impact
    game.balls.clear()
    for i in range(3):
        ball = aws_cloudburst.Ball(400 + i * 100, 500 - i * 50, 200)
        ball.velocity.x = 150 * (1 if i % 2 == 0 else -1)
        ball.velocity.y = -200 + i * 50
        game.balls.append(ball)
    
    # Create showcase blocks with all AWS services
    game.level.blocks.clear()
    showcase_services = [
        # Top row - Tier 1
        (aws_cloudburst.BlockType.S3, 200, 150),
        (aws_cloudburst.BlockType.LAMBDA, 350, 150),
        (aws_cloudburst.BlockType.CLOUDWATCH, 500, 150),
        (aws_cloudburst.BlockType.S3, 650, 150),
        (aws_cloudburst.BlockType.LAMBDA, 800, 150),
        
        # Second row - Tier 2
        (aws_cloudburst.BlockType.EC2, 200, 200),
        (aws_cloudburst.BlockType.RDS, 350, 200),
        (aws_cloudburst.BlockType.API_GATEWAY, 500, 200),
        (aws_cloudburst.BlockType.EC2, 650, 200),
        (aws_cloudburst.BlockType.RDS, 800, 200),
        
        # Third row - Tier 3
        (aws_cloudburst.BlockType.EKS, 275, 250),
        (aws_cloudburst.BlockType.SAGEMAKER, 425, 250),
        (aws_cloudburst.BlockType.BEDROCK, 575, 250),
        (aws_cloudburst.BlockType.EKS, 725, 250),
        
        # Special blocks
        (aws_cloudburst.BlockType.Q_DEVELOPER, 350, 300),
        (aws_cloudburst.BlockType.CLOUDFORMATION, 500, 300),
        (aws_cloudburst.BlockType.AUTO_SCALING, 650, 300),
    ]
    
    for block_type, x, y in showcase_services:
        block = aws_cloudburst.Block(x, y, block_type)
        game.level.blocks.append(block)
    
    # Create power-ups for visual showcase
    powerup_types = list(aws_cloudburst.PowerUpType)
    for i, powerup_type in enumerate(powerup_types):
        x = 100 + i * 150
        y = 400
        powerup = aws_cloudburst.PowerUp(x, y, powerup_type)
        powerup.velocity.y = 50  # Slow fall for visibility
        game.powerups.append(powerup)
    
    # Activate some power-ups for visual effects
    game.active_powerups[aws_cloudburst.PowerUpType.PADDLE_EXTEND] = 10.0
    game.active_powerups[aws_cloudburst.PowerUpType.SCORE_MULTIPLIER] = 8.0
    game.active_powerups[aws_cloudburst.PowerUpType.MULTI_BALL] = 5.0
    game.paddle.extended = True
    game.paddle.width = 180
    game.score_multiplier = 2
    game.score = 15750  # Show impressive score
    
    print("\n🎬 Recording 15-second feature showcase...")
    
    start_time = time.time()
    frames = 0
    demo_phase = 0
    
    while time.time() - start_time < 15.0:
        current_time = time.time() - start_time
        dt = game.clock.tick(60) / 1000.0
        frames += 1
        
        # Handle quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        # Dynamic demo phases
        if current_time < 3.0:
            demo_phase = 0  # Branding showcase
        elif current_time < 6.0:
            demo_phase = 1  # Gameplay action
        elif current_time < 9.0:
            demo_phase = 2  # Power-ups showcase
        elif current_time < 12.0:
            demo_phase = 3  # Block destruction
        else:
            demo_phase = 4  # Final showcase
        
        # Update game elements
        keys = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_a: False, pygame.K_d: False}
        
        # Automated paddle movement for demo
        if demo_phase == 1 or demo_phase == 3:
            # Follow the balls
            if game.balls:
                target_x = game.balls[0].position.x
                if game.paddle.position.x < target_x - 20:
                    keys[pygame.K_RIGHT] = True
                elif game.paddle.position.x > target_x + 20:
                    keys[pygame.K_LEFT] = True
        
        game.paddle.update(dt, keys)
        
        # Update balls with collision
        for ball in game.balls:
            ball.update(dt)
            
            # Ball-paddle collision
            paddle_rect = game.paddle.get_rect()
            ball_rect = pygame.Rect(ball.position.x - ball.radius, ball.position.y - ball.radius,
                                  ball.radius * 2, ball.radius * 2)
            
            if ball_rect.colliderect(paddle_rect) and ball.velocity.y > 0:
                ball.bounce_off_paddle(game.paddle.position.x, game.paddle.width)
                game.audio.play_bounce()
            
            # Ball-block collision with destruction
            for block in game.level.blocks:
                if not block.destroyed and ball_rect.colliderect(block.get_rect()):
                    # Simple collision response
                    if abs(ball.position.x - block.get_rect().centerx) > abs(ball.position.y - block.get_rect().centery):
                        ball.velocity.x = -ball.velocity.x
                    else:
                        ball.velocity.y = -ball.velocity.y
                    
                    # Destroy block for visual effect
                    if demo_phase >= 2:
                        points, destroyed = block.hit()
                        if points > 0:
                            game.score += points * game.score_multiplier
                            game.audio.play_block_hit()
                    break
        
        # Update power-ups
        for powerup in game.powerups:
            powerup.update(dt)
        
        # Update active power-up timers
        for powerup_type in aws_cloudburst.PowerUpType:
            if game.active_powerups[powerup_type] > 0:
                game.active_powerups[powerup_type] -= dt
        
        # Draw everything
        game._draw_background()
        
        # Dynamic titles based on demo phase
        title_font = pygame.font.Font(None, 48)
        subtitle_font = pygame.font.Font(None, 24)
        
        if demo_phase == 0:
            title = "AWS CloudBurst - Professional Branding"
            subtitle = "Authentic AWS Q Developer Ball & Service Icons"
        elif demo_phase == 1:
            title = "Dynamic Gameplay Action"
            subtitle = "Smooth Physics & Ball Control"
        elif demo_phase == 2:
            title = "AWS-Themed Power-ups"
            subtitle = "Auto Scaling, Multi-Ball, Score Multiplier Active"
        elif demo_phase == 3:
            title = "Service Block Destruction"
            subtitle = "Learn AWS Services Through Gameplay"
        else:
            title = "Complete AWS Gaming Experience"
            subtitle = "Education + Entertainment + Professional Design"
        
        title_text = title_font.render(title, True, aws_cloudburst.AWS_ORANGE)
        title_rect = title_text.get_rect(center=(512, 40))
        game.screen.blit(title_text, title_rect)
        
        subtitle_text = subtitle_font.render(subtitle, True, aws_cloudburst.AWS_WHITE)
        subtitle_rect = subtitle_text.get_rect(center=(512, 70))
        game.screen.blit(subtitle_text, subtitle_rect)
        
        # Draw game elements
        for block in game.level.blocks:
            if not block.destroyed:
                block.draw(game.screen)
        
        for ball in game.balls:
            ball.draw(game.screen)
        
        game.paddle.draw(game.screen)
        
        for powerup in game.powerups:
            powerup.draw(game.screen)
        
        # Draw enhanced HUD
        game.ui.draw_hud(game.screen, game.score, game.lives, game.current_level, game.active_powerups)
        
        # Add feature callouts based on phase
        feature_font = pygame.font.Font(None, 18)
        
        if demo_phase == 0:
            features = [
                "✓ AWS Q Developer Ball with AI Branding",
                "✓ AWS Smile Curve Paddle Design",
                "✓ 12 Authentic AWS Service Icons"
            ]
        elif demo_phase == 1:
            features = [
                "✓ 60 FPS Smooth Gameplay",
                "✓ Realistic Ball Physics",
                "✓ Responsive Paddle Control"
            ]
        elif demo_phase == 2:
            features = [
                "✓ 6 AWS-Themed Power-ups",
                "✓ Visual Effect Indicators",
                "✓ Timed Enhancement System"
            ]
        elif demo_phase == 3:
            features = [
                "✓ Progressive Difficulty Levels",
                "✓ AWS Architecture Patterns",
                "✓ Educational Service Learning"
            ]
        else:
            features = [
                "✓ Professional AWS Branding",
                "✓ Complete Menu System",
                "✓ High Score Achievements"
            ]
        
        y_offset = 100
        for feature in features:
            feature_text = feature_font.render(feature, True, aws_cloudburst.AWS_WHITE)
            game.screen.blit(feature_text, (50, y_offset))
            y_offset += 22
        
        # Add progress indicator
        progress = current_time / 15.0
        progress_width = int(400 * progress)
        progress_rect = pygame.Rect(312, 720, progress_width, 8)
        pygame.draw.rect(game.screen, aws_cloudburst.AWS_ORANGE, progress_rect)
        pygame.draw.rect(game.screen, aws_cloudburst.AWS_WHITE, (312, 720, 400, 8), 2)
        
        # Time remaining
        time_remaining = 15.0 - current_time
        time_text = feature_font.render(f"Demo: {time_remaining:.1f}s remaining", True, aws_cloudburst.AWS_WHITE)
        game.screen.blit(time_text, (720, 715))
        
        pygame.display.flip()
    
    print(f"✅ Demo completed! Rendered {frames} frames at {frames/15.0:.1f} FPS")
    
    # Final summary
    print("\n🎯 15-Second Demo Showcased:")
    print("   🎨 Professional AWS Branding")
    print("     • Q Developer ball with gradient & AI branding")
    print("     • AWS smile curve paddle design")
    print("     • 12 authentic AWS service icons")
    print()
    print("   🎮 Dynamic Gameplay")
    print("     • Smooth 60 FPS physics")
    print("     • Responsive ball control")
    print("     • Realistic collision detection")
    print()
    print("   ⚡ Power-up System")
    print("     • 6 AWS-themed enhancements")
    print("     • Visual effect indicators")
    print("     • Timed activation system")
    print()
    print("   🏗️ Educational Content")
    print("     • AWS service recognition")
    print("     • Architecture pattern levels")
    print("     • Professional learning tool")
    print()
    print("   🏆 Complete Experience")
    print("     • High score achievements")
    print("     • Menu system with help")
    print("     • Professional polish throughout")
    
    pygame.quit()
    print("\n🎬 15-Second Feature Demo Complete!")
    print("AWS CloudBurst: Where AWS Education Meets Retro Gaming! 🚀")

if __name__ == "__main__":
    try:
        demo_15_seconds()
    except KeyboardInterrupt:
        print("\n⏹️  Demo interrupted by user")
        pygame.quit()
    except Exception as e:
        print(f"❌ Demo error: {e}")
        pygame.quit()
        sys.exit(1)
