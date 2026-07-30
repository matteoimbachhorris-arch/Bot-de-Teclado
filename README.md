# Keyboard Bot

A Python script to automate keypresses with a precision timer, 100% locally executable. Designed for games and applications that require exact timed responses without constant manual intervention.

## Usage

1. Install the required dependencies in the console:

Bash
```
pip install pynput pydirectinput
```
2. Run the Python script:

Bash

```
python Keyboard_bot.py

```
3. Press the configured key (key 3 by default) to start the cycle.
4. The bot will wait for the specified time (0.3 seconds) and automatically send the physical keypress.

## How it works

It uses multithreading (`threading`) along with `pynput` to listen for keyboard inputs in the background without freezing the application, and `pydirectinput` to simulate low-level inputs compatible with games:

Python
```
#Listens for the target key and activates the timer in a separate thread
if hasattr(key, 'char') and key.char == TECLA_OBJETIVO:
hilo = threading.Thread(target=presionar_tecla_automatica)
hilo.start()
```

## Requirements

-Python 3.x installed on the system.
-Administrator privileges if the target game or application blocks keyboard simulation events.

## Demo

If GitHub Pages is enabled in this repo:
```
https://matteoimbachhorris-arch.github.io/Keyboard-Bot/
```
## Security note

-Keep in mind the Terms of Service (ToS) of games where you use automation scripts or macros, as some anti-cheat systems may detect them.
-Modify the `SEGUNDOS_EXACTOS` and `TECLA_OBJETIVO` variables in the code according to the specific needs of your application.

## License

Free to use, provided as-is without warranties.
