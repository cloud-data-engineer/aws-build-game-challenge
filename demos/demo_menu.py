#!/usr/bin/env python3
"""
Visual demo of the new High Scores and Controls screens.
"""

import sys
import os
import time

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import aws_cloudburst
import pygame

def demo_menu_screens():
    """Show a visual demo of the new menu screens."""
    print("🎮 Starting AWS CloudBurst Menu Demo...")
    
    # Create game instance
    game = aws_cloudburst.Game()
    
    # Set a sample high score for demo
    game.high_score = 25000
    
    print("📺 Displaying menu screens for 3 seconds each...")
    
    screens_to_demo = [
        (aws_cloudburst.GameState.MENU, "Main Menu"),
        (aws_cloudburst.GameState.HIGH_SCORE, "High Scores Screen"),
        (aws_cloudburst.GameState.CONTROLS, "Controls & Help Screen")
    ]
    
    for state, name in screens_to_demo:
        print(f"   🖥️  Showing: {name}")
        game.state = state
        
        # Render the screen for 3 seconds
        start_time = time.time()
        frames = 0
        
        while time.time() - start_time < 3.0:
            # Handle quit events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            
            # Render the appropriate screen
            if game.state == aws_cloudburst.GameState.MENU:
                game.ui.draw_menu(game.screen, "AWS CloudBurst", game.menu_options, game.selected_menu_option)
            elif game.state == aws_cloudburst.GameState.HIGH_SCORE:
                game.ui.draw_high_scores(game.screen, game.high_score)
            elif game.state == aws_cloudburst.GameState.CONTROLS:
                game.ui.draw_controls(game.screen)
            
            pygame.display.flip()
            game.clock.tick(60)
            frames += 1
        
        print(f"      ✅ Rendered {frames} frames successfully")
    
    print("\n🎯 Demo Summary:")
    print("   • Main Menu: Navigate with Up/Down arrows, select with SPACE")
    print("   • High Scores: Shows best score and AWS certification achievements")
    print("   • Controls: Complete game instructions and AWS services info")
    print("   • All screens: Press ESC or SPACE to return to main menu")
    
    pygame.quit()
    print("\n🎮 Menu Demo Complete!")
    print("The game now has fully functional High Scores and Controls pages!")

if __name__ == "__main__":
    try:
        demo_menu_screens()
    except KeyboardInterrupt:
        print("\n⏹️  Demo interrupted by user")
        pygame.quit()
    except Exception as e:
        print(f"❌ Demo error: {e}")
        pygame.quit()
        sys.exit(1)
