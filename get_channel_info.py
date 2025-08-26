import requests
import os

API_KEY = os.getenv("YOUTUBE_API_KEY")
CHANNEL_ID = "UCCBZLVFvsfDps_1NmG7so_w"  # Ejemplo: canal de Google Developers

def get_channel_data():
    url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={CHANNEL_ID}&key={API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error en la solicitud:", response.text)
        return

    data = response.json()
    if "items" not in data:
        print("No se encontraron datos del canal.")
        return

    channel = data["items"][0]
    snippet = channel["snippet"]
    stats = channel["statistics"]

    print(f"Nombre del canal: {snippet['title']}")
    print(f"Descripción: {snippet['description']}")
    print(f"Suscriptores: {stats.get('subscriberCount', 'Oculto')}")
    print(f"Videos: {stats['videoCount']}")
    print(f"Vistas totales: {stats['viewCount']}")

if __name__ == "__main__":
    get_channel_data()
