import time
import pyautogui

def get_coord(coord_name, coord_map):
    """Obtem as coordenadas do mapa."""
    if coord_name in coord_map:
        coord = coord_map[coord_name]
        x = coord.get("x", coord.get("x_normalizado"))
        y = coord.get("y", coord.get("y_normalizado"))
        if x is not None and y is not None:
            return x, y
    print(f"Aviso: {coord_name} nao encontrado ou com coordenadas ausentes em coordenadas.json")
    return None, None

def click_at(coord_map, coord_name, button='left', duration=0.5):
    """Move para uma coordenada, espera e clica."""
    x, y = get_coord(coord_name, coord_map)
    if x is not None:
        pyautogui.moveTo(x, y, duration=duration)
        time.sleep(1)  # Espera o elemento da UI aparecer
        pyautogui.click(button=button)
        time.sleep(1)  # Mantem uma pequena pausa apos o clique

def find_and_click_image(image_path, attempts=5, delay=1, confidence=0.7):
    """
    Tenta localizar e clicar em uma imagem na tela varias vezes.
    Retorna True se a imagem for encontrada e clicada, False caso contrario.
    """
    print(f"--- Tentando localizar e clicar em {image_path} ---")
    for i in range(attempts):
        try:
            location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
            if location:
                print(f"Imagem {image_path} encontrada em: {location} (tentativa {i+1}/{attempts})")
                pyautogui.moveTo(location, duration=0.5)
                pyautogui.click()
                return True
            else:
                print(f"Imagem {image_path} nao encontrada na tela (tentativa {i+1}/{attempts})...")
        except pyautogui.PyAutoGUIException as e:
            print(f"Erro ao procurar {image_path} (tentativa {i+1}/{attempts}): {e}")
        time.sleep(delay)
    print(f"Erro: Nao foi possivel localizar e clicar em {image_path} apos {attempts} tentativas.")
    return False
