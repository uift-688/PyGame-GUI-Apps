import pygame
import pygame_gui

# Pygameの初期化
pygame.init()

# 実際のスクリーンのサイズ
w = 800
h = 600
screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)
pygame.display.set_caption("メモ帳")

manager = pygame_gui.UIManager(screen.get_size())

box = pygame_gui.elements.UITextEntryBox(pygame.Rect(20, 20, screen.get_size()[0] - 40, screen.get_size()[1] - 40), manager=manager)

clock = pygame.time.Clock()

# メインループ
running = True
entered_text = ""
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        manager.process_events(event)
        if event.type == pygame.VIDEORESIZE:
            if (w, h) != (event.w, event.h):
                w, h = pygame.display.get_window_size()
                manager.set_window_resolution((event.w, event.h))
                box.set_dimensions((event.w - 40, event.h - 40))
    # GUIの更新
    manager.update(clock.tick(60) / 1000.0)
    # 画面の描画
    screen.fill((25, 25, 25))
    manager.draw_ui(screen)
    
    pygame.display.flip()
