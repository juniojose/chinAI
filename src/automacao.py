import json
import time
import pyautogui
import random

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

def click_at(coord_name, coord_map, button='left', duration=0.5):
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

def curtir_na_timeline_test():
    try:
        with open("coordenadas.json", "r") as f:
            coordenadas = json.load(f)
    except FileNotFoundError:
        print("Erro: coordenadas.json nao encontrado.")
        return

    coord_map = {item["nome_coordenada"]: item for item in coordenadas}

    # Initial setup: clearWindows (outside the phone loop)
    print("--- Iniciando configuracao inicial: clearWindows ---")
    time.sleep(2)
    click_at("clearWindows", coord_map)
    time.sleep(2)

    for i in range(1, 19): # Loop from activePhone01 to activePhone18
        phone_coord_name = f"activePhone{i:02d}" # Formats as activePhone01, activePhone02, etc.
        print(f"--- Executando fluxo para {phone_coord_name} ---")

        # Initial setup: chinaActivate and activePhoneXX (inside the phone loop)
        click_at("chinaActivate", coord_map)
        time.sleep(10)
        click_at(phone_coord_name, coord_map)

        # 2. Open Instagram
        print("--- Abrindo Instagram ---")
        time.sleep(2)
        click_at("instagramOpen", coord_map)

        # 3. Go to Instagram Home
        print("--- Indo para a Home do Instagram ---")
        time.sleep(2)
        click_at("instagramHome", coord_map)
        time.sleep(3)  # Espera a tela inicial carregar

        # 4. Click chinaActionRecord
        print("--- Clicando em chinaActionRecord ---")
        time.sleep(2)
        x_record, y_record = get_coord("chinaActionRecord", coord_map)
        if x_record is not None:
            pyautogui.moveTo(x_record, y_record, duration=0.5)
            time.sleep(0.5)
            pyautogui.click()

        # 5. Click chinaActionRun01
        print("--- Clicando em chinaActionRun01 ---")
        time.sleep(2)
        x_run01, y_run01 = get_coord("chinaActionRun01", coord_map)
        if x_run01 is not None:
            pyautogui.moveTo(x_run01, y_run01, duration=0.5)
            time.sleep(0.5)
            pyautogui.click()

        # New step: Move to chinaActionRecordStartRecordButton before chinaCloseActionRecord
        time.sleep(2)
        x_start_record, y_start_record = get_coord("chinaActionRecordStartRecordButton", coord_map)
        if x_start_record is not None:
            pyautogui.moveTo(x_start_record, y_start_record, duration=0.5)
            time.sleep(1)

        # 6. Click chinaCloseActionRecord
        print("--- Clicando em chinaCloseActionRecord ---")
        time.sleep(5)
        x_close, y_close = get_coord("chinaCloseActionRecord", coord_map)
        if x_close is not None:
            pyautogui.moveTo(x_close, y_close, duration=0.5)
            time.sleep(0.5)
            pyautogui.click()
        
        # New step: Move to activePhoneXX after chinaCloseActionRecord
        time.sleep(2)
        x_active_phone_current, y_active_phone_current = get_coord(phone_coord_name, coord_map)
        if x_active_phone_current is not None:
            pyautogui.moveTo(x_active_phone_current, y_active_phone_current, duration=0.5)
            time.sleep(1)
            pyautogui.click()

        # 7. Locate and click src/curtir.png
        find_and_click_image('assets/coracao.png')

        # 8. Define random number for loop
        num_loops = random.randint(10, 15)
        print(f"--- Rodando loop {num_loops} vezes ---")

        # 9. Loop
        for j in range(num_loops):
            print(f"--- Loop {j+1}/{num_loops} ---")
            # 9.1 Click chinaActionRecord
            time.sleep(2)
            if x_record is not None:
                pyautogui.moveTo(x_record, y_record, duration=0.5)
                time.sleep(0.5)
                pyautogui.click()

            # 9.2 Click chinaActionRun02
            time.sleep(2)
            x_run02, y_run02 = get_coord("chinaActionRun02", coord_map)
            if x_run02 is not None:
                pyautogui.moveTo(x_run02, y_run02, duration=0.5)
                time.sleep(0.5)
                pyautogui.click()

            # New step: Move to chinaActionRecordStartRecordButton before chinaCloseActionRecord inside loop
            time.sleep(2)
            x_start_record, y_start_record = get_coord("chinaActionRecordStartRecordButton", coord_map)
            if x_start_record is not None:
                pyautogui.moveTo(x_start_record, y_start_record, duration=0.5)
                time.sleep(1)

            # 9.3 Click chinaCloseActionRecord
            time.sleep(2)
            if x_close is not None:
                pyautogui.moveTo(x_close, y_close, duration=0.5)
                time.sleep(0.5)
                pyautogui.click()
            
            # New step: Move to activePhoneXX after chinaCloseActionRecord inside loop
            time.sleep(2)
            x_active_phone_current, y_active_phone_current = get_coord(phone_coord_name, coord_map)
            if x_active_phone_current is not None:
                pyautogui.moveTo(x_active_phone_current, y_active_phone_current, duration=0.5)
                time.sleep(1)
                pyautogui.click()

            # 9.4 Locate and click src/curtir.png (optional)
            find_and_click_image('assets/coracao.png')

if __name__ == "__main__":
    curtir_na_timeline_test()
