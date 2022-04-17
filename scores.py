import pygame

class Scores():
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = '#13F21B'
        self.font = pygame.font.SysFont('CLOUD SANS', 36)
        self.image_score()


    def image_score(self):
        self.score_img = self.font.render(str(self.stats.score), True,
                                          self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20


    def show_score(self):
        """Вывод счета на экран"""
        self.screen.blit(self.score_img, self.score_rect)