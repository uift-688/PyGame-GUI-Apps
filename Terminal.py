import pygame
import pygame_gui
from code import InteractiveConsole
import io
from threading import local
from contextlib import redirect_stdout, redirect_stderr
import html

pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
w, h = pygame.display.get_window_size()
clock = pygame.time.Clock()

# pygame_guiのマネージャー
manager = pygame_gui.UIManager((800, 600))

pygame.display.set_caption('Terminal')

# テキストエリア（背景色、フォントサイズ、パディングを追加）
text_area = pygame_gui.elements.UITextBox(
    relative_rect=pygame.Rect(50, 150, 700, 350),
    html_text="",
    manager=manager,
    object_id="#text_area"
)

# 入力欄（背景色、フォントサイズ、ボーダー色を追加）
input_box = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect(50, 35, 700, 35),
    manager=manager,
    object_id="#input_box"
)

# 送信ボタンを作成
send_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(650, 80, 100, 40),
    text="Enter",
    manager=manager
)


string = io.StringIO()

name_space = local()

console = InteractiveConsole(name_space.__dict__)

def evaler(code):
    stringer = io.StringIO()
    with redirect_stdout(stringer): 
        with redirect_stderr(stringer):
            console.push(code)
    return html.escape(stringer.getvalue())

# メインループ
running = True
entered_text = ""
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        manager.process_events(event)

        # 送信ボタンが押されたとき
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == send_button:  # 送信ボタンが押された場合
                entered_text = input_box.text  # 入力されたテキストを取得
                string.write(f" >> {entered_text}\n")  # 入力されたテキストを保存
                string.write(f"{evaler(entered_text)}")
                text_area.set_text(string.getvalue())  # テキストエリアに表示
                input_box.set_text('')  # 入力欄をクリア
        elif event.type == pygame.VIDEORESIZE:
            if screen.size != (event.w, event.h):
                screen = pygame.transform.smoothscale(screen, (event.w, event.h))
                manager.set_window_resolution((event.w, event.h))
            w, h = event.w, event.h
            rw, rh = w / 800, h / 600
            text_area_w, text_area_h = 700 * rw, 350 * rh
            input_box_w, input_box_h = 700 * rw, 35 * rh
            send_button_w, send_button_h = 100 * rw, 40 * rh
            text_area_x, text_area_y = 50 * rw, 150 * rh
            input_box_x, input_box_y = 50 * rw, 35 * rh
            send_button_x, send_button_y = 650 * rw, 80 * rh
            text_area.set_position((text_area_x, text_area_y))
            text_area.set_dimensions((text_area_w, text_area_h))
            input_box.set_position((input_box_x, input_box_y))
            input_box.set_dimensions((input_box_w, input_box_h))
            send_button.set_position((send_button_x, send_button_y))
            send_button.set_dimensions((send_button_w, send_button_h))
    # GUIの更新
    manager.update(clock.tick(60) / 1000.0)
    # 画面の描画
    screen.fill((25, 25, 25))
    manager.draw_ui(screen)
    
    pygame.display.flip()
