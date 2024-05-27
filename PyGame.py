import pygame
import random

Black = (0, 0, 0)
White = (255, 225, 255)

Width, Height = 800, 600
Ball_Radius = 10
Paddle_Width = 100
Paddle_Height = 20

class Ball:
    def init(self):
        self.x =Width//2
        self.y =Height//2
        self.speed_x = random.choice([-3, 3])
        self.speed_y = 2

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def check_collision(self):
        if self.x <= Ball_Radius or self.x >= Width - Ball_Radius:
            self.speed_x = - self.speed_x 
        if self.y <= Ball_Radius:
            self.speed_y = -self.speed_y

class Paddle:
    def init(self):
        self.width = Paddle_Width
        self.height = Paddle_Height
        self.x = (Width - self.width)//2
        self.y = Height - self.height - 10

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= 10
        elif direction == "right" and self.x < Width - self.width:
            self.x += 10

class Game:
   def init(self):
    self.ball = Ball()
    self.paddle = Paddle()
    self.score = 0
    self.font = pygame.font.Font(None, 36)
    self.game_over = False

   def handle_events(self):
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            self.game_over = True

   def update(self):
     self.ball.move()
     self.ball.check_collision()

     if self.ball.y >= Height - Ball_Radius - Paddle_Height:
        if self.paddle.x <= self.ball.x <= self.paddle.x + Paddle_Width:
         self.ball.y = Height - Ball_Radius - Paddle_Height - 1
         self.ball.speed_y = -self.ball.speed_y
         self.score += 1
     else:
        self.game_over = True

   def draw(self, screen):
     screen.fill(Black)
     pygame.draw.circle(screen, White, (self.ball.x, self.ball.y), Ball_Radius)
     pygame.draw.rect(screen, White, (self.paddle.x, self.paddle.y, self.paddle.width, self.paddle.height))
     score_text = self.font.render(f"Score: {self.score}", True, White)
     screen.blit(score_text, (10, 10))
    
     if self.game_over:
       game_over_text = self.font.render(f"Your score: {self.score}", True, White)
       game_over_rect = game_over_text.get_rect()
       game_over_rect.center = (Width // 2, Height // 2)
       screen.blit(game_over_text, game_over_rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption("Ping Pong")
    clock = pygame.time.Clock()
    game = Game()
 
    while not game.game_over:
       game.handle_events()

       keys = pygame.key.get_pressed()
       if keys[pygame.K_LEFT]:
         game.paddle.move("left")
       if keys[pygame.K_RIGHT]:
         game.paddle.move("right")
         
       game.update()
       game.draw(screen)
         
       pygame.display.flip()
       clock.tick(60)
    
    pygame.quit()   
main()