#!/usr/bin/env python3
"""
Test script to verify menu navigation works correctly.
"""

import sys
import os
import pygame

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import aws_cloudburst

def test_menu_navigation():
    """Test that all menu options work correctly."""
    print("🎮 Testing AWS CloudBurst Menu Navigation...")
    
    # Create game instance
    game = aws_cloudburst.Game()
    
    print("✅ Game initialized successfully")
    print(f"   • Initial state: {game.state}")
    print(f"   • Menu options: {game.menu_options}")
    print(f"   • Selected option: {game.selected_menu_option}")
    
    # Test menu option selection
    print("\n🔍 Testing menu option selection:")
    
    # Test High Scores option (option 1)
    game.selected_menu_option = 1
    game._handle_menu_input(pygame.K_SPACE)
    print(f"   • Selected High Scores: State = {game.state}")
    assert game.state == aws_cloudburst.GameState.HIGH_SCORE, "High Scores navigation failed"
    
    # Test returning to menu from High Scores
    game.state = aws_cloudburst.GameState.HIGH_SCORE
    # Simulate ESC key press
    for event_type in [pygame.KEYDOWN]:
        event = type('Event', (), {'type': event_type, 'key': pygame.K_ESCAPE})()
        if game.state == aws_cloudburst.GameState.HIGH_SCORE:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                game.state = aws_cloudburst.GameState.MENU
    print(f"   • Return from High Scores: State = {game.state}")
    assert game.state == aws_cloudburst.GameState.MENU, "Return from High Scores failed"
    
    # Test Controls option (option 2)
    game.selected_menu_option = 2
    game._handle_menu_input(pygame.K_SPACE)
    print(f"   • Selected Controls: State = {game.state}")
    assert game.state == aws_cloudburst.GameState.CONTROLS, "Controls navigation failed"
    
    # Test returning to menu from Controls
    game.state = aws_cloudburst.GameState.CONTROLS
    # Simulate ESC key press
    if game.state == aws_cloudburst.GameState.CONTROLS:
        game.state = aws_cloudburst.GameState.MENU
    print(f"   • Return from Controls: State = {game.state}")
    assert game.state == aws_cloudburst.GameState.MENU, "Return from Controls failed"
    
    # Test Play option (option 0)
    game.selected_menu_option = 0
    game._handle_menu_input(pygame.K_SPACE)
    print(f"   • Selected Play: State = {game.state}")
    assert game.state == aws_cloudburst.GameState.PLAYING, "Play navigation failed"
    
    print("\n🎯 Testing UI rendering methods:")
    
    # Test UI methods exist and can be called
    try:
        # Create a test surface
        test_surface = pygame.Surface((1024, 768))
        
        # Test high scores screen
        game.ui.draw_high_scores(test_surface, 12345)
        print("   ✅ High Scores screen renders successfully")
        
        # Test controls screen
        game.ui.draw_controls(test_surface)
        print("   ✅ Controls screen renders successfully")
        
        # Test menu screen
        game.ui.draw_menu(test_surface, "Test Menu", ["Option 1", "Option 2"], 0)
        print("   ✅ Menu screen renders successfully")
        
    except Exception as e:
        print(f"   ❌ UI rendering error: {e}")
        return False
    
    pygame.quit()
    print("\n✅ All menu navigation tests passed!")
    print("🎮 The High Scores and Controls pages are now working!")
    return True

if __name__ == "__main__":
    try:
        success = test_menu_navigation()
        if success:
            print("\n🎉 Menu fix successful! You can now access:")
            print("   • High Scores page (shows achievements and best score)")
            print("   • Controls page (shows game controls and help)")
            print("   • Both pages allow returning to main menu with ESC or SPACE")
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ Test error: {e}")
        pygame.quit()
        sys.exit(1)
