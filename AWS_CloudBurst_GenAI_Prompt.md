# AWS CloudBurst - Comprehensive GenAI Development Prompt

## Project Overview
You are tasked with creating "AWS CloudBurst," a retro arcade-style Breakout game that combines classic 8-bit gaming aesthetics with AWS corporate branding and cloud computing themes. This must be a complete, playable Python game using pygame that can be run locally.

## Core Requirements

### 1. Technical Specifications
- **Language**: Python 3.8+
- **Framework**: pygame library
- **Architecture**: Object-oriented design with clear class separation
- **File Structure**: Single main game file with modular class design
- **Performance**: 60 FPS target, smooth gameplay
- **Resolution**: 1024x768 pixels (4:3 aspect ratio for retro feel)

### 2. Visual Design & Branding

#### Color Palette (Official AWS Colors)
- **Primary Orange**: #FF9900 (AWS signature color)
- **Dark Blue**: #232F3E (AWS dark background)
- **Light Gray**: #F2F3F3 (secondary elements)
- **White**: #FFFFFF (text and highlights)
- **Success Green**: #7AA116 (power-ups, positive feedback)
- **Warning Red**: #D13212 (danger, negative feedback)

#### Typography & UI
- **Font**: Monospace font (Courier New or similar) for retro feel
- **UI Elements**: Pixelated, 8-bit style borders and buttons
- **Score Display**: Top-left corner, large retro font
- **Lives Display**: Top-right corner with heart icons
- **Level Display**: Center-top

#### Visual Assets Requirements
- All AWS service logos must be accurately represented as block sprites
- Paddle design should resemble a load balancer icon
- Ball should have AWS Q Developer branding/styling
- Background should feature subtle AWS cloud patterns
- Particle effects for block destruction should use AWS orange

### 3. Game Mechanics & Physics

#### Ball Physics
- **Initial Speed**: 300 pixels/second
- **Speed Increase**: 5% per level completion
- **Bounce Mechanics**: Realistic angle reflection off paddle and walls
- **Paddle Interaction**: Ball angle varies based on hit position (center = straight, edges = angled)
- **Maximum Speed**: Cap at 600 pixels/second to maintain playability

#### Paddle Mechanics
- **Size**: 120x20 pixels (Load Balancer themed)
- **Speed**: 400 pixels/second
- **Controls**: Arrow keys or A/D keys
- **Boundaries**: Cannot move beyond screen edges
- **Visual**: AWS Load Balancer icon styling

#### Block System
- **Block Types**: Each represents a different AWS service
- **Durability**: 1-3 hits depending on service tier
- **Point Values**: 10-50 points based on service complexity
- **Special Blocks**: Some blocks trigger power-ups when destroyed

### 4. AWS Service Integration (Block Types)

#### Tier 1 Blocks (1 hit, 10 points)
- **S3**: Simple Storage Service (blue bucket icon)
- **Lambda**: Serverless compute (orange lambda symbol)
- **CloudWatch**: Monitoring (green graph icon)

#### Tier 2 Blocks (2 hits, 25 points)
- **EC2**: Elastic Compute Cloud (orange server icon)
- **RDS**: Relational Database Service (blue database icon)
- **API Gateway**: API management (purple gateway icon)

#### Tier 3 Blocks (3 hits, 50 points)
- **EKS**: Kubernetes service (blue container icon)
- **SageMaker**: Machine learning (green AI icon)
- **Bedrock**: Generative AI (purple rock icon)

#### Special Blocks
- **AWS Q Developer**: Triggers multi-ball power-up
- **CloudFormation**: Rebuilds destroyed blocks in formation
- **Auto Scaling**: Temporarily enlarges paddle

### 5. Power-Up System

#### Power-Up Types
1. **Multi-Ball** (AWS Q Developer): Spawns 2 additional balls
2. **Paddle Extend** (Auto Scaling): Increases paddle width by 50% for 15 seconds
3. **Slow Motion** (CloudWatch): Reduces ball speed by 30% for 10 seconds
4. **Laser Paddle** (Lambda): Allows shooting projectiles for 20 seconds
5. **Shield** (WAF): Creates temporary barrier above paddle
6. **Score Multiplier** (Cost Optimizer): 2x points for 15 seconds

#### Power-Up Mechanics
- 15% chance of dropping when destroying Tier 2+ blocks
- Power-ups fall at 150 pixels/second
- Must be caught by paddle to activate
- Visual indicators show remaining time for temporary power-ups
- Maximum 1 active power-up per type

### 6. Level Design

#### Level Progression
- **Level 1**: Basic S3 and Lambda blocks in simple rows
- **Level 2**: Mixed Tier 1 and 2 blocks with gaps
- **Level 3**: All tiers with special blocks introduced
- **Level 4+**: Complex formations resembling AWS architecture diagrams

#### Level Layouts
Each level should represent common AWS architectures:
- **Web Application**: Load balancer, EC2, RDS formation
- **Serverless**: API Gateway, Lambda, DynamoDB pattern
- **Data Pipeline**: S3, Glue, Redshift arrangement
- **ML Workflow**: SageMaker, S3, Bedrock configuration

### 7. Game States & Flow

#### State Management
```python
class GameState(Enum):
    MENU = "menu"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"
    LEVEL_COMPLETE = "level_complete"
    HIGH_SCORE = "high_score"
```

#### Menu System
- **Main Menu**: Play, High Scores, Controls, Quit
- **Pause Menu**: Resume, Restart Level, Main Menu
- **Game Over**: Final Score, High Score Entry, Play Again

### 8. Audio Requirements

#### Sound Effects
- **Ball Bounce**: Retro beep sound
- **Block Destruction**: Different tones for each service tier
- **Power-Up Collection**: AWS notification sound
- **Level Complete**: Success fanfare
- **Game Over**: Dramatic failure sound

#### Background Music
- Chiptune-style background music
- Different tracks for menu and gameplay
- Volume controls in settings

### 9. Code Architecture Requirements

#### Main Classes
```python
class Game:
    # Main game loop and state management
    
class Paddle:
    # Player-controlled load balancer
    
class Ball:
    # AWS Q Developer packet with physics
    
class Block:
    # AWS service blocks with different properties
    
class PowerUp:
    # Collectible enhancements
    
class Level:
    # Level data and block arrangements
    
class UI:
    # Score, lives, and menu rendering
    
class AudioManager:
    # Sound effects and music
```

#### Code Quality Standards
- Comprehensive docstrings for all classes and methods
- Type hints throughout the codebase
- Error handling for file operations and pygame events
- Configuration constants at the top of the file
- Clean separation of concerns between classes

### 10. Performance Optimization

#### Rendering Optimization
- Sprite groups for efficient collision detection
- Dirty rectangle updates where possible
- Optimized image loading and caching
- Minimal garbage collection during gameplay

#### Memory Management
- Proper cleanup of pygame surfaces
- Efficient sprite management
- Resource pooling for frequently created objects

### 11. User Experience Features

#### Accessibility
- High contrast mode option
- Keyboard navigation for all menus
- Clear visual feedback for all interactions
- Adjustable game speed settings

#### Quality of Life
- Auto-pause when window loses focus
- Save high scores locally
- Customizable controls
- Level skip option (for testing)

### 12. Documentation Requirements

#### README.md Structure
```markdown
# AWS CloudBurst

## Overview
Brief description of the game and its AWS theming

## Installation
Step-by-step setup instructions

## How to Play
Game controls and objectives

## AWS Services Featured
List of all AWS services represented in the game

## Technical Details
Architecture overview and key features

## Development
Code structure and modification guide

## Credits
Attribution and licensing information
```

#### Code Documentation
- Header comment explaining the game concept
- Inline comments for complex algorithms
- Class and method docstrings with parameter descriptions
- Configuration section with clear variable names

### 13. Testing & Validation

#### Functional Testing
- All power-ups work correctly
- Ball physics behave realistically
- Level progression functions properly
- Score calculation is accurate

#### Performance Testing
- Maintains 60 FPS during normal gameplay
- No memory leaks during extended play
- Smooth animations and transitions

### 14. Deployment Preparation

#### File Organization
```
aws_cloudburst.py          # Main game file
README.md                  # Documentation
requirements.txt           # Python dependencies
assets/                    # Game assets (if external files needed)
  sounds/                  # Audio files
  images/                  # Sprite images (if not generated in code)
```

#### Dependencies
```
pygame>=2.1.0
```

## Implementation Guidelines

### Development Process
1. Start with basic game loop and window creation
2. Implement paddle movement and ball physics
3. Add block system with AWS service theming
4. Integrate power-up mechanics
5. Implement level progression
6. Add audio and visual polish
7. Create comprehensive documentation

### Code Style
- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Keep functions focused and under 50 lines when possible
- Use constants for all magic numbers
- Implement proper error handling

### AWS Theming Integration
- Every game element should have clear AWS connection
- Use official AWS service descriptions in tooltips/help
- Maintain professional appearance while being fun
- Include subtle educational elements about AWS services

## Success Criteria

The completed game must:
1. Run without errors on Python 3.8+ with pygame installed
2. Provide smooth, engaging gameplay for 15+ minutes
3. Accurately represent AWS services and branding
4. Include all specified power-ups and mechanics
5. Have comprehensive documentation
6. Demonstrate professional code quality
7. Be immediately playable after following README instructions

## Final Notes

This prompt should result in a production-quality game that serves as both entertainment and a subtle introduction to AWS services. The code should be clean enough to serve as a learning resource for game development while showcasing AWS branding in a creative, engaging way.

The AI should prioritize creating a complete, working game over adding extra features not specified in this prompt. Every requirement listed above should be implemented before considering additional enhancements.
