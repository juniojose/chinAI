import time
from src.utils import click_at

def run_recorded_action(coord_map, run_action_name):
    """
    Executa uma sequência de ações pré-gravadas.
    """
    print(f"--- Executando ação gravada: {run_action_name} ---")
    
    click_at(coord_map, "chinaActionRecord")
    time.sleep(2)
    
    click_at(coord_map, run_action_name)
    time.sleep(2)

    # Este passo parece ser comum a todas as ações gravadas
    click_at(coord_map, "chinaActionRecordStartRecordButton")
    time.sleep(1)

    click_at(coord_map, "chinaCloseActionRecord")
    time.sleep(5)
