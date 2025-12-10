import time
from src.utils import click_at

def activate_phone(coord_map, phone_coord_name):
    """
    Ativa um 'telefone' especifico na interface.
    """
    print(f"--- Ativando {phone_coord_name} ---")
    click_at(coord_map, "chinaActivate")
    time.sleep(10)
    click_at(coord_map, phone_coord_name)
