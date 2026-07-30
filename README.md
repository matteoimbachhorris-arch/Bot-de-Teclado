# Bot Teclado

Script en Python para automatizar pulsaciones de teclado con temporizador de precisión, 100% ejecutable en local. Diseñado para juegos y aplicaciones que requieren respuestas temporizadas exactas sin intervención manual constante.

## Uso

1. Instalá las dependencias necesarias en la consola:


Bash
```
pip install pynput pydirectinput
```
2. Ejecutá el script de Python:

Bash
```
python Bot_de_teclado.py
```
3. Presioná la tecla configurada (por defecto la tecla 3) para iniciar el ciclo.
4. El bot esperará el tiempo especificado (0.3 segundos) y enviará la pulsación física de forma automática.

## Cómo funciona

Utiliza hilos de ejecución (threading) junto con pynput para escuchar las entradas del teclado en segundo plano sin congelar la aplicación, y pydirectinput para simular entradas de bajo nivel compatibles con juegos:

Python
```
# Escucha la tecla objetivo y activa el temporizador en un hilo separado
if hasattr(key, 'char') and key.char == TECLA_OBJETIVO:
    hilo = threading.Thread(target=presionar_tecla_automatica)
    hilo.start()
```

## Requisitos

-Python 3.x instalado en el sistema.
-Permisos de administrador si el juego o aplicación objetivo bloquea eventos de simulación de teclado.

## Demo

Si está habilitado GitHub Pages en este repo:

```
https://matteoimbachhorris-arch.github.io/Bot-de-Teclado/
```

## Nota de seguridad

-Tené en cuenta los términos de servicio (ToS) de los juegos en los que utilices scripts de automatización o macros, ya que algunos sistemas anti-cheat pueden detectarlos.
-Modificá la variable SEGUNDOS_EXACTOS y TECLA_OBJETIVO en el código según las necesidades específicas de tu aplicación.

## Licencia
Uso libre, sin garantías.
