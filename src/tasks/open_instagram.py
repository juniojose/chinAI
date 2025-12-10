import time
from src.utils import click_at

def open_instagram(coord_map):
    """
    Abre o Instagram e navega para a tela inicial.
    """
    print("--- Abrindo Instagram ---")
    click_at(coord_map, "instagramOpen")
    time.sleep(2)
    print("--- Indo para a Home do Instagram ---")
    click_at(coord_map, "instagramHome")
    time.sleep(3)
