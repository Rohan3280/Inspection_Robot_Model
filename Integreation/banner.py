from rich.console import Console
import time
import os
import pygame

console = Console()

ascii_art = [
    " ████████╗██████╗ ██╗██╗   ██╗██╗███████╗██╗ ██████╗ ███╗   ██╗ ",
    " ╚══██╔══╝██╔══██╗██║╚██╗ ██╔╝██║██╔════╝██║██╔═══██╗████╗  ██║ ",
    "    ██║   ██████╔╝██║ ╚████╔╝ ██║█████╗  ██║██║   ██║██╔██╗ ██║ ",
    "    ██║   ██╔═══╝ ██║  ╚██╔╝  ██║██╔══╝  ██║██║   ██║██║╚██╗██║ ",
    "    ██║   ██║     ██║   ██║   ██║██║     ██║╚██████╔╝██║ ╚████║ ",
    "    ╚═╝   ╚═╝     ╚═╝   ╚═╝   ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ",
]

def play_sound(path="C:/Users/rishi/OneDrive/Desktop/Trivision/Integreation/launch.wav"):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
    except Exception as e:
        console.print(f"[red]Sound error:[/red] {e}")

def sliding_banner():
    for i in range(1, len(ascii_art[0]) + 1):
        os.system('cls' if os.name == 'nt' else 'clear')
        current = "\n".join(line[:i] for line in ascii_art)
        print("🤖 Launching TRIVISION...\n" + current + "\npowered by Jetson Nano")
        time.sleep(0.03)
    time.sleep(0.4)

def show_trivision_banner(animated=True, sound=True):
    if sound:
        play_sound()
    if animated:
        sliding_banner()
    else:
        console.print("[bold green]TRIVISION ready![/bold green]")
