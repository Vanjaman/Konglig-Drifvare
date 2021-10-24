from threading import Thread
from flask import Flask

app = Flask('')

"""Denna modul håller botten vid liv i Replit"""

@app.route('/')
def main():
    """Skriver ut "Your bot is alive" på hemsidan"""
    return "Your bot is alive!"


def run():
    """Kör webbservern på port 8080"""
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    """Startar server"""
    server = Thread(target=run)
    server.start()
