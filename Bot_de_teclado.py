import time
import threading
from pynput import keyboard
import pydirectinput

# --- CONFIGURACIÓN DE PRECISIÓN ---
TECLA_OBJETIVO = '3'  
SEGUNDOS_EXACTOS = 0.3  # Cambia esto al tiempo exacto que necesite el juego
# ----------------------------------

esta_presionando_auto = False

def presionar_tecla_automatica():
    global esta_presionando_auto
    
    # Espera el tiempo exacto configurado
    time.sleep(SEGUNDOS_EXACTOS)
    
    esta_presionando_auto = True
    
    # Simula la pulsación física de forma inmediata
    pydirectinput.press(TECLA_OBJETIVO)
    
    print(f"-> [!] Tecla '{TECLA_OBJETIVO}' enviada con éxito.")
    
    esta_presionando_auto = False

def al_presionar(key):
    global esta_presionando_auto
    
    try:
        # Detecta cuando tú presionas el "1" manualmente
        if hasattr(key, 'char') and key.char == TECLA_OBJETIVO:
            if not esta_presionando_auto:
                print(f"[*] Inicio de ciclo: Siguiente pulsación en exactamente {SEGUNDOS_EXACTOS}s")
                
                # Usamos un hilo para que la espera no bloquee el teclado
                hilo = threading.Thread(target=presionar_tecla_automatica)
                hilo.start()
                
    except Exception:
        pass

print("=== BOT DE PRECISIÓN PARA ROBLOX ===")
print(f"Tecla: {TECLA_OBJETIVO} | Tiempo: {SEGUNDOS_EXACTOS}s")

with keyboard.Listener(on_press=al_presionar) as listener:
    listener.join()
