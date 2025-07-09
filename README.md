# AWS CloudBurst 🎮

A retro-style Breakout game featuring AWS services and Q Developer branding, built for the AWS Build Game Challenge.

## 🚀 Quick Start

```bash
# Install dependencies
pip install pygame

# Run the game
python aws_cloudburst.py
```

## 🎮 How to Play

- **Move Paddle**: Arrow keys or A/D
- **Fire Lasers**: SPACE (when Laser Paddle power-up is active)
- **Pause**: P or ESC
- **Menu Navigation**: Arrow keys + Enter/Space

## ⚡ Power-Ups

- 🔴 **Laser Paddle** - Fire destructive lasers
- 🔵 **Slow Motion** - Reduce ball speed by 30%
- ⚪ **Shield** - Protective barrier (3 hits)
- 🟢 **Paddle Extend** - 50% wider paddle
- 🟠 **Multi-Ball** - Spawn 2 additional balls
- 🟡 **Score Multiplier** - Double your points

## 🏗️ AWS Services Featured

**Tier 1**: S3, Lambda, CloudWatch  
**Tier 2**: EC2, RDS, API Gateway  
**Tier 3**: EKS, SageMaker, Bedrock  
**Special**: Q Developer, CloudFormation, Auto Scaling

## 📁 Project Structure

```
aws-build-game-challenge/
├── aws_cloudburst.py      # Main game file
├── requirements.txt       # Dependencies
├── high_score.json       # High score storage
├── demos/                # Demo versions
├── tests/                # Test files
└── docs/                 # Documentation
    ├── RELEASE_NOTES.md  # Version history
    └── ...               # Other docs
```

## 🔄 Latest Updates (v1.1.0)

- ✅ All 6 power-ups now fully functional
- ✅ Fixed game crashes on power-up pickup
- ✅ Fixed laser always firing bug
- ✅ Implemented missing Slow Motion and Shield
- ✅ Increased power-up drop rate to 25%
- ✅ Complete menu system functionality

See [RELEASE_NOTES.md](docs/RELEASE_NOTES.md) for full changelog.

## 🎯 Game Features

- **Professional AWS Branding** throughout
- **4+ Levels** representing AWS architectures
- **Retro Aesthetics** with modern polish
- **Complete Menu System** with high scores
- **60 FPS Gameplay** with smooth animations
- **Enhanced Visual Effects** and sound

## 🛠️ Development

Built with Python and Pygame, featuring:
- Object-oriented design
- Proper collision detection
- State management
- Professional AWS theming

---

*Built for the AWS Build Game Challenge - Combining classic gaming with cloud education!*
