#!/usr/bin/env python3
"""
Visual demo of the enhanced AWS logos for paddle and ball.
"""

import sys
import os
import time
import math

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import aws_cloudburst
import pygame

def demo_aws_logos():
    """Show a visual demo of the enhanced AWS logos."""
    print("🎮 Starting AWS Logo Enhancement Demo...")
    
    # Create game instance
    game = aws_cloudburst.Game()
    
    print("🎨 Showcasing enhanced AWS branding:")
    print("   • AWS Q Developer Ball: Enhanced with gradient, AI indicator, and branding dots")
    print("   • AWS Paddle: Features iconic AWS smile curve and AWS text")
    
    # Position elements for better visibility
    game.paddle.position.x = 512
    game.paddle.position.y = 400
    
    # Create multiple balls to show different sizes
    game.balls.clear()
    ball_sizes = [6, 8, 10, 12]
    for i, size in enumerate(ball_sizes):
        ball = aws_cloudburst.Ball(200 + i * 150, 200, 0)  # Speed 0 for static display
        ball.radius = size
        ball.velocity.x = 0
        ball.velocity.y = 0
        game.balls.append(ball)
    
    print("\n📺 Displaying enhanced logos for 8 seconds...")
    
    start_time = time.time()
    frames = 0
    
    while time.time() - start_time < 8.0:
        # Handle quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        # Clear screen
        game.screen.fill(aws_cloudburst.AWS_DARK_BLUE)
        
        # Draw title
        font = pygame.font.Font(None, 48)
        title_text = font.render("AWS CloudBurst - Enhanced Logos", True, aws_cloudburst.AWS_ORANGE)
        title_rect = title_text.get_rect(center=(512, 50))
        game.screen.blit(title_text, title_rect)
        
        # Draw subtitle
        subtitle_font = pygame.font.Font(None, 24)
        subtitle_text = subtitle_font.render("AWS Q Developer Ball & AWS-Branded Paddle", True, aws_cloudburst.AWS_WHITE)
        subtitle_rect = subtitle_text.get_rect(center=(512, 80))
        game.screen.blit(subtitle_text, subtitle_rect)
        
        # Draw balls with labels
        for i, ball in enumerate(game.balls):
            ball.draw(game.screen)
            
            # Add size label
            label_font = pygame.font.Font(None, 20)
            label_text = label_font.render(f"Size {ball.radius}", True, aws_cloudburst.AWS_WHITE)
            label_rect = label_text.get_rect(center=(ball.position.x, ball.position.y + 30))
            game.screen.blit(label_text, label_rect)
        
        # Draw paddle with label
        game.paddle.draw(game.screen)
        paddle_label = subtitle_font.render("AWS-Branded Paddle with Smile Curve", True, aws_cloudburst.AWS_WHITE)
        paddle_rect = paddle_label.get_rect(center=(512, 450))
        game.screen.blit(paddle_label, paddle_rect)
        
        # Draw extended paddle example
        extended_paddle = aws_cloudburst.Paddle(512, 500)
        extended_paddle.extended = True
        extended_paddle.width = 180
        extended_paddle.draw(game.screen)
        extended_label = subtitle_font.render("Extended Paddle (Power-up Active)", True, aws_cloudburst.AWS_GREEN)
        extended_rect = extended_label.get_rect(center=(512, 550))
        game.screen.blit(extended_label, extended_rect)
        
        # Add feature callouts
        features = [
            "✓ AWS Q Developer branding with AI indicator",
            "✓ Gradient effects and professional styling", 
            "✓ Iconic AWS smile curve on paddle",
            "✓ Enhanced visual feedback and recognition"
        ]
        
        y_offset = 600
        feature_font = pygame.font.Font(None, 20)
        for feature in features:
            feature_text = feature_font.render(feature, True, aws_cloudburst.AWS_WHITE)
            game.screen.blit(feature_text, (50, y_offset))
            y_offset += 25
        
        pygame.display.flip()
        game.clock.tick(60)
        frames += 1
    
    print(f"✅ Demo completed! Rendered {frames} frames")
    print("\n🎨 Logo Enhancement Summary:")
    print("   • AWS Q Developer Ball:")
    print("     - Gradient orange-to-white effect")
    print("     - Large 'Q' with 'AI' indicator below")
    print("     - AWS branding dots around perimeter")
    print("     - Enhanced trail effects")
    print()
    print("   • AWS-Branded Paddle:")
    print("     - Iconic AWS smile curve design")
    print("     - 'AWS' text branding")
    print("     - Gradient background effect")
    print("     - Cloud service indicator dots")
    print("     - Green color when extended (power-up)")
    
    pygame.quit()
    print("\n🎮 AWS Logo Enhancement Demo Complete!")
    print("The game now features authentic AWS branding elements!")

if __name__ == "__main__":
    try:
        demo_aws_logos()
    except KeyboardInterrupt:
        print("\n⏹️  Demo interrupted by user")
        pygame.quit()
    except Exception as e:
        print(f"❌ Demo error: {e}")
        pygame.quit()
        sys.exit(1)
