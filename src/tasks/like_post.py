from src.utils import find_and_click_image

def like_post(image_path='assets/coracao.png'):
    """
    Curte um post, procurando pela imagem do coração.
    """
    print("--- Curtindo post ---")
    find_and_click_image(image_path)
