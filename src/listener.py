
import threading
import time
import queue

import pyautogui
import win32api
import keyboard

def start_mouse_listener(coord_queue: queue.Queue, stop_event: threading.Event):
    """
    Inicia um loop em uma thread separada para verificar o clique do mouse.
    Usa uma abordagem de polling em vez de um hook.
    """
    def poll_mouse():
        # Pega o estado inicial do botão esquerdo do mouse
        old_state = win32api.GetKeyState(0x01)
        
        while not stop_event.is_set():
            new_state = win32api.GetKeyState(0x01)
            if new_state != old_state:  # O estado mudou
                old_state = new_state
                if new_state < 0:  # O botão está pressionado
                    x, y = pyautogui.position()
                    coord_queue.put((x, y))
            # Pequena pausa para não consumir 100% da CPU
            time.sleep(0.01)

    thread = threading.Thread(target=poll_mouse)
    thread.daemon = True # Permite que o programa principal saia sem esperar por esta thread
    thread.start()
    return thread

def start_keyboard_listener(stop_callback):
    """
    Inicia o listener do teclado para a tecla ESC.
    """
    # keyboard.add_hotkey não é bloqueante e roda em seu próprio thread
    keyboard.add_hotkey('esc', stop_callback)
