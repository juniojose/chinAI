import json
import time
import pyautogui
import random

import json
import random
import time
from src.tasks import (
    activate_phone,
    clear_windows,
    like_post,
    open_instagram,
    run_recorded_action,
)
from src.utils import click_at

def run_curtir_na_timeline_workflow():
    """
    Orquestra o fluxo de trabalho para curtir posts na timeline do Instagram.
    """
    try:
        with open("coordenadas.json", "r") as f:
            coordenadas = json.load(f)
    except FileNotFoundError:
        print("Erro: coordenadas.json nao encontrado.")
        print("Por favor, execute o script de configuração de coordenadas primeiro.")
        return

    coord_map = {item["nome_coordenada"]: item for item in coordenadas}

    # Contagem de telefones ativos
    phone_count = sum(1 for key in coord_map if key.startswith("activePhone"))
    if phone_count == 0:
        print("Nenhuma coordenada 'activePhone' encontrada em coordenadas.json.")
        return
    
    print(f"Encontrados {phone_count} telefones ativos.")

    # 1. Ação inicial de limpeza
    clear_windows(coord_map)

    # 2. Loop principal para cada telefone
    for i in range(1, phone_count + 1):
        phone_coord_name = f"activePhone{i:02d}"
        print(f"\n--- INICIANDO FLUXO PARA {phone_coord_name.upper()} ---")

        # 2.1 Ativa o telefone
        activate_phone(coord_map, phone_coord_name)

        # 2.2 Abre o Instagram
        open_instagram(coord_map)

        # 2.3 Executa a primeira ação gravada
        run_recorded_action(coord_map, "chinaActionRun01")
        
        # 2.4 Clica no telefone ativo novamente (passo pós-ação)
        click_at(coord_map, phone_coord_name)
        time.sleep(1)

        # 2.5 Curte o post
        like_post()

        # 2.6 Loop secundário de ações
        num_loops = random.randint(10, 15)
        print(f"--- Executando loop secundário {num_loops} vezes ---")
        for j in range(num_loops):
            print(f"--- Loop {j + 1}/{num_loops} ---")
            
            # Executa a segunda ação gravada
            run_recorded_action(coord_map, "chinaActionRun02")

            # Clica no telefone ativo novamente
            click_at(coord_map, phone_coord_name)
            time.sleep(1)

            # Tenta curtir o post novamente
            like_post()
        
        print(f"--- FLUXO PARA {phone_coord_name.upper()} FINALIZADO ---")

if __name__ == "__main__":
    run_curtir_na_timeline_workflow()

