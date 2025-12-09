import queue
import threading
import json
import datetime

from src import listener

# Evento global para sinalizar a parada para todas as threads
stop_event = threading.Event()
JSON_FILE = 'coordenadas.json'

def save_coordinate_to_json(data):
    """
    Salva uma nova coordenada no arquivo JSON.
    """
    try:
        try:
            with open(JSON_FILE, 'r', encoding='utf-8') as f:
                all_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            all_data = []

        all_data.append(data)

        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(all_data, f, indent=4, ensure_ascii=False)
        
        print(f"Coordenada ''{data['nome_coordenada']}'' salva em {JSON_FILE}.")

    except Exception as e:
        print(f"Erro ao salvar no arquivo JSON: {e}")

def main():
    """
    Função principal da aplicação.
    """
    coord_queue = queue.Queue()

    def stop_program():
        if not stop_event.is_set():
            print("\nTecla ESC pressionada. Encerrando a aplicação...")
            stop_event.set()

    print("Iniciando listeners...")
    mouse_thread = listener.start_mouse_listener(coord_queue, stop_event)
    listener.start_keyboard_listener(stop_program)

    print("\nAplicação iniciada. Clique na tela para capturar as coordenadas.")
    print("Pressione ESC para sair.")

    try:
        while not stop_event.is_set():
            try:
                x, y = coord_queue.get(timeout=0.1)
                print(f"\nCoordenada capturada: X={x}, Y={y}")
                
                nome = input("Digite o nome para esta coordenada: ")
                if not nome:
                    print("Nome não pode ser vazio. Coordenada descartada.")
                    continue

                descricao = input("Digite uma descrição (opcional): ")

                coordinate_data = {
                    'nome_coordenada': nome,
                    'x': x,
                    'y': y,
                    'descricao': descricao,
                    'timestamp_registro': datetime.datetime.utcnow().isoformat()
                }

                save_coordinate_to_json(coordinate_data)

            except queue.Empty:
                continue
    finally:
        print("\nEncerrando...")
        # O listener de teclado e a thread do mouse são daemons ou gerenciados
        # em segundo plano, então o programa pode encerrar.
        if mouse_thread.is_alive():
             # Apenas para garantir que a thread do mouse termine se ainda estiver viva
             mouse_thread.join(timeout=0.1)
        print("Aplicação encerrada.")

if __name__ == "__main__":
    main()