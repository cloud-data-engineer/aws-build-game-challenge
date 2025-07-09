#!/usr/bin/env python3
"""
AWS CloudBurst - A Retro Arcade Breakout Game with AWS Theming

This game combines classic Breakout mechanics with AWS service branding,
featuring a Load Balancer paddle, AWS Q Developer ball, and blocks representing
various AWS services. Each level represents common AWS architectures.

Author: Generated for AWS Build Game Challenge
License: MIT
"""

import pygame
import math
import random
import json
import os
from enum import Enum
from typing import List, Tuple, Optional, Dict, Any
from dataclasses import dataclass

# Initialize Pygame
pygame.init()

# Configuration Constants
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
FPS = 60

# AWS Official Color Palette
AWS_ORANGE = (255, 153, 0)      # #FF9900
AWS_DARK_BLUE = (35, 47, 62)    # #232F3E
AWS_LIGHT_GRAY = (242, 243, 243) # #F2F3F3
AWS_WHITE = (255, 255, 255)      # #FFFFFF
AWS_GREEN = (122, 161, 22)       # #7AA116
AWS_RED = (209, 50, 18)          # #D13212

# Game Physics Constants
BALL_INITIAL_SPEED = 300
BALL_SPEED_INCREASE = 0.05
BALL_MAX_SPEED = 600
PADDLE_SPEED = 400
PADDLE_WIDTH = 120
PADDLE_HEIGHT = 20
POWERUP_FALL_SPEED = 150

# Block Configuration
BLOCK_WIDTH = 80
BLOCK_HEIGHT = 30
BLOCKS_PER_ROW = 12
BLOCK_ROWS = 8

class GameState(Enum):
    """Game state enumeration for state management."""
    MENU = "menu"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"
    LEVEL_COMPLETE = "level_complete"
    HIGH_SCORE = "high_score"
    CONTROLS = "controls"

class BlockType(Enum):
    """AWS Service block types with their properties."""
    # Tier 1 Blocks (1 hit, 10 points)
    S3 = ("S3", 1, 10, (52, 144, 220))          # Blue
    LAMBDA = ("Lambda", 1, 10, AWS_ORANGE)       # Orange
    CLOUDWATCH = ("CloudWatch", 1, 10, AWS_GREEN) # Green
    
    # Tier 2 Blocks (2 hits, 25 points)
    EC2 = ("EC2", 2, 25, AWS_ORANGE)            # Orange
    RDS = ("RDS", 2, 25, (52, 144, 220))        # Blue
    API_GATEWAY = ("API Gateway", 2, 25, (147, 102, 204)) # Purple
    
    # Tier 3 Blocks (3 hits, 50 points)
    EKS = ("EKS", 3, 50, (52, 144, 220))        # Blue
    SAGEMAKER = ("SageMaker", 3, 50, AWS_GREEN)  # Green
    BEDROCK = ("Bedrock", 3, 50, (147, 102, 204)) # Purple
    
    # Special Blocks
    Q_DEVELOPER = ("Q Developer", 1, 100, AWS_ORANGE)
    CLOUDFORMATION = ("CloudFormation", 2, 75, AWS_RED)
    AUTO_SCALING = ("Auto Scaling", 1, 50, AWS_GREEN)

class PowerUpType(Enum):
    """Power-up types with their properties."""
    MULTI_BALL = ("Multi-Ball", 15, AWS_ORANGE)
    PADDLE_EXTEND = ("Paddle Extend", 15, AWS_GREEN)
    SLOW_MOTION = ("Slow Motion", 10, (52, 144, 220))
    LASER_PADDLE = ("Laser Paddle", 20, AWS_RED)
    SHIELD = ("Shield", 30, AWS_LIGHT_GRAY)
    SCORE_MULTIPLIER = ("Score Multiplier", 15, (255, 215, 0))

@dataclass
class Vector2D:
    """2D Vector class for position and velocity calculations."""
    x: float
    y: float
    
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)
    
    def magnitude(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def normalize(self):
        mag = self.magnitude()
        if mag > 0:
            return Vector2D(self.x / mag, self.y / mag)
        return Vector2D(0, 0)

class Ball:
    """AWS Q Developer packet - the game ball with physics."""
    
    def __init__(self, x: float, y: float, speed: float = BALL_INITIAL_SPEED):
        self.position = Vector2D(x, y)
        self.velocity = Vector2D(random.choice([-1, 1]), -1).normalize() * speed
        self.radius = 8
        self.speed = speed
        self.trail_positions = []
        
    def update(self, dt: float) -> None:
        """Update ball position and handle wall collisions."""
        # Store trail positions for visual effect
        self.trail_positions.append((self.position.x, self.position.y))
        if len(self.trail_positions) > 5:
            self.trail_positions.pop(0)
            
        # Update position
        self.position = self.position + self.velocity * dt
        
        # Wall collisions
        if self.position.x <= self.radius or self.position.x >= SCREEN_WIDTH - self.radius:
            self.velocity.x = -self.velocity.x
            self.position.x = max(self.radius, min(SCREEN_WIDTH - self.radius, self.position.x))
            
        if self.position.y <= self.radius:
            self.velocity.y = -self.velocity.y
            self.position.y = self.radius
    
    def bounce_off_paddle(self, paddle_x: float, paddle_width: float) -> None:
        """Handle ball collision with paddle."""
        # Calculate hit position relative to paddle center (-1 to 1)
        hit_pos = (self.position.x - paddle_x) / (paddle_width / 2)
        hit_pos = max(-1, min(1, hit_pos))  # Clamp to [-1, 1]
        
        # Calculate new velocity based on hit position
        angle = hit_pos * math.pi / 3  # Max 60 degrees
        speed = self.velocity.magnitude()
        
        self.velocity = Vector2D(math.sin(angle) * speed, -abs(math.cos(angle)) * speed)
    
    def draw(self, screen: pygame.Surface) -> None:
        """Draw the AWS Q Developer ball with enhanced logo design."""
        # Draw trail
        for i, pos in enumerate(self.trail_positions):
            alpha = (i + 1) / len(self.trail_positions) * 100
            trail_surface = pygame.Surface((self.radius * 2, self.radius * 2))
            trail_surface.set_alpha(alpha)
            pygame.draw.circle(trail_surface, AWS_ORANGE, (self.radius, self.radius), self.radius)
            screen.blit(trail_surface, (pos[0] - self.radius, pos[1] - self.radius))
        
        # Draw main ball with gradient effect
        center_x, center_y = int(self.position.x), int(self.position.y)
        
        # Draw multiple circles for gradient effect (simplified)
        for i in range(self.radius, 0, -2):
            intensity = i / self.radius
            color = tuple(int(c * intensity) for c in AWS_ORANGE)
            pygame.draw.circle(screen, color, (center_x, center_y), i)
        
        # Draw outer ring
        pygame.draw.circle(screen, AWS_WHITE, (center_x, center_y), self.radius, 2)
        
        # Draw AWS Q Developer logo elements
        # Main Q shape
        font_size = max(10, self.radius)
        font = pygame.font.Font(None, font_size)
        
        # Draw Q with distinctive styling
        q_text = font.render("Q", True, AWS_WHITE)
        q_rect = q_text.get_rect(center=(center_x, center_y - 1))
        screen.blit(q_text, q_rect)
        
        # Add small "AI" indicator below Q
        if self.radius >= 8:
            ai_font = pygame.font.Font(None, max(8, self.radius // 2))
            ai_text = ai_font.render("AI", True, AWS_WHITE)
            ai_rect = ai_text.get_rect(center=(center_x, center_y + self.radius // 2))
            screen.blit(ai_text, ai_rect)
        
        # Add AWS branding dots around the Q
        if self.radius >= 6:
            dot_positions = [
                (center_x - self.radius + 2, center_y - 2),
                (center_x + self.radius - 2, center_y - 2),
                (center_x, center_y - self.radius + 2),
                (center_x, center_y + self.radius - 2)
            ]
            
            for dot_x, dot_y in dot_positions:
                pygame.draw.circle(screen, AWS_WHITE, (int(dot_x), int(dot_y)), 1)

class Paddle:
    """AWS Load Balancer - the player-controlled paddle."""
    
    def __init__(self, x: float, y: float):
        self.position = Vector2D(x, y)
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.speed = PADDLE_SPEED
        self.extended = False
        self.extend_timer = 0
        self.original_width = PADDLE_WIDTH
        
    def update(self, dt: float, keys_pressed: Dict) -> None:
        """Update paddle position based on input."""
        # Handle movement
        if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            self.position.x -= self.speed * dt
        if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            self.position.x += self.speed * dt
            
        # Keep paddle within screen bounds
        self.position.x = max(self.width / 2, min(SCREEN_WIDTH - self.width / 2, self.position.x))
        
        # Handle paddle extension timer
        if self.extended:
            self.extend_timer -= dt
            if self.extend_timer <= 0:
                self.extended = False
                self.width = self.original_width
    
    def extend_paddle(self, duration: float) -> None:
        """Activate paddle extension power-up."""
        self.extended = True
        self.extend_timer = duration
        self.width = self.original_width * 1.5
    
    def get_rect(self) -> pygame.Rect:
        """Get paddle collision rectangle."""
        return pygame.Rect(
            self.position.x - self.width / 2,
            self.position.y - self.height / 2,
            self.width,
            self.height
        )
    
    def draw(self, screen: pygame.Surface) -> None:
        """Draw the AWS-branded paddle with logo elements."""
        rect = self.get_rect()
        
        # Draw main paddle body with gradient effect
        color = AWS_GREEN if self.extended else AWS_ORANGE
        
        # Create gradient effect
        for i in range(rect.height):
            gradient_color = tuple(max(0, c - i * 3) for c in color)
            pygame.draw.rect(screen, gradient_color, 
                           (rect.left, rect.top + i, rect.width, 1))
        
        # Draw border
        pygame.draw.rect(screen, AWS_WHITE, rect, 2)
        
        # Draw AWS logo elements
        center_x, center_y = rect.centerx, rect.centery
        
        # AWS "smile" curve (iconic AWS logo element)
        # Draw the curved arrow/smile
        smile_points = []
        for i in range(11):  # 11 points for smooth curve
            angle = math.pi * i / 10  # 0 to π (half circle)
            x = center_x - 30 + i * 6
            y = center_y + 3 - int(3 * math.sin(angle))
            smile_points.append((x, y))
        
        if len(smile_points) > 2:
            pygame.draw.lines(screen, AWS_WHITE, False, smile_points, 2)
        
        # Draw arrow tip at the end of smile
        arrow_tip = [
            (center_x + 32, center_y + 1),
            (center_x + 28, center_y - 1),
            (center_x + 28, center_y + 3)
        ]
        pygame.draw.polygon(screen, AWS_WHITE, arrow_tip)
        
        # Draw "AWS" text
        if rect.width >= 80:  # Only draw text if paddle is wide enough
            font = pygame.font.Font(None, 16)
            aws_text = font.render("AWS", True, AWS_WHITE)
            text_rect = aws_text.get_rect(center=(center_x, center_y - 6))
            screen.blit(aws_text, text_rect)
        
        # Add small dots representing cloud services
        dot_positions = [
            (center_x - 40, center_y - 3),
            (center_x - 35, center_y + 2),
            (center_x + 35, center_y - 2),
            (center_x + 40, center_y + 3)
        ]
        
        for dot_x, dot_y in dot_positions:
            if rect.left < dot_x < rect.right:  # Only draw dots within paddle bounds
                pygame.draw.circle(screen, AWS_WHITE, (int(dot_x), int(dot_y)), 1)

class Block:
    """AWS Service block with different properties based on service type."""
    
    def __init__(self, x: float, y: float, block_type: BlockType):
        self.position = Vector2D(x, y)
        self.block_type = block_type
        self.width = BLOCK_WIDTH
        self.height = BLOCK_HEIGHT
        self.hits_remaining = block_type.value[1]
        self.max_hits = block_type.value[1]
        self.points = block_type.value[2]
        self.color = block_type.value[3]
        self.destroyed = False
        
    def hit(self) -> Tuple[int, bool]:
        """Handle block being hit. Returns (points, destroyed)."""
        self.hits_remaining -= 1
        if self.hits_remaining <= 0:
            self.destroyed = True
            return self.points, True
        return 0, False
    
    def get_rect(self) -> pygame.Rect:
        """Get block collision rectangle."""
        return pygame.Rect(
            self.position.x - self.width / 2,
            self.position.y - self.height / 2,
            self.width,
            self.height
        )
    
    def draw(self, screen: pygame.Surface) -> None:
        """Draw the AWS service block with service-specific icons."""
        if self.destroyed:
            return
            
        rect = self.get_rect()
        
        # Calculate color intensity based on remaining hits
        intensity = self.hits_remaining / self.max_hits
        color = tuple(int(c * intensity) for c in self.color)
        
        # Draw block with gradient effect
        for i in range(rect.height):
            gradient_color = tuple(max(0, c - i * 2) for c in color)
            pygame.draw.rect(screen, gradient_color, 
                           (rect.left, rect.top + i, rect.width, 1))
        
        # Draw border
        pygame.draw.rect(screen, AWS_WHITE, rect, 2)
        
        # Draw service-specific icon
        self._draw_service_icon(screen, rect)
        
        # Draw service name (smaller font to make room for icon)
        font = pygame.font.Font(None, 12)
        text = font.render(self.block_type.value[0], True, AWS_WHITE)
        text_rect = text.get_rect(center=(rect.centerx, rect.bottom - 8))
        screen.blit(text, text_rect)
        
        # Draw hit indicator
        if self.max_hits > 1:
            hit_font = pygame.font.Font(None, 14)
            hit_text = hit_font.render(f"{self.hits_remaining}", True, AWS_WHITE)
            hit_rect = hit_text.get_rect(topright=(rect.right - 3, rect.top + 2))
            screen.blit(hit_text, hit_rect)
    
    def _draw_service_icon(self, screen: pygame.Surface, rect: pygame.Rect) -> None:
        """Draw service-specific icon based on block type."""
        center_x, center_y = rect.centerx, rect.centery - 5
        
        if self.block_type == BlockType.S3:
            # S3 bucket icon
            bucket_rect = pygame.Rect(center_x - 8, center_y - 6, 16, 10)
            pygame.draw.rect(screen, AWS_WHITE, bucket_rect, 1)
            pygame.draw.line(screen, AWS_WHITE, 
                           (bucket_rect.left + 2, bucket_rect.bottom - 3),
                           (bucket_rect.right - 2, bucket_rect.bottom - 3), 1)
            
        elif self.block_type == BlockType.LAMBDA:
            # Lambda function icon (λ symbol)
            font = pygame.font.Font(None, 20)
            lambda_text = font.render("λ", True, AWS_WHITE)
            lambda_rect = lambda_text.get_rect(center=(center_x, center_y))
            screen.blit(lambda_text, lambda_rect)
            
        elif self.block_type == BlockType.CLOUDWATCH:
            # CloudWatch monitoring icon (graph)
            points = [
                (center_x - 8, center_y + 4),
                (center_x - 4, center_y - 2),
                (center_x, center_y + 1),
                (center_x + 4, center_y - 4),
                (center_x + 8, center_y + 2)
            ]
            pygame.draw.lines(screen, AWS_WHITE, False, points, 2)
            
        elif self.block_type == BlockType.EC2:
            # EC2 server icon
            server_rect = pygame.Rect(center_x - 6, center_y - 6, 12, 12)
            pygame.draw.rect(screen, AWS_WHITE, server_rect, 1)
            # Server lines
            for i in range(3):
                y = server_rect.top + 2 + i * 3
                pygame.draw.line(screen, AWS_WHITE,
                               (server_rect.left + 2, y),
                               (server_rect.right - 2, y), 1)
                               
        elif self.block_type == BlockType.RDS:
            # RDS database icon
            # Database cylinder
            pygame.draw.ellipse(screen, AWS_WHITE, 
                              (center_x - 8, center_y - 6, 16, 6), 1)
            pygame.draw.ellipse(screen, AWS_WHITE, 
                              (center_x - 8, center_y + 2, 16, 6), 1)
            pygame.draw.line(screen, AWS_WHITE,
                           (center_x - 8, center_y - 3),
                           (center_x - 8, center_y + 5), 1)
            pygame.draw.line(screen, AWS_WHITE,
                           (center_x + 8, center_y - 3),
                           (center_x + 8, center_y + 5), 1)
                           
        elif self.block_type == BlockType.API_GATEWAY:
            # API Gateway icon
            # Gateway symbol
            pygame.draw.circle(screen, AWS_WHITE, (center_x - 6, center_y), 2, 1)
            pygame.draw.circle(screen, AWS_WHITE, (center_x + 6, center_y), 2, 1)
            pygame.draw.line(screen, AWS_WHITE,
                           (center_x - 4, center_y),
                           (center_x + 4, center_y), 2)
                           
        elif self.block_type == BlockType.EKS:
            # EKS Kubernetes icon (hexagon)
            hex_points = []
            for i in range(6):
                angle = i * math.pi / 3
                x = center_x + 6 * math.cos(angle)
                y = center_y + 6 * math.sin(angle)
                hex_points.append((x, y))
            pygame.draw.polygon(screen, AWS_WHITE, hex_points, 1)
            
        elif self.block_type == BlockType.SAGEMAKER:
            # SageMaker ML icon
            # Neural network nodes
            nodes = [
                (center_x - 6, center_y - 3),
                (center_x - 6, center_y + 3),
                (center_x, center_y),
                (center_x + 6, center_y - 3),
                (center_x + 6, center_y + 3)
            ]
            for node in nodes:
                pygame.draw.circle(screen, AWS_WHITE, node, 2, 1)
            # Connections
            pygame.draw.line(screen, AWS_WHITE, nodes[0], nodes[2], 1)
            pygame.draw.line(screen, AWS_WHITE, nodes[1], nodes[2], 1)
            pygame.draw.line(screen, AWS_WHITE, nodes[2], nodes[3], 1)
            pygame.draw.line(screen, AWS_WHITE, nodes[2], nodes[4], 1)
            
        elif self.block_type == BlockType.BEDROCK:
            # Bedrock AI icon (diamond/gem)
            diamond_points = [
                (center_x, center_y - 6),
                (center_x - 6, center_y),
                (center_x, center_y + 6),
                (center_x + 6, center_y)
            ]
            pygame.draw.polygon(screen, AWS_WHITE, diamond_points, 1)
            pygame.draw.line(screen, AWS_WHITE,
                           (center_x - 3, center_y - 3),
                           (center_x + 3, center_y + 3), 1)
            pygame.draw.line(screen, AWS_WHITE,
                           (center_x + 3, center_y - 3),
                           (center_x - 3, center_y + 3), 1)
                           
        elif self.block_type == BlockType.Q_DEVELOPER:
            # Q Developer icon (enhanced Q)
            font = pygame.font.Font(None, 18)
            q_text = font.render("Q", True, AWS_WHITE)
            q_rect = q_text.get_rect(center=(center_x, center_y))
            screen.blit(q_text, q_rect)
            
        elif self.block_type == BlockType.CLOUDFORMATION:
            # CloudFormation stack icon
            stack_rects = [
                pygame.Rect(center_x - 6, center_y + 2, 12, 3),
                pygame.Rect(center_x - 4, center_y - 1, 8, 3),
                pygame.Rect(center_x - 2, center_y - 4, 4, 3)
            ]
            for stack_rect in stack_rects:
                pygame.draw.rect(screen, AWS_WHITE, stack_rect, 1)
                
        elif self.block_type == BlockType.AUTO_SCALING:
            # Auto Scaling icon (arrows)
            # Up arrow
            up_arrow = [
                (center_x, center_y - 6),
                (center_x - 3, center_y - 2),
                (center_x + 3, center_y - 2)
            ]
            pygame.draw.polygon(screen, AWS_WHITE, up_arrow)
            # Down arrow
            down_arrow = [
                (center_x, center_y + 6),
                (center_x - 3, center_y + 2),
                (center_x + 3, center_y + 2)
            ]
            pygame.draw.polygon(screen, AWS_WHITE, down_arrow)

class PowerUp:
    """Collectible power-up that falls from destroyed blocks."""
    
    def __init__(self, x: float, y: float, powerup_type: PowerUpType):
        self.position = Vector2D(x, y)
        self.powerup_type = powerup_type
        self.velocity = Vector2D(0, POWERUP_FALL_SPEED)
        self.width = 40
        self.height = 20
        self.collected = False
        
    def update(self, dt: float) -> None:
        """Update power-up position."""
        self.position = self.position + self.velocity * dt
        
        # Remove if off screen
        if self.position.y > SCREEN_HEIGHT:
            self.collected = True  # Mark for removal
    
    def get_rect(self) -> pygame.Rect:
        """Get power-up collision rectangle."""
        return pygame.Rect(
            self.position.x - self.width / 2,
            self.position.y - self.height / 2,
            self.width,
            self.height
        )
    
    def draw(self, screen: pygame.Surface) -> None:
        """Draw the power-up."""
        if self.collected:
            return
            
        rect = self.get_rect()
        
        # Draw power-up background
        pygame.draw.rect(screen, self.powerup_type.value[2], rect)
        pygame.draw.rect(screen, AWS_WHITE, rect, 2)
        
        # Draw power-up text
        font = pygame.font.Font(None, 12)
        text = font.render(self.powerup_type.value[0][:8], True, AWS_WHITE)
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)

class Level:
    """Level data and block arrangements representing AWS architectures."""
    
    def __init__(self, level_number: int):
        self.level_number = level_number
        self.blocks: List[Block] = []
        self.completed = False
        self.generate_level()
    
    def generate_level(self) -> None:
        """Generate blocks for the current level."""
        self.blocks.clear()
        
        if self.level_number == 1:
            self._generate_basic_level()
        elif self.level_number == 2:
            self._generate_web_app_level()
        elif self.level_number == 3:
            self._generate_serverless_level()
        elif self.level_number == 4:
            self._generate_ml_workflow_level()
        else:
            self._generate_advanced_level()
    
    def _generate_basic_level(self) -> None:
        """Level 1: Basic S3 and Lambda blocks."""
        start_x = BLOCK_WIDTH
        start_y = 100
        
        # Row 1: S3 blocks
        for i in range(8):
            x = start_x + i * (BLOCK_WIDTH + 5)
            self.blocks.append(Block(x, start_y, BlockType.S3))
        
        # Row 2: Lambda blocks
        for i in range(8):
            x = start_x + i * (BLOCK_WIDTH + 5)
            self.blocks.append(Block(x, start_y + BLOCK_HEIGHT + 10, BlockType.LAMBDA))
    
    def _generate_web_app_level(self) -> None:
        """Level 2: Web application architecture."""
        start_x = BLOCK_WIDTH
        start_y = 80
        
        # Load balancer tier (API Gateway)
        for i in range(6):
            x = start_x + (i + 1) * (BLOCK_WIDTH + 5)
            self.blocks.append(Block(x, start_y, BlockType.API_GATEWAY))
        
        # Compute tier (EC2)
        for i in range(8):
            x = start_x + i * (BLOCK_WIDTH + 5)
            self.blocks.append(Block(x, start_y + (BLOCK_HEIGHT + 10), BlockType.EC2))
        
        # Database tier (RDS)
        for i in range(4):
            x = start_x + (i + 2) * (BLOCK_WIDTH + 5)
            self.blocks.append(Block(x, start_y + 2 * (BLOCK_HEIGHT + 10), BlockType.RDS))
    
    def _generate_serverless_level(self) -> None:
        """Level 3: Serverless architecture with special blocks."""
        start_x = BLOCK_WIDTH
        start_y = 70
        
        # API Gateway
        for i in range(6):
            x = start_x + (i + 1) * (BLOCK_WIDTH + 5)
            self.blocks.append(Block(x, start_y, BlockType.API_GATEWAY))
        
        # Lambda functions
        for i in range(8):
            x = start_x + i * (BLOCK_WIDTH + 5)
            self.blocks.append(Block(x, start_y + (BLOCK_HEIGHT + 10), BlockType.LAMBDA))
        
        # Storage and monitoring
        for i in range(6):
            x = start_x + (i + 1) * (BLOCK_WIDTH + 5)
            block_type = BlockType.S3 if i % 2 == 0 else BlockType.CLOUDWATCH
            self.blocks.append(Block(x, start_y + 2 * (BLOCK_HEIGHT + 10), block_type))
        
        # Special blocks
        self.blocks.append(Block(start_x + 3 * (BLOCK_WIDTH + 5), 
                                start_y + 3 * (BLOCK_HEIGHT + 10), BlockType.Q_DEVELOPER))
        self.blocks.append(Block(start_x + 5 * (BLOCK_WIDTH + 5), 
                                start_y + 3 * (BLOCK_HEIGHT + 10), BlockType.AUTO_SCALING))
    
    def _generate_ml_workflow_level(self) -> None:
        """Level 4: Machine learning workflow."""
        start_x = BLOCK_WIDTH
        start_y = 60
        
        # Data ingestion (S3)
        for i in range(8):
            x = start_x + i * (BLOCK_WIDTH + 5)
            self.blocks.append(Block(x, start_y, BlockType.S3))
        
        # ML processing (SageMaker)
        for i in range(6):
            x = start_x + (i + 1) * (BLOCK_WIDTH + 5)
            self.blocks.append(Block(x, start_y + (BLOCK_HEIGHT + 10), BlockType.SAGEMAKER))
        
        # AI services (Bedrock)
        for i in range(4):
            x = start_x + (i + 2) * (BLOCK_WIDTH + 5)
            self.blocks.append(Block(x, start_y + 2 * (BLOCK_HEIGHT + 10), BlockType.BEDROCK))
        
        # Infrastructure (EKS)
        for i in range(6):
            x = start_x + (i + 1) * (BLOCK_WIDTH + 5)
            self.blocks.append(Block(x, start_y + 3 * (BLOCK_HEIGHT + 10), BlockType.EKS))
        
        # Special blocks
        self.blocks.append(Block(start_x + 2 * (BLOCK_WIDTH + 5), 
                                start_y + 4 * (BLOCK_HEIGHT + 10), BlockType.CLOUDFORMATION))
    
    def _generate_advanced_level(self) -> None:
        """Advanced levels with mixed architectures."""
        start_x = BLOCK_WIDTH
        start_y = 50
        
        # Create a complex pattern with all block types
        block_types = list(BlockType)
        
        for row in range(6):
            blocks_in_row = 8 - (row % 3)  # Varying row lengths
            start_offset = (8 - blocks_in_row) // 2
            
            for col in range(blocks_in_row):
                x = start_x + (start_offset + col) * (BLOCK_WIDTH + 5)
                y = start_y + row * (BLOCK_HEIGHT + 10)
                
                # Select block type based on position and level
                type_index = (row * blocks_in_row + col + self.level_number) % len(block_types)
                block_type = block_types[type_index]
                
                self.blocks.append(Block(x, y, block_type))
    
    def is_complete(self) -> bool:
        """Check if all blocks are destroyed."""
        return all(block.destroyed for block in self.blocks)
    
    def get_remaining_blocks(self) -> int:
        """Get count of remaining blocks."""
        return sum(1 for block in self.blocks if not block.destroyed)

class UI:
    """User interface rendering and management."""
    
    def __init__(self):
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 32)
        self.font_small = pygame.font.Font(None, 24)
        
    def draw_hud(self, screen: pygame.Surface, score: int, lives: int, level: int, 
                 active_powerups: Dict[PowerUpType, float]) -> None:
        """Draw the heads-up display."""
        # Score
        score_text = self.font_medium.render(f"Score: {score:,}", True, AWS_WHITE)
        screen.blit(score_text, (10, 10))
        
        # Lives
        lives_text = self.font_medium.render(f"Lives: {lives}", True, AWS_WHITE)
        screen.blit(lives_text, (SCREEN_WIDTH - 150, 10))
        
        # Level
        level_text = self.font_medium.render(f"Level {level}", True, AWS_WHITE)
        level_rect = level_text.get_rect(center=(SCREEN_WIDTH // 2, 25))
        screen.blit(level_text, level_rect)
        
        # Active power-ups
        y_offset = 50
        for powerup_type, remaining_time in active_powerups.items():
            if remaining_time > 0:
                powerup_text = self.font_small.render(
                    f"{powerup_type.value[0]}: {remaining_time:.1f}s", 
                    True, powerup_type.value[2]
                )
                screen.blit(powerup_text, (10, y_offset))
                y_offset += 25
    
    def draw_menu(self, screen: pygame.Surface, title: str, options: List[str], 
                  selected_index: int) -> None:
        """Draw a menu screen."""
        screen.fill(AWS_DARK_BLUE)
        
        # Title
        title_text = self.font_large.render(title, True, AWS_ORANGE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 200))
        screen.blit(title_text, title_rect)
        
        # Options
        for i, option in enumerate(options):
            color = AWS_WHITE if i == selected_index else AWS_LIGHT_GRAY
            option_text = self.font_medium.render(option, True, color)
            option_rect = option_text.get_rect(center=(SCREEN_WIDTH // 2, 300 + i * 50))
            screen.blit(option_text, option_rect)
            
            # Highlight selected option
            if i == selected_index:
                pygame.draw.rect(screen, AWS_ORANGE, option_rect.inflate(20, 10), 2)
    
    def draw_game_over(self, screen: pygame.Surface, final_score: int, high_score: int) -> None:
        """Draw game over screen."""
        screen.fill(AWS_DARK_BLUE)
        
        # Game Over text
        game_over_text = self.font_large.render("GAME OVER", True, AWS_RED)
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, 250))
        screen.blit(game_over_text, game_over_rect)
        
        # Final score
        score_text = self.font_medium.render(f"Final Score: {final_score:,}", True, AWS_WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 320))
        screen.blit(score_text, score_rect)
        
        # High score
        if final_score >= high_score:
            high_score_text = self.font_medium.render("NEW HIGH SCORE!", True, AWS_GREEN)
        else:
            high_score_text = self.font_medium.render(f"High Score: {high_score:,}", True, AWS_LIGHT_GRAY)
        
        high_score_rect = high_score_text.get_rect(center=(SCREEN_WIDTH // 2, 370))
        screen.blit(high_score_text, high_score_rect)
        
        # Instructions
        instruction_text = self.font_small.render("Press SPACE to play again or ESC to quit", True, AWS_WHITE)
        instruction_rect = instruction_text.get_rect(center=(SCREEN_WIDTH // 2, 450))
        screen.blit(instruction_text, instruction_rect)
    
    def draw_high_scores(self, screen: pygame.Surface, high_score: int) -> None:
        """Draw high scores screen."""
        screen.fill(AWS_DARK_BLUE)
        
        # Title
        title_text = self.font_large.render("HIGH SCORES", True, AWS_ORANGE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 150))
        screen.blit(title_text, title_rect)
        
        # High score display
        if high_score > 0:
            score_text = self.font_medium.render(f"Best Score: {high_score:,}", True, AWS_WHITE)
            score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 250))
            screen.blit(score_text, score_rect)
            
            # Achievement levels
            achievements = [
                ("AWS Novice", 1000),
                ("Cloud Practitioner", 5000),
                ("Solutions Architect", 15000),
                ("DevOps Engineer", 30000),
                ("Cloud Expert", 50000)
            ]
            
            y_offset = 320
            for title, threshold in achievements:
                if high_score >= threshold:
                    color = AWS_GREEN
                    status = "✓ ACHIEVED"
                else:
                    color = AWS_LIGHT_GRAY
                    status = f"({threshold:,} points needed)"
                
                achievement_text = self.font_small.render(f"{title}: {status}", True, color)
                achievement_rect = achievement_text.get_rect(center=(SCREEN_WIDTH // 2, y_offset))
                screen.blit(achievement_text, achievement_rect)
                y_offset += 30
        else:
            no_score_text = self.font_medium.render("No high score yet!", True, AWS_LIGHT_GRAY)
            no_score_rect = no_score_text.get_rect(center=(SCREEN_WIDTH // 2, 250))
            screen.blit(no_score_text, no_score_rect)
            
            play_text = self.font_small.render("Play the game to set your first high score!", True, AWS_WHITE)
            play_rect = play_text.get_rect(center=(SCREEN_WIDTH // 2, 300))
            screen.blit(play_text, play_rect)
        
        # Instructions
        instruction_text = self.font_small.render("Press ESC or SPACE to return to main menu", True, AWS_WHITE)
        instruction_rect = instruction_text.get_rect(center=(SCREEN_WIDTH // 2, 650))
        screen.blit(instruction_text, instruction_rect)
    
    def draw_controls(self, screen: pygame.Surface) -> None:
        """Draw controls/help screen."""
        screen.fill(AWS_DARK_BLUE)
        
        # Title
        title_text = self.font_large.render("CONTROLS & HELP", True, AWS_ORANGE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 80))
        screen.blit(title_text, title_rect)
        
        # Controls section
        controls_title = self.font_medium.render("Game Controls:", True, AWS_WHITE)
        screen.blit(controls_title, (100, 150))
        
        controls = [
            ("Arrow Keys or A/D", "Move Load Balancer paddle"),
            ("P or ESC", "Pause/Resume game"),
            ("SPACE", "Select menu options"),
            ("Up/Down Arrows", "Navigate menus")
        ]
        
        y_offset = 180
        for key, action in controls:
            key_text = self.font_small.render(f"{key}:", True, AWS_ORANGE)
            action_text = self.font_small.render(action, True, AWS_WHITE)
            screen.blit(key_text, (120, y_offset))
            screen.blit(action_text, (280, y_offset))
            y_offset += 25
        
        # Gameplay section
        gameplay_title = self.font_medium.render("How to Play:", True, AWS_WHITE)
        screen.blit(gameplay_title, (100, 320))
        
        gameplay_tips = [
            "• Use your Load Balancer paddle to bounce the AWS Q Developer ball",
            "• Destroy all AWS service blocks to complete each level",
            "• Collect power-ups that fall from destroyed blocks",
            "• Each level represents a different AWS architecture pattern",
            "• Ball speed increases with each completed level"
        ]
        
        y_offset = 350
        for tip in gameplay_tips:
            tip_text = self.font_small.render(tip, True, AWS_WHITE)
            screen.blit(tip_text, (120, y_offset))
            y_offset += 25
        
        # AWS Services section
        services_title = self.font_medium.render("AWS Services Featured:", True, AWS_WHITE)
        screen.blit(services_title, (100, 480))
        
        services_info = [
            "• Tier 1 (1 hit): S3, Lambda, CloudWatch",
            "• Tier 2 (2 hits): EC2, RDS, API Gateway", 
            "• Tier 3 (3 hits): EKS, SageMaker, Bedrock",
            "• Special blocks trigger unique power-ups"
        ]
        
        y_offset = 510
        for info in services_info:
            info_text = self.font_small.render(info, True, AWS_WHITE)
            screen.blit(info_text, (120, y_offset))
            y_offset += 25
        
        # Instructions
        instruction_text = self.font_small.render("Press ESC or SPACE to return to main menu", True, AWS_WHITE)
        instruction_rect = instruction_text.get_rect(center=(SCREEN_WIDTH // 2, 650))
        screen.blit(instruction_text, instruction_rect)

class AudioManager:
    """Sound effects and music management."""
    
    def __init__(self):
        self.sounds_enabled = True
        self.volume = 0.7
        
        # Initialize mixer
        try:
            pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
            self._generate_sounds()
        except pygame.error:
            print("Warning: Audio system not available, running in silent mode")
            self.sounds_enabled = False
    
    def _generate_sounds(self) -> None:
        """Generate simple beep sounds for retro feel."""
        try:
            # Create simple tones for different events
            self.bounce_sound = self._create_tone(440, 0.1)  # A note
            self.block_hit_sound = self._create_tone(660, 0.15)  # E note
            self.powerup_sound = self._create_tone(880, 0.2)  # A note (higher)
            self.level_complete_sound = self._create_chord([440, 554, 659], 0.5)  # A major chord
        except Exception as e:
            print(f"Warning: Could not generate sounds: {e}")
            self.sounds_enabled = False
    
    def _create_tone(self, frequency: float, duration: float) -> Optional[pygame.mixer.Sound]:
        """Create a simple tone."""
        try:
            sample_rate = 22050
            frames = int(duration * sample_rate)
            arr = []
            
            for i in range(frames):
                wave = 4096 * math.sin(2 * math.pi * frequency * i / sample_rate)
                arr.append([int(wave), int(wave)])
            
            # Try to use sndarray if available, otherwise create a dummy sound
            try:
                sound = pygame.sndarray.make_sound(pygame.array.array('i', arr))
                sound.set_volume(self.volume)
                return sound
            except (ImportError, AttributeError):
                # Fallback: create a minimal sound buffer
                return self._create_simple_sound(frequency, duration)
        except Exception:
            return None
    
    def _create_simple_sound(self, frequency: float, duration: float) -> Optional[pygame.mixer.Sound]:
        """Create a simple sound without numpy/sndarray."""
        try:
            # Create a minimal sound buffer
            sample_rate = 22050
            frames = int(duration * sample_rate)
            
            # Create raw audio data
            raw_data = bytearray()
            for i in range(frames):
                # Simple sine wave
                sample = int(4096 * math.sin(2 * math.pi * frequency * i / sample_rate))
                # Convert to 16-bit signed integer, little-endian, stereo
                raw_data.extend(sample.to_bytes(2, 'little', signed=True))
                raw_data.extend(sample.to_bytes(2, 'little', signed=True))
            
            sound = pygame.mixer.Sound(buffer=raw_data)
            sound.set_volume(self.volume)
            return sound
        except Exception:
            return None
    
    def _create_chord(self, frequencies: List[float], duration: float) -> Optional[pygame.mixer.Sound]:
        """Create a chord from multiple frequencies."""
        try:
            sample_rate = 22050
            frames = int(duration * sample_rate)
            
            # Create raw audio data
            raw_data = bytearray()
            for i in range(frames):
                wave = 0
                for freq in frequencies:
                    wave += 1024 * math.sin(2 * math.pi * freq * i / sample_rate)
                
                sample = int(wave)
                # Convert to 16-bit signed integer, little-endian, stereo
                raw_data.extend(sample.to_bytes(2, 'little', signed=True))
                raw_data.extend(sample.to_bytes(2, 'little', signed=True))
            
            sound = pygame.mixer.Sound(buffer=raw_data)
            sound.set_volume(self.volume)
            return sound
        except Exception:
            return None
    
    def play_bounce(self) -> None:
        """Play ball bounce sound."""
        if self.sounds_enabled and hasattr(self, 'bounce_sound') and self.bounce_sound:
            self.bounce_sound.play()
    
    def play_block_hit(self) -> None:
        """Play block hit sound."""
        if self.sounds_enabled and hasattr(self, 'block_hit_sound') and self.block_hit_sound:
            self.block_hit_sound.play()
    
    def play_powerup(self) -> None:
        """Play power-up collection sound."""
        if self.sounds_enabled and hasattr(self, 'powerup_sound') and self.powerup_sound:
            self.powerup_sound.play()
    
    def play_level_complete(self) -> None:
        """Play level completion sound."""
        if self.sounds_enabled and hasattr(self, 'level_complete_sound') and self.level_complete_sound:
            self.level_complete_sound.play()

class Game:
    """Main game class handling game loop and state management."""
    
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("AWS CloudBurst")
        self.clock = pygame.time.Clock()
        
        # Game state
        self.state = GameState.MENU
        self.running = True
        self.score = 0
        self.lives = 3
        self.current_level = 1
        self.high_score = self._load_high_score()
        
        # Game objects
        self.paddle = Paddle(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
        self.balls: List[Ball] = []
        self.level = Level(1)
        self.powerups: List[PowerUp] = []
        
        # Power-up tracking
        self.active_powerups: Dict[PowerUpType, float] = {
            powerup_type: 0 for powerup_type in PowerUpType
        }
        self.score_multiplier = 1
        
        # UI and audio
        self.ui = UI()
        self.audio = AudioManager()
        
        # Menu state
        self.menu_options = ["Play", "High Scores", "Controls", "Quit"]
        self.selected_menu_option = 0
        
        # Initialize first ball
        self._spawn_ball()
    
    def _load_high_score(self) -> int:
        """Load high score from file."""
        try:
            with open("high_score.json", "r") as f:
                data = json.load(f)
                return data.get("high_score", 0)
        except (FileNotFoundError, json.JSONDecodeError):
            return 0
    
    def _save_high_score(self) -> None:
        """Save high score to file."""
        try:
            with open("high_score.json", "w") as f:
                json.dump({"high_score": self.high_score}, f)
        except IOError:
            pass  # Fail silently if can't save
    
    def _spawn_ball(self) -> None:
        """Spawn a new ball at the paddle position."""
        ball_speed = BALL_INITIAL_SPEED * (1 + (self.current_level - 1) * BALL_SPEED_INCREASE)
        ball_speed = min(ball_speed, BALL_MAX_SPEED)
        
        ball = Ball(self.paddle.position.x, self.paddle.position.y - 30, ball_speed)
        self.balls.append(ball)
    
    def _handle_events(self) -> None:
        """Handle pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN:
                if self.state == GameState.MENU:
                    self._handle_menu_input(event.key)
                elif self.state == GameState.PLAYING:
                    self._handle_game_input(event.key)
                elif self.state == GameState.GAME_OVER:
                    self._handle_game_over_input(event.key)
                elif self.state == GameState.PAUSED:
                    if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                        self.state = GameState.PLAYING
                elif self.state == GameState.HIGH_SCORE:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                        self.state = GameState.MENU
                elif self.state == GameState.CONTROLS:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                        self.state = GameState.MENU
    
    def _handle_menu_input(self, key: int) -> None:
        """Handle menu navigation."""
        if key == pygame.K_UP:
            self.selected_menu_option = (self.selected_menu_option - 1) % len(self.menu_options)
        elif key == pygame.K_DOWN:
            self.selected_menu_option = (self.selected_menu_option + 1) % len(self.menu_options)
        elif key == pygame.K_RETURN or key == pygame.K_SPACE:
            if self.selected_menu_option == 0:  # Play
                self._start_new_game()
            elif self.selected_menu_option == 1:  # High Scores
                self.state = GameState.HIGH_SCORE
            elif self.selected_menu_option == 2:  # Controls
                self.state = GameState.CONTROLS
            elif self.selected_menu_option == 3:  # Quit
                self.running = False
    
    def _handle_game_input(self, key: int) -> None:
        """Handle in-game input."""
        if key == pygame.K_p or key == pygame.K_ESCAPE:
            self.state = GameState.PAUSED
    
    def _handle_game_over_input(self, key: int) -> None:
        """Handle game over screen input."""
        if key == pygame.K_SPACE:
            self._start_new_game()
        elif key == pygame.K_ESCAPE:
            self.state = GameState.MENU
    
    def _start_new_game(self) -> None:
        """Initialize a new game."""
        self.state = GameState.PLAYING
        self.score = 0
        self.lives = 3
        self.current_level = 1
        self.score_multiplier = 1
        
        # Reset game objects
        self.paddle = Paddle(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
        self.balls.clear()
        self.powerups.clear()
        self.level = Level(1)
        
        # Reset power-ups
        for powerup_type in PowerUpType:
            self.active_powerups[powerup_type] = 0
        
        self._spawn_ball()
    
    def _update_game(self, dt: float) -> None:
        """Update game logic."""
        keys_pressed = pygame.key.get_pressed()
        
        # Update paddle
        self.paddle.update(dt, keys_pressed)
        
        # Update balls
        for ball in self.balls[:]:
            ball.update(dt)
            
            # Check if ball fell off screen
            if ball.position.y > SCREEN_HEIGHT:
                self.balls.remove(ball)
                if not self.balls:  # No balls left
                    self.lives -= 1
                    if self.lives <= 0:
                        self._game_over()
                    else:
                        self._spawn_ball()
        
        # Ball-paddle collision
        paddle_rect = self.paddle.get_rect()
        for ball in self.balls:
            ball_rect = pygame.Rect(ball.position.x - ball.radius, ball.position.y - ball.radius,
                                  ball.radius * 2, ball.radius * 2)
            
            if ball_rect.colliderect(paddle_rect) and ball.velocity.y > 0:
                ball.bounce_off_paddle(self.paddle.position.x, self.paddle.width)
                self.audio.play_bounce()
        
        # Ball-block collision
        for ball in self.balls:
            ball_rect = pygame.Rect(ball.position.x - ball.radius, ball.position.y - ball.radius,
                                  ball.radius * 2, ball.radius * 2)
            
            for block in self.level.blocks:
                if not block.destroyed and ball_rect.colliderect(block.get_rect()):
                    # Determine collision side and bounce accordingly
                    block_rect = block.get_rect()
                    
                    # Simple collision response
                    if abs(ball.position.x - block_rect.centerx) > abs(ball.position.y - block_rect.centery):
                        ball.velocity.x = -ball.velocity.x
                    else:
                        ball.velocity.y = -ball.velocity.y
                    
                    # Handle block hit
                    points, destroyed = block.hit()
                    if points > 0:
                        self.score += points * self.score_multiplier
                        self.audio.play_block_hit()
                        
                        # Chance to spawn power-up
                        if destroyed and block.block_type.value[1] >= 2 and random.random() < 0.15:
                            powerup_type = random.choice(list(PowerUpType))
                            powerup = PowerUp(block.position.x, block.position.y, powerup_type)
                            self.powerups.append(powerup)
                    
                    break
        
        # Update power-ups
        for powerup in self.powerups[:]:
            powerup.update(dt)
            
            if powerup.collected:
                self.powerups.remove(powerup)
                continue
            
            # Check collision with paddle
            if powerup.get_rect().colliderect(paddle_rect):
                self._activate_powerup(powerup.powerup_type)
                self.powerups.remove(powerup)
                self.audio.play_powerup()
        
        # Update active power-ups
        for powerup_type in PowerUpType:
            if self.active_powerups[powerup_type] > 0:
                self.active_powerups[powerup_type] -= dt
                
                if self.active_powerups[powerup_type] <= 0:
                    self._deactivate_powerup(powerup_type)
        
        # Check level completion
        if self.level.is_complete():
            self._complete_level()
    
    def _activate_powerup(self, powerup_type: PowerUpType) -> None:
        """Activate a power-up effect."""
        duration = powerup_type.value[1]
        self.active_powerups[powerup_type] = duration
        
        if powerup_type == PowerUpType.MULTI_BALL:
            # Spawn additional balls
            for _ in range(2):
                self._spawn_ball()
        elif powerup_type == PowerUpType.PADDLE_EXTEND:
            self.paddle.extend_paddle(duration)
        elif powerup_type == PowerUpType.SCORE_MULTIPLIER:
            self.score_multiplier = 2
    
    def _deactivate_powerup(self, powerup_type: PowerUpType) -> None:
        """Deactivate a power-up effect."""
        if powerup_type == PowerUpType.SCORE_MULTIPLIER:
            self.score_multiplier = 1
    
    def _complete_level(self) -> None:
        """Handle level completion."""
        self.audio.play_level_complete()
        self.current_level += 1
        self.level = Level(self.current_level)
        
        # Bonus points for remaining lives
        self.score += self.lives * 100
        
        # Clear power-ups and spawn new ball
        self.powerups.clear()
        self.balls.clear()
        self._spawn_ball()
    
    def _game_over(self) -> None:
        """Handle game over."""
        self.state = GameState.GAME_OVER
        
        if self.score > self.high_score:
            self.high_score = self.score
            self._save_high_score()
    
    def _draw_background(self) -> None:
        """Draw the game background with AWS cloud pattern."""
        self.screen.fill(AWS_DARK_BLUE)
        
        # Draw subtle cloud pattern
        for i in range(0, SCREEN_WIDTH, 100):
            for j in range(0, SCREEN_HEIGHT, 100):
                if (i + j) % 200 == 0:
                    pygame.draw.circle(self.screen, (40, 55, 70), (i, j), 30, 1)
    
    def _draw_game(self) -> None:
        """Draw the game screen."""
        self._draw_background()
        
        # Draw game objects
        self.paddle.draw(self.screen)
        
        for ball in self.balls:
            ball.draw(self.screen)
        
        for block in self.level.blocks:
            block.draw(self.screen)
        
        for powerup in self.powerups:
            powerup.draw(self.screen)
        
        # Draw UI
        self.ui.draw_hud(self.screen, self.score, self.lives, self.current_level, self.active_powerups)
    
    def run(self) -> None:
        """Main game loop."""
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0  # Delta time in seconds
            
            self._handle_events()
            
            if self.state == GameState.PLAYING:
                self._update_game(dt)
                self._draw_game()
            elif self.state == GameState.MENU:
                self.ui.draw_menu(self.screen, "AWS CloudBurst", self.menu_options, self.selected_menu_option)
            elif self.state == GameState.PAUSED:
                self._draw_game()
                # Draw pause overlay
                pause_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
                pause_surface.set_alpha(128)
                pause_surface.fill(AWS_DARK_BLUE)
                self.screen.blit(pause_surface, (0, 0))
                
                pause_text = self.ui.font_large.render("PAUSED", True, AWS_WHITE)
                pause_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                self.screen.blit(pause_text, pause_rect)
            elif self.state == GameState.GAME_OVER:
                self.ui.draw_game_over(self.screen, self.score, self.high_score)
            elif self.state == GameState.HIGH_SCORE:
                self.ui.draw_high_scores(self.screen, self.high_score)
            elif self.state == GameState.CONTROLS:
                self.ui.draw_controls(self.screen)
            
            pygame.display.flip()
        
        pygame.quit()

def main():
    """Main function to start the game."""
    try:
        game = Game()
        game.run()
    except Exception as e:
        print(f"Error running AWS CloudBurst: {e}")
        pygame.quit()

if __name__ == "__main__":
    main()
