#!/usr/bin/env python3
"""
Video-Ready 15-Second AWS CloudBurst Demo
Perfect for screen recording with clear feature segments
"""

import sys
import os
import time
import math

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import aws_cloudburst
import pygame

def demo_video_ready():
    """Video-ready 15-second demo with clear segments."""
    print("🎬 Starting Video-Ready AWS CloudBurst Demo...")
    print("📹 Perfect for screen recording - 15 seconds of pure showcase")
    
    # Create game instance
    game = aws_cloudburst.Game()
    
    # Set up perfect demo scene
    game.paddle.position.x = 512
    game.paddle.position.y = 650
    game.score = 25000  # Impressive score
    game.lives = 3
    game.current_level = 4
    
    # Create visually appealing ball setup
    game.balls.clear()
    main_ball = aws_cloudburst.Ball(512, 400, 250)
    main_ball.velocity.x = 200
    main_ball.velocity.y = -180
    game.balls.append(main_ball)
    
    # Add second ball for multi-ball effect
    second_ball = aws_cloudburst.Ball(400, 350, 220)
    second_ball.velocity.x = -150
    second_ball.velocity.y = -200
    game.balls.append(second_ball)
    
    # Create perfect block arrangement showcasing all services
    game.level.blocks.clear()
    
    # Top row - Tier 1 (colorful variety)
    tier1_blocks = [
        (aws_cloudburst.BlockType.S3, 200, 120),
        (aws_cloudburst.BlockType.LAMBDA, 320, 120),
        (aws_cloudburst.BlockType.CLOUDWATCH, 440, 120),
        (aws_cloudburst.BlockType.S3, 560, 120),
        (aws_cloudburst.BlockType.LAMBDA, 680, 120),
        (aws_cloudburst.BlockType.CLOUDWATCH, 800, 120),
    ]
    
    # Middle row - Tier 2 (more complex)
    tier2_blocks = [
        (aws_cloudburst.BlockType.EC2, 200, 180),
        (aws_cloudburst.BlockType.RDS, 320, 180),
        (aws_cloudburst.BlockType.API_GATEWAY, 440, 180),
        (aws_cloudburst.BlockType.EC2, 560, 180),
        (aws_cloudburst.BlockType.RDS, 680, 180),
        (aws_cloudburst.BlockType.API_GATEWAY, 800, 180),
    ]
    
    # Advanced row - Tier 3 (premium services)
    tier3_blocks = [
        (aws_cloudburst.BlockType.EKS, 260, 240),
        (aws_cloudburst.BlockType.SAGEMAKER, 380, 240),
        (aws_cloudburst.BlockType.BEDROCK, 500, 240),
        (aws_cloudburst.BlockType.EKS, 620, 240),
        (aws_cloudburst.BlockType.SAGEMAKER, 740, 240),
    ]
    
    # Special blocks row
    special_blocks = [
        (aws_cloudburst.BlockType.Q_DEVELOPER, 320, 300),
        (aws_cloudburst.BlockType.CLOUDFORMATION, 440, 300),
        (aws_cloudburst.BlockType.AUTO_SCALING, 560, 300),
        (aws_cloudburst.BlockType.Q_DEVELOPER, 680, 300),
    ]
    
    # Add all blocks
    for block_type, x, y in tier1_blocks + tier2_blocks + tier3_blocks + special_blocks:
        block = aws_cloudburst.Block(x, y, block_type)
        game.level.blocks.append(block)
    
    # Set up power-ups showcase
    game.active_powerups[aws_cloudburst.PowerUpType.PADDLE_EXTEND] = 12.0
    game.active_powerups[aws_cloudburst.PowerUpType.SCORE_MULTIPLIER] = 10.0
    game.active_powerups[aws_cloudburst.PowerUpType.MULTI_BALL] = 8.0
    game.paddle.extended = True
    game.paddle.width = 180
    game.score_multiplier = 2
    
    # Create falling power-ups for visual appeal
    powerup_showcase = [
        (aws_cloudburst.PowerUpType.LASER_PADDLE, 150, 350),
        (aws_cloudburst.PowerUpType.SHIELD, 300, 380),
        (aws_cloudburst.PowerUpType.SLOW_MOTION, 450, 360),
    ]
    
    for powerup_type, x, y in powerup_showcase:
        powerup = aws_cloudburst.PowerUp(x, y, powerup_type)
        powerup.velocity.y = 80  # Slow fall
        game.powerups.append(powerup)
    
    print("\n🎥 Recording video-ready demo...")
    print("   📊 Segment 1 (0-3s): AWS Branding Showcase")
    print("   🎮 Segment 2 (3-6s): Dynamic Gameplay")
    print("   ⚡ Segment 3 (6-9s): Power-ups & Effects")
    print("   🏗️ Segment 4 (9-12s): Service Learning")
    print("   🏆 Segment 5 (12-15s): Complete Experience")
    
    start_time = time.time()
    frames = 0
    
    while time.time() - start_time < 15.0:
        current_time = time.time() - start_time
        dt = game.clock.tick(60) / 1000.0
        frames += 1
        
        # Handle quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        # Determine current segment
        if current_time < 3.0:
            segment = "BRANDING"
            segment_color = aws_cloudburst.AWS_ORANGE
        elif current_time < 6.0:
            segment = "GAMEPLAY"
            segment_color = aws_cloudburst.AWS_GREEN
        elif current_time < 9.0:
            segment = "POWER-UPS"
            segment_color = (255, 215, 0)  # Gold
        elif current_time < 12.0:
            segment = "LEARNING"
            segment_color = (52, 144, 220)  # Blue
        else:
            segment = "COMPLETE"
            segment_color = aws_cloudburst.AWS_WHITE
        
        # Automated paddle movement for perfect demo
        keys = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_a: False, pygame.K_d: False}
        
        if game.balls:
            # Smart paddle AI for demo
            target_x = sum(ball.position.x for ball in game.balls) / len(game.balls)
            if game.paddle.position.x < target_x - 30:
                keys[pygame.K_RIGHT] = True
            elif game.paddle.position.x > target_x + 30:
                keys[pygame.K_LEFT] = True
        
        game.paddle.update(dt, keys)
        
        # Update balls with perfect collision
        for ball in game.balls:
            ball.update(dt)
            
            # Ball-paddle collision
            paddle_rect = game.paddle.get_rect()
            ball_rect = pygame.Rect(ball.position.x - ball.radius, ball.position.y - ball.radius,
                                  ball.radius * 2, ball.radius * 2)
            
            if ball_rect.colliderect(paddle_rect) and ball.velocity.y > 0:
                ball.bounce_off_paddle(game.paddle.position.x, game.paddle.width)
                game.audio.play_bounce()
            
            # Ball-block collision with strategic destruction
            for block in game.level.blocks[:]:
                if not block.destroyed and ball_rect.colliderect(block.get_rect()):
                    # Collision response
                    block_rect = block.get_rect()
                    if abs(ball.position.x - block_rect.centerx) > abs(ball.position.y - block_rect.centery):
                        ball.velocity.x = -ball.velocity.x
                    else:
                        ball.velocity.y = -ball.velocity.y
                    
                    # Strategic block destruction for demo
                    if current_time > 4.0:  # Start destroying after branding showcase
                        points, destroyed = block.hit()
                        if points > 0:
                            game.score += points * game.score_multiplier
                            game.audio.play_block_hit()
                    break
        
        # Update power-ups
        for powerup in game.powerups:
            powerup.update(dt)
        
        # Update power-up timers
        for powerup_type in aws_cloudburst.PowerUpType:
            if game.active_powerups[powerup_type] > 0:
                game.active_powerups[powerup_type] -= dt
        
        # Draw everything with perfect presentation
        game._draw_background()
        
        # Main title - always visible
        title_font = pygame.font.Font(None, 56)
        title_text = title_font.render("AWS CloudBurst", True, aws_cloudburst.AWS_ORANGE)
        title_rect = title_text.get_rect(center=(512, 35))
        game.screen.blit(title_text, title_rect)
        
        # Segment indicator
        segment_font = pygame.font.Font(None, 28)
        segment_text = segment_font.render(f"Showcasing: {segment}", True, segment_color)
        segment_rect = segment_text.get_rect(center=(512, 65))
        game.screen.blit(segment_text, segment_rect)
        
        # Draw all game elements
        for block in game.level.blocks:
            if not block.destroyed:
                block.draw(game.screen)
        
        for ball in game.balls:
            ball.draw(game.screen)
        
        game.paddle.draw(game.screen)
        
        for powerup in game.powerups:
            powerup.draw(game.screen)
        
        # Enhanced HUD
        game.ui.draw_hud(game.screen, game.score, game.lives, game.current_level, game.active_powerups)
        
        # Segment-specific callouts
        callout_font = pygame.font.Font(None, 20)
        
        if segment == "BRANDING":
            callouts = [
                "🎨 Professional AWS Visual Identity",
                "🏀 Q Developer Ball with AI Branding",
                "🏓 AWS Smile Curve Paddle Design",
                "🧱 Authentic Service Icons"
            ]
        elif segment == "GAMEPLAY":
            callouts = [
                "🎮 Smooth 60 FPS Physics Engine",
                "⚡ Responsive Ball Control",
                "🎯 Realistic Collision Detection",
                "🏃 Dynamic Paddle Movement"
            ]
        elif segment == "POWER-UPS":
            callouts = [
                "⚡ 6 AWS-Themed Power-ups Active",
                "📊 Visual Effect Indicators",
                "⏱️ Timed Enhancement System",
                "🔄 Multi-Ball & Score Multiplier"
            ]
        elif segment == "LEARNING":
            callouts = [
                "🏗️ AWS Architecture Patterns",
                "📚 12 Authentic AWS Services",
                "🎓 Educational Service Recognition",
                "💡 Learn Through Gameplay"
            ]
        else:  # COMPLETE
            callouts = [
                "🏆 Complete Gaming Experience",
                "📈 High Score Achievements",
                "📋 Full Menu System",
                "✨ Professional Polish"
            ]
        
        y_offset = 95
        for callout in callouts:
            callout_text = callout_font.render(callout, True, aws_cloudburst.AWS_WHITE)
            game.screen.blit(callout_text, (30, y_offset))
            y_offset += 25
        
        # Progress bar
        progress = current_time / 15.0
        bar_width = 500
        bar_height = 12
        bar_x = (1024 - bar_width) // 2
        bar_y = 740
        
        # Background
        pygame.draw.rect(game.screen, aws_cloudburst.AWS_DARK_BLUE, (bar_x, bar_y, bar_width, bar_height))
        # Progress
        pygame.draw.rect(game.screen, segment_color, (bar_x, bar_y, int(bar_width * progress), bar_height))
        # Border
        pygame.draw.rect(game.screen, aws_cloudburst.AWS_WHITE, (bar_x, bar_y, bar_width, bar_height), 2)
        
        # Timer
        timer_text = callout_font.render(f"{15.0 - current_time:.1f}s", True, aws_cloudburst.AWS_WHITE)
        game.screen.blit(timer_text, (bar_x + bar_width + 10, bar_y - 2))
        
        pygame.display.flip()
    
    print(f"\n✅ Video demo completed! {frames} frames at {frames/15.0:.1f} FPS")
    print("🎬 Perfect for screen recording and showcasing!")
    
    pygame.quit()
    print("\n🎥 Video-Ready Demo Complete!")
    print("🚀 AWS CloudBurst: Professional AWS Education Gaming!")

if __name__ == "__main__":
    try:
        demo_video_ready()
    except KeyboardInterrupt:
        print("\n⏹️  Demo interrupted by user")
        pygame.quit()
    except Exception as e:
        print(f"❌ Demo error: {e}")
        pygame.quit()
        sys.exit(1)
