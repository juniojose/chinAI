import time
from src.utils import click_at

def clear_windows(coord_map):
    """
    Executa a ação de limpar janelas.
    """
    print("--- Limpando janelas ---")
    click_at(coord_map, "clearWindows")
    time.sleep(2)
