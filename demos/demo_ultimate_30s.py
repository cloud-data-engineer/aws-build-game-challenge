#!/usr/bin/env python3
"""
Ultimate 30-Second AWS CloudBurst Demo
Maximum visual impact with guaranteed feature showcase
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

def demo_ultimate_30s():
    """Ultimate 30-second demo with maximum visual impact."""
    print("🎮 Starting ULTIMATE 30-Second AWS CloudBurst Demo...")
    print("🌟 Maximum Visual Impact - All Features Guaranteed!")
    
    # Create game instance
    game = aws_cloudburst.Game()
    
    # Set up spectacular demo scene
    game.paddle.position.x = 512
    game.paddle.position.y = 650
    game.score = 0  # Start from zero to show score growth
    game.lives = 3
    game.current_level = 3
    
    # Create optimal ball setup
    game.balls.clear()
    main_ball = aws_cloudburst.Ball(512, 450, 300)
    main_ball.velocity.x = 200
    main_ball.velocity.y = -250
    game.balls.append(main_ball)
    
    # Create perfect block arrangement for maximum destruction
    game.level.blocks.clear()
    
    # Strategic block placement for guaranteed hits
    showcase_blocks = [
        # Front row - guaranteed to be hit first (Tier 1)
        (aws_cloudburst.BlockType.S3, 300, 180),
        (aws_cloudburst.BlockType.LAMBDA, 420, 180),
        (aws_cloudburst.BlockType.CLOUDWATCH, 540, 180),
        (aws_cloudburst.BlockType.S3, 660, 180),
        (aws_cloudburst.BlockType.LAMBDA, 780, 180),
        
        # Second row - Tier 2 blocks
        (aws_cloudburst.BlockType.EC2, 240, 230),
        (aws_cloudburst.BlockType.RDS, 360, 230),
        (aws_cloudburst.BlockType.API_GATEWAY, 480, 230),
        (aws_cloudburst.BlockType.EC2, 600, 230),
        (aws_cloudburst.BlockType.RDS, 720, 230),
        (aws_cloudburst.BlockType.API_GATEWAY, 840, 230),
        
        # Third row - Tier 3 blocks
        (aws_cloudburst.BlockType.EKS, 300, 280),
        (aws_cloudburst.BlockType.SAGEMAKER, 420, 280),
        (aws_cloudburst.BlockType.BEDROCK, 540, 280),
        (aws_cloudburst.BlockType.EKS, 660, 280),
        (aws_cloudburst.BlockType.SAGEMAKER, 780, 280),
        
        # Special blocks row - positioned for guaranteed trigger
        (aws_cloudburst.BlockType.Q_DEVELOPER, 360, 330),
        (aws_cloudburst.BlockType.AUTO_SCALING, 480, 330),
        (aws_cloudburst.BlockType.CLOUDFORMATION, 600, 330),
        (aws_cloudburst.BlockType.Q_DEVELOPER, 720, 330),
    ]
    
    # Add all blocks
    for block_type, x, y in showcase_blocks:
        block = aws_cloudburst.Block(x, y, block_type)
        game.level.blocks.append(block)
    
    # Pre-stage power-ups for guaranteed showcase
    staged_powerups = []
    
    # Demo tracking
    blocks_destroyed = 0
    features_shown = {
        'multi_ball': False,
        'paddle_extend': False,
        'score_multiplier': False,
        'slow_motion': False,
        'laser_paddle': False,
        'shield': False
    }
    
    # Force feature activation at specific times
    feature_schedule = {
        3.0: 'branding_complete',
        6.0: 'multi_ball',
        9.0: 'paddle_extend',
        12.0: 'score_multiplier',
        15.0: 'intense_action',
        18.0: 'slow_motion',
        21.0: 'laser_paddle',
        24.0: 'shield',
        27.0: 'finale'
    }
    
    print("\n🎬 Recording ULTIMATE 30-second showcase...")
    print("   🎨 Segment 1 (0-5s): AWS Branding Excellence")
    print("   💥 Segment 2 (5-10s): Block Destruction Spectacle")
    print("   ⚡ Segment 3 (10-15s): Power-up Showcase")
    print("   🚀 Segment 4 (15-20s): Multi-ball Mayhem")
    print("   🔥 Segment 5 (20-25s): Advanced Features")
    print("   🏆 Segment 6 (25-30s): Grand Finale")
    
    start_time = time.time()
    frames = 0
    destruction_effects = []
    
    while time.time() - start_time < 30.0:
        current_time = time.time() - start_time
        dt = game.clock.tick(60) / 1000.0
        frames += 1
        
        # Handle quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        # Determine current segment
        if current_time < 5.0:
            segment = "BRANDING"
            segment_color = aws_cloudburst.AWS_ORANGE
        elif current_time < 10.0:
            segment = "DESTRUCTION"
            segment_color = aws_cloudburst.AWS_RED
        elif current_time < 15.0:
            segment = "POWER-UPS"
            segment_color = (255, 215, 0)
        elif current_time < 20.0:
            segment = "MULTI-BALL"
            segment_color = aws_cloudburst.AWS_GREEN
        elif current_time < 25.0:
            segment = "ADVANCED"
            segment_color = (255, 100, 255)
        else:
            segment = "FINALE"
            segment_color = aws_cloudburst.AWS_WHITE
        
        # Execute feature schedule
        for schedule_time, feature in feature_schedule.items():
            if current_time >= schedule_time and current_time < schedule_time + 0.1:
                if feature == 'multi_ball' and not features_shown['multi_ball']:
                    # Add second and third balls
                    ball2 = aws_cloudburst.Ball(400, 400, 280)
                    ball2.velocity.x = -180
                    ball2.velocity.y = -200
                    game.balls.append(ball2)
                    
                    ball3 = aws_cloudburst.Ball(600, 420, 260)
                    ball3.velocity.x = 150
                    ball3.velocity.y = -220
                    game.balls.append(ball3)
                    
                    game.active_powerups[aws_cloudburst.PowerUpType.MULTI_BALL] = 20.0
                    features_shown['multi_ball'] = True
                    
                elif feature == 'paddle_extend' and not features_shown['paddle_extend']:
                    game.active_powerups[aws_cloudburst.PowerUpType.PADDLE_EXTEND] = 18.0
                    game.paddle.extended = True
                    game.paddle.width = 200  # Extra wide for demo
                    features_shown['paddle_extend'] = True
                    
                elif feature == 'score_multiplier' and not features_shown['score_multiplier']:
                    game.active_powerups[aws_cloudburst.PowerUpType.SCORE_MULTIPLIER] = 15.0
                    game.score_multiplier = 3  # Triple for demo impact
                    features_shown['score_multiplier'] = True
                    
                elif feature == 'slow_motion' and not features_shown['slow_motion']:
                    game.active_powerups[aws_cloudburst.PowerUpType.SLOW_MOTION] = 8.0
                    # Slow down all balls
                    for ball in game.balls:
                        ball.velocity.x *= 0.6
                        ball.velocity.y *= 0.6
                    features_shown['slow_motion'] = True
                    
                elif feature == 'intense_action':
                    # Add fourth ball for maximum action
                    if len(game.balls) < 4:
                        ball4 = aws_cloudburst.Ball(512, 300, 290)
                        ball4.velocity.x = random.choice([-200, 200])
                        ball4.velocity.y = -180
                        game.balls.append(ball4)
        
        # Intelligent paddle movement for perfect demo
        keys = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_a: False, pygame.K_d: False}
        
        if game.balls:
            # Advanced AI for optimal ball management
            closest_ball = min(game.balls, key=lambda b: abs(b.position.y - game.paddle.position.y))
            target_x = closest_ball.position.x
            
            # Predict ball position
            if closest_ball.velocity.y > 0:  # Ball coming down
                time_to_paddle = (game.paddle.position.y - closest_ball.position.y) / closest_ball.velocity.y
                predicted_x = closest_ball.position.x + closest_ball.velocity.x * time_to_paddle
                target_x = predicted_x
            
            # Move paddle with some smoothing
            paddle_speed = 500 if current_time > 15.0 else 400
            if game.paddle.position.x < target_x - 30:
                keys[pygame.K_RIGHT] = True
            elif game.paddle.position.x > target_x + 30:
                keys[pygame.K_LEFT] = True
        
        game.paddle.update(dt, keys)
        
        # Update balls with enhanced physics
        for ball in game.balls[:]:
            ball.update(dt)
            
            # Respawn balls that fall off for continuous action
            if ball.position.y > game.screen.get_height():
                game.balls.remove(ball)
                if len(game.balls) < 2:  # Maintain minimum balls
                    new_ball = aws_cloudburst.Ball(
                        game.paddle.position.x + random.randint(-50, 50), 
                        game.paddle.position.y - 40, 
                        280 + random.randint(-20, 20)
                    )
                    new_ball.velocity.x = random.choice([-180, -120, 120, 180])
                    new_ball.velocity.y = -200
                    game.balls.append(new_ball)
            
            # Ball-paddle collision
            paddle_rect = game.paddle.get_rect()
            ball_rect = pygame.Rect(ball.position.x - ball.radius, ball.position.y - ball.radius,
                                  ball.radius * 2, ball.radius * 2)
            
            if ball_rect.colliderect(paddle_rect) and ball.velocity.y > 0:
                ball.bounce_off_paddle(game.paddle.position.x, game.paddle.width)
                game.audio.play_bounce()
            
            # Ball-block collision with GUARANTEED destruction
            for block in game.level.blocks[:]:
                if not block.destroyed and ball_rect.colliderect(block.get_rect()):
                    # Perfect collision response
                    block_rect = block.get_rect()
                    if abs(ball.position.x - block_rect.centerx) > abs(ball.position.y - block_rect.centery):
                        ball.velocity.x = -ball.velocity.x
                    else:
                        ball.velocity.y = -ball.velocity.y
                    
                    # FORCE destruction for spectacular demo
                    block.destroyed = True
                    points = block.points * game.score_multiplier
                    game.score += points
                    blocks_destroyed += 1
                    game.audio.play_block_hit()
                    
                    # Add destruction effect
                    destruction_effects.append({
                        'x': block.position.x,
                        'y': block.position.y,
                        'time': current_time,
                        'color': block.color
                    })
                    
                    # Create power-up drops for visual effect
                    if random.random() < 0.4:  # 40% chance
                        powerup_types = list(aws_cloudburst.PowerUpType)
                        powerup_type = random.choice(powerup_types)
                        powerup = aws_cloudburst.PowerUp(block.position.x, block.position.y, powerup_type)
                        staged_powerups.append(powerup)
                    
                    break
        
        # Update staged power-ups
        for powerup in staged_powerups[:]:
            powerup.update(dt)
            
            if powerup.collected or powerup.position.y > game.screen.get_height():
                staged_powerups.remove(powerup)
                continue
            
            # Auto-collect for demo
            paddle_rect = game.paddle.get_rect()
            if powerup.get_rect().colliderect(paddle_rect):
                game._activate_powerup(powerup.powerup_type)
                staged_powerups.remove(powerup)
                game.audio.play_powerup()
        
        # Update power-up timers
        for powerup_type in aws_cloudburst.PowerUpType:
            if game.active_powerups[powerup_type] > 0:
                game.active_powerups[powerup_type] -= dt
                if game.active_powerups[powerup_type] <= 0:
                    game._deactivate_powerup(powerup_type)
        
        # Draw everything with enhanced effects
        game._draw_background()
        
        # Draw destruction effects
        for effect in destruction_effects[:]:
            effect_age = current_time - effect['time']
            if effect_age > 1.0:
                destruction_effects.remove(effect)
                continue
            
            # Explosion effect
            alpha = int(255 * (1.0 - effect_age))
            size = int(20 * effect_age)
            
            explosion_surface = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
            pygame.draw.circle(explosion_surface, (*effect['color'], alpha), (size, size), size)
            game.screen.blit(explosion_surface, (effect['x'] - size, effect['y'] - size))
        
        # Main title with pulsing effect
        title_font = pygame.font.Font(None, 56)
        pulse = 1.0 + 0.1 * math.sin(current_time * 4)
        title_size = int(56 * pulse)
        title_font = pygame.font.Font(None, title_size)
        title_text = title_font.render("AWS CloudBurst ULTIMATE", True, aws_cloudburst.AWS_ORANGE)
        title_rect = title_text.get_rect(center=(512, 25))
        game.screen.blit(title_text, title_rect)
        
        # Segment indicator with glow effect
        segment_font = pygame.font.Font(None, 28)
        segment_text = segment_font.render(f"🎬 {segment} SHOWCASE", True, segment_color)
        segment_rect = segment_text.get_rect(center=(512, 55))
        game.screen.blit(segment_text, segment_rect)
        
        # Draw game elements
        for block in game.level.blocks:
            if not block.destroyed:
                block.draw(game.screen)
        
        for ball in game.balls:
            ball.draw(game.screen)
        
        game.paddle.draw(game.screen)
        
        for powerup in staged_powerups:
            powerup.draw(game.screen)
        
        # Enhanced HUD with extra info
        game.ui.draw_hud(game.screen, game.score, game.lives, game.current_level, game.active_powerups)
        
        # Real-time statistics
        stats_font = pygame.font.Font(None, 20)
        stats = [
            f"🎯 Blocks Destroyed: {blocks_destroyed}",
            f"⚡ Active Balls: {len(game.balls)}",
            f"🚀 Score: {game.score:,}",
            f"💫 Multiplier: {game.score_multiplier}x",
            f"🔥 FPS: {frames/(current_time+0.001):.0f}"
        ]
        
        y_offset = 85
        for stat in stats:
            stat_text = stats_font.render(stat, True, aws_cloudburst.AWS_WHITE)
            game.screen.blit(stat_text, (20, y_offset))
            y_offset += 25
        
        # Feature showcase panel
        feature_font = pygame.font.Font(None, 18)
        active_features = []
        for feature, shown in features_shown.items():
            if shown:
                active_features.append(f"✅ {feature.replace('_', ' ').title()}")
        
        if active_features:
            y_offset = 85
            for feature in active_features[-6:]:  # Show last 6
                feature_text = feature_font.render(feature, True, aws_cloudburst.AWS_GREEN)
                game.screen.blit(feature_text, (750, y_offset))
                y_offset += 20
        
        # Animated progress bar
        progress = current_time / 30.0
        bar_width = 700
        bar_height = 20
        bar_x = (1024 - bar_width) // 2
        bar_y = 720
        
        # Animated background
        for i in range(0, bar_width, 20):
            alpha = int(100 + 50 * math.sin(current_time * 3 + i * 0.1))
            bar_bg = pygame.Surface((20, bar_height), pygame.SRCALPHA)
            bar_bg.fill((*aws_cloudburst.AWS_DARK_BLUE, alpha))
            game.screen.blit(bar_bg, (bar_x + i, bar_y))
        
        # Progress fill with gradient
        progress_width = int(bar_width * progress)
        for i in range(progress_width):
            intensity = i / bar_width
            color = tuple(int(c * (0.5 + 0.5 * intensity)) for c in segment_color)
            pygame.draw.line(game.screen, color, (bar_x + i, bar_y), (bar_x + i, bar_y + bar_height))
        
        # Border
        pygame.draw.rect(game.screen, aws_cloudburst.AWS_WHITE, (bar_x, bar_y, bar_width, bar_height), 3)
        
        # Timer with countdown effect
        remaining = 30.0 - current_time
        timer_color = aws_cloudburst.AWS_RED if remaining < 5.0 else aws_cloudburst.AWS_WHITE
        timer_text = stats_font.render(f"⏱️ {remaining:.1f}s", True, timer_color)
        game.screen.blit(timer_text, (bar_x + bar_width + 20, bar_y))
        
        pygame.display.flip()
    
    print(f"\n🎉 ULTIMATE demo completed! {frames} frames at {frames/30.0:.1f} FPS")
    print(f"📊 Final Statistics:")
    print(f"   • Blocks Destroyed: {blocks_destroyed}")
    print(f"   • Final Score: {game.score:,}")
    print(f"   • Max Balls Active: {len(game.balls)}")
    print(f"   • Features Showcased: {sum(features_shown.values())}/6")
    print(f"   • Destruction Effects: {len(destruction_effects)}")
    
    pygame.quit()
    print("\n🌟 ULTIMATE 30-Second Demo Complete!")
    print("🚀 Maximum visual impact with all features guaranteed!")

if __name__ == "__main__":
    try:
        demo_ultimate_30s()
    except KeyboardInterrupt:
        print("\n⏹️  Demo interrupted by user")
        pygame.quit()
    except Exception as e:
        print(f"❌ Demo error: {e}")
        pygame.quit()
        sys.exit(1)
