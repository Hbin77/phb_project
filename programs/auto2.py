import pyautogui
from pynput import keyboard
import time

# 화면 크기 구하기
w, h = pyautogui.size()
center_x, center_y = w // 2, h // 2

# 종료 플래그 설정
running = True
clicking = False

def on_press(key):
    global running, clicking
    try:
        if key.char == 'q':
            clicking = True
        elif key.char == 'w':
            clicking = False
        elif key.char == 'e':
            running = False
            return False  # Stop listener
    except AttributeError:
        pass

# 키보드 리스너 시작
listener = keyboard.Listener(on_press=on_press)
listener.start()


# 클릭 작업을 수행하며 키 입력을 감지
while running:
    if clicking:
        pyautogui.click()
    time.sleep(0.01)  # 너무 빠른 클릭 방지

# 키보드 리스너 종료
listener.stop()
    