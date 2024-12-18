import pygame
import pygame_gui
from html import escape
import sympy as sp

pygame.init()

# ウィンドウサイズと画面設定
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption('Calculator')

# pygame_guiのマネージャー
manager = pygame_gui.UIManager((800, 600))

# フォント設定
font = pygame.font.SysFont("Arial", 24)

# 入力エリア
expr_input = pygame_gui.elements.UITextEntryLine(
    pygame.Rect(150, 100, 500, 50), manager, placeholder_text='Enter Expression')
expr_input.set_text('')

# 出力エリア
output_display = pygame_gui.elements.UITextBox(
    '', pygame.Rect(150, 400, 500, 50), manager)

# ボタンの設定
run_button = pygame_gui.elements.UIButton(
    pygame.Rect(350, 200, 100, 50), 'Calculate', manager)

# メインループ
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == run_button:
                try:
                    # 数式の計算（高精度）
                    result = sp.sympify(expr_input.text).evalf()

                    # 結果の表示
                    output_text = f"{result}"
                    output_display.set_text(output_text)
                except Exception as e:
                    output_display.set_text('Error: Invalid Expression')
                    print(f"[Debug] {e}")

        manager.process_events(event)

    # GUIの更新
    manager.update(clock.tick(60) / 1000.0)
    
    # 画面の描画
    screen.fill((25, 25, 25))  # 背景色
    manager.draw_ui(screen)

    pygame.display.flip()
