# AWS CloudBurst

A retro arcade-style Breakout game that combines classic 8-bit gaming aesthetics with AWS corporate branding and cloud computing themes. Break through AWS service blocks using your Load Balancer paddle and AWS Q Developer ball!

![AWS CloudBurst](https://img.shields.io/badge/AWS-CloudBurst-FF9900?style=for-the-badge&logo=amazon-aws)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python)
![Pygame](https://img.shields.io/badge/Pygame-2.1+-00599C?style=for-the-badge)

## Overview

AWS CloudBurst transforms the classic Breakout arcade game into an engaging AWS-themed experience. Players control a Load Balancer paddle to bounce an AWS Q Developer packet (ball) and destroy blocks representing various AWS services. Each level represents common AWS architectures, from basic web applications to complex machine learning workflows.

### Key Features

- **Authentic AWS Branding**: Professional AWS visual design throughout
  - **AWS Q Developer Ball**: Gradient effects, AI branding, and AWS logo elements
  - **AWS-Branded Paddle**: Iconic AWS smile curve and official branding
  - **Service-Specific Icons**: Each AWS service has its own recognizable icon
- **Progressive Difficulty**: 4+ levels with increasing complexity and speed
- **Power-Up System**: 6 different power-ups themed around AWS services
- **Retro Aesthetics**: 8-bit style graphics with modern smooth gameplay
- **Educational Value**: Learn AWS service relationships through gameplay
- **High Score System**: Persistent score tracking with local storage
- **Complete Menu System**: High scores, controls, and help screens

### AWS Branding Details

#### 🏀 AWS Q Developer Ball
- **Gradient Visual Effects**: Orange-to-white gradient for professional appearance
- **AI Branding**: Large 'Q' with 'AI' indicator showcasing Q Developer
- **AWS Logo Elements**: Branding dots around perimeter
- **Enhanced Trails**: Smooth motion effects with AWS orange coloring

#### 🏓 AWS-Branded Paddle  
- **Iconic AWS Smile**: Features the famous AWS logo smile curve
- **Professional Styling**: Gradient background with AWS text branding
- **Visual Feedback**: Green color when extended (Auto Scaling power-up)
- **Cloud Indicators**: Small dots representing distributed cloud services

#### 🧱 AWS Service Block Icons
Each block features authentic service-specific iconography:

**Tier 1 Services (1 hit)**
- **S3**: Bucket icon with storage representation
- **Lambda**: λ (lambda) symbol for serverless functions  
- **CloudWatch**: Graph lines for monitoring and observability

**Tier 2 Services (2 hits)**
- **EC2**: Server icon with horizontal lines
- **RDS**: Database cylinder representation
- **API Gateway**: Connected circles for API routing

**Tier 3 Services (3 hits)**
- **EKS**: Hexagon for Kubernetes container orchestration
- **SageMaker**: Neural network nodes and connections
- **Bedrock**: Diamond/gem shape for AI foundation models

**Special Services**
- **Q Developer**: Enhanced Q logo with special effects
- **CloudFormation**: Stacked layers for infrastructure as code
- **Auto Scaling**: Up/down arrows for automatic scaling

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Quick Start

1. **Clone or download the game files**:
   ```bash
   # If using git
   git clone <repository-url>
   cd aws-cloudburst
   
   # Or download aws_cloudburst.py directly
   ```

2. **Install dependencies**:
   ```bash
   pip install pygame>=2.1.0
   ```

3. **Run the game**:
   ```bash
   python aws_cloudburst.py
   ```

### Alternative Installation

If you prefer using a virtual environment:

```bash
# Create virtual environment
python -m venv aws_cloudburst_env

# Activate virtual environment
# On Windows:
aws_cloudburst_env\Scripts\activate
# On macOS/Linux:
source aws_cloudburst_env/bin/activate

# Install dependencies
pip install pygame>=2.1.0

# Run the game
python aws_cloudburst.py
```

## How to Play

### Objective

Destroy all AWS service blocks on each level using your Load Balancer paddle to bounce the AWS Q Developer ball. Complete increasingly complex AWS architecture patterns while collecting power-ups and avoiding losing all your lives.

### Controls

| Key | Action |
|-----|--------|
| **Arrow Keys** or **A/D** | Move Load Balancer paddle left/right |
| **P** or **ESC** | Pause/Resume game |
| **SPACE** | Select menu option / Play again |
| **Up/Down Arrows** | Navigate menus |
| **ESC** | Return to main menu (from game over, high scores, or controls) |

### Menu System

The game features a complete menu system with the following screens:

#### Main Menu
- **Play**: Start a new game
- **High Scores**: View your best score and AWS certification achievements
- **Controls**: View game controls, instructions, and AWS services information
- **Quit**: Exit the game

#### High Scores Screen
- Displays your current high score
- Shows AWS certification achievement levels:
  - AWS Novice (1,000+ points)
  - Cloud Practitioner (5,000+ points)
  - Solutions Architect (15,000+ points)
  - DevOps Engineer (30,000+ points)
  - Cloud Expert (50,000+ points)

#### Controls & Help Screen
- Complete game controls reference
- Gameplay instructions and tips
- Information about AWS services featured in the game
- Power-up explanations

*All menu screens allow returning to the main menu by pressing ESC or SPACE.*

### Gameplay Mechanics

#### Ball Physics
- **Initial Speed**: 300 pixels/second
- **Speed Increase**: 5% per level completion
- **Maximum Speed**: 600 pixels/second (maintains playability)
- **Paddle Interaction**: Ball angle varies based on hit position
  - Center hit: Straight bounce
  - Edge hits: Angled bounces for strategic play

#### Scoring System
- **Tier 1 Blocks**: 10 points (S3, Lambda, CloudWatch)
- **Tier 2 Blocks**: 25 points (EC2, RDS, API Gateway)
- **Tier 3 Blocks**: 50 points (EKS, SageMaker, Bedrock)
- **Special Blocks**: 50-100 points (Q Developer, CloudFormation, Auto Scaling)
- **Life Bonus**: 100 points per remaining life at level completion
- **Score Multiplier**: 2x points when active (power-up)

#### Lives System
- Start with 3 lives
- Lose a life when all balls fall off screen
- Game over when all lives are lost

## AWS Services Featured

### Tier 1 Services (1 hit to destroy)
- **Amazon S3**: Simple Storage Service - Blue bucket icon
- **AWS Lambda**: Serverless compute - Orange lambda symbol
- **Amazon CloudWatch**: Monitoring and observability - Green graph icon

### Tier 2 Services (2 hits to destroy)
- **Amazon EC2**: Elastic Compute Cloud - Orange server icon
- **Amazon RDS**: Relational Database Service - Blue database icon
- **Amazon API Gateway**: API management - Purple gateway icon

### Tier 3 Services (3 hits to destroy)
- **Amazon EKS**: Elastic Kubernetes Service - Blue container icon
- **Amazon SageMaker**: Machine learning platform - Green AI icon
- **Amazon Bedrock**: Generative AI service - Purple rock icon

### Special Services
- **AWS Q Developer**: AI-powered coding assistant - Triggers multi-ball
- **AWS CloudFormation**: Infrastructure as code - Rebuilds formations
- **AWS Auto Scaling**: Automatic scaling - Enlarges paddle temporarily

## Power-Up System

Collect power-ups by catching them with your paddle when they drop from destroyed Tier 2+ blocks (15% chance).

### Available Power-Ups

1. **Multi-Ball** (AWS Q Developer)
   - **Effect**: Spawns 2 additional balls
   - **Duration**: Until balls are lost
   - **Strategy**: Increases block destruction rate

2. **Paddle Extend** (Auto Scaling)
   - **Effect**: Increases paddle width by 50%
   - **Duration**: 15 seconds
   - **Strategy**: Easier ball control and catching

3. **Slow Motion** (CloudWatch)
   - **Effect**: Reduces ball speed by 30%
   - **Duration**: 10 seconds
   - **Strategy**: Precision control for difficult shots

4. **Laser Paddle** (Lambda)
   - **Effect**: Allows shooting projectiles upward
   - **Duration**: 20 seconds
   - **Strategy**: Direct block destruction

5. **Shield** (WAF - Web Application Firewall)
   - **Effect**: Creates temporary barrier above paddle
   - **Duration**: 30 seconds
   - **Strategy**: Protection from ball loss

6. **Score Multiplier** (Cost Optimizer)
   - **Effect**: Doubles all points earned
   - **Duration**: 15 seconds
   - **Strategy**: Maximize scoring opportunities

## Level Progression

### Level 1: Basic Infrastructure
- **Theme**: Simple S3 and Lambda deployment
- **Layout**: Basic rows of Tier 1 services
- **Focus**: Learning basic ball control

### Level 2: Web Application Architecture
- **Theme**: Three-tier web application
- **Layout**: API Gateway → EC2 → RDS formation
- **Focus**: Understanding load balancing concepts

### Level 3: Serverless Architecture
- **Theme**: Event-driven serverless application
- **Layout**: API Gateway, Lambda, S3, CloudWatch with special blocks
- **Focus**: Introduction to power-ups and special mechanics

### Level 4: Machine Learning Workflow
- **Theme**: End-to-end ML pipeline
- **Layout**: S3 → SageMaker → Bedrock → EKS formation
- **Focus**: Complex patterns and all service tiers

### Level 5+: Advanced Architectures
- **Theme**: Mixed enterprise patterns
- **Layout**: Complex formations with all services
- **Focus**: Mastery of all game mechanics

## Technical Details

### Architecture Overview

The game is built using object-oriented design principles with clear separation of concerns:

```
Game (Main Controller)
├── Paddle (Load Balancer)
├── Ball (AWS Q Developer packet)
├── Level (AWS Architecture layouts)
├── Block (AWS Services)
├── PowerUp (Service enhancements)
├── UI (Interface rendering)
└── AudioManager (Sound effects)
```

### Key Classes

- **Game**: Main game loop, state management, and coordination
- **Paddle**: Player-controlled Load Balancer with movement and power-ups
- **Ball**: Physics-enabled AWS Q Developer packet with collision detection
- **Block**: AWS service representations with hit points and scoring
- **Level**: Architecture patterns and block arrangements
- **PowerUp**: Collectible enhancements with timed effects
- **UI**: Menu systems and HUD rendering
- **AudioManager**: Retro sound effects and audio feedback

### Performance Features

- **60 FPS Target**: Smooth gameplay with consistent frame timing
- **Efficient Collision Detection**: Optimized rectangle-based collision system
- **Memory Management**: Proper cleanup of game objects and surfaces
- **Sprite Groups**: Efficient rendering and update cycles
- **Delta Time**: Frame-rate independent physics calculations

### File Structure

```
aws-cloudburst/
├── aws_cloudburst.py          # Main game file (complete implementation)
├── README.md                  # This documentation
├── requirements.txt           # Python dependencies
├── high_score.json           # High score storage (created automatically)
└── assets/                   # Future expansion for external assets
```

## Development

### Code Structure

The game follows Python best practices with:

- **Type Hints**: Full type annotation throughout
- **Docstrings**: Comprehensive documentation for all classes and methods
- **Error Handling**: Graceful handling of file operations and pygame events
- **Constants**: Configuration values clearly defined at module level
- **Clean Architecture**: Modular design with single responsibility principle

### Customization Options

#### Difficulty Adjustment
Modify these constants in the code:
```python
BALL_INITIAL_SPEED = 300        # Starting ball speed
BALL_SPEED_INCREASE = 0.05      # Speed increase per level (5%)
BALL_MAX_SPEED = 600           # Maximum ball speed
PADDLE_SPEED = 400             # Paddle movement speed
```

#### Visual Customization
AWS color palette can be adjusted:
```python
AWS_ORANGE = (255, 153, 0)      # Primary brand color
AWS_DARK_BLUE = (35, 47, 62)    # Background color
AWS_GREEN = (122, 161, 22)      # Success/power-up color
```

#### Game Balance
Power-up and scoring can be tuned:
```python
# Power-up drop chance (15% default)
if destroyed and block.block_type.value[1] >= 2 and random.random() < 0.15:

# Score multiplier values
TIER_1_POINTS = 10
TIER_2_POINTS = 25
TIER_3_POINTS = 50
```

### Adding New Features

#### New AWS Services
1. Add to `BlockType` enum with appropriate properties
2. Update level generation methods to include new service
3. Add visual representation in `Block.draw()` method

#### New Power-Ups
1. Add to `PowerUpType` enum with duration and color
2. Implement activation logic in `Game._activate_powerup()`
3. Add deactivation logic in `Game._deactivate_powerup()`

#### New Levels
1. Create new generation method in `Level` class
2. Add to `Level.generate_level()` switch statement
3. Design block patterns representing AWS architectures

## Troubleshooting

### Common Issues

#### Game Won't Start
- **Check Python Version**: Ensure Python 3.8+ is installed
- **Install Pygame**: Run `pip install pygame>=2.1.0`
- **Check File Permissions**: Ensure aws_cloudburst.py is executable

#### Performance Issues
- **Lower FPS**: Modify `FPS = 60` to a lower value (30 or 45)
- **Reduce Effects**: Comment out trail rendering in `Ball.draw()`
- **Simplify Audio**: Set `AudioManager.sounds_enabled = False`

#### Audio Problems
- **No Sound**: Check system audio settings and pygame mixer initialization
- **Audio Errors**: Install additional audio codecs or disable audio in AudioManager

#### High Score Not Saving
- **File Permissions**: Ensure write permissions in game directory
- **Disk Space**: Check available disk space for high_score.json

### System Requirements

#### Minimum Requirements
- **OS**: Windows 7+, macOS 10.12+, or Linux with X11
- **Python**: 3.8 or higher
- **RAM**: 256 MB available
- **Storage**: 50 MB free space
- **Display**: 1024x768 resolution or higher

#### Recommended Requirements
- **OS**: Windows 10+, macOS 10.15+, or modern Linux distribution
- **Python**: 3.9 or higher
- **RAM**: 512 MB available
- **Storage**: 100 MB free space
- **Display**: 1920x1080 resolution
- **Audio**: Sound card with speakers or headphones

## Contributing

This game was created as part of the AWS Build Game Challenge. While it's a complete implementation, potential enhancements could include:

### Suggested Improvements
- **Additional AWS Services**: More block types representing newer services
- **Advanced Power-Ups**: Service-specific abilities (e.g., CloudFront caching)
- **Multiplayer Mode**: Competitive or cooperative gameplay
- **Level Editor**: Custom architecture design tools
- **Enhanced Audio**: Background music and improved sound effects
- **Visual Effects**: Particle systems and animations
- **Mobile Support**: Touch controls and responsive design

### Code Quality
- All code follows PEP 8 style guidelines
- Comprehensive error handling and logging
- Unit tests for core game mechanics
- Performance profiling and optimization
- Cross-platform compatibility testing

## Credits

### Development
- **Game Engine**: Pygame Community
- **AWS Branding**: Amazon Web Services (used with respect for educational purposes)
- **Inspiration**: Classic Breakout arcade games
- **Architecture**: Modern object-oriented Python practices

### AWS Services Referenced
This game respectfully references AWS services for educational and entertainment purposes. All AWS trademarks and service names are property of Amazon Web Services, Inc.

### Open Source Libraries
- **Pygame**: Cross-platform game development library
- **Python**: Programming language and standard library

## License

This project is created for educational and entertainment purposes as part of the AWS Build Game Challenge. The code is provided as-is for learning and modification.

### Usage Rights
- ✅ Personal use and modification
- ✅ Educational purposes
- ✅ Learning game development concepts
- ✅ Understanding AWS service relationships

### Restrictions
- ❌ Commercial distribution without permission
- ❌ Misrepresentation of AWS services or branding
- ❌ Use of AWS trademarks outside educational context

---

**Enjoy playing AWS CloudBurst and learning about AWS services through gaming!**

For questions, issues, or suggestions, please refer to the troubleshooting section or create an issue in the project repository.

*Built with ❤️ for the AWS community and retro gaming enthusiasts.*
