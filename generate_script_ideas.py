import os
from openai import OpenAI

api_key = os.getenv("OPEN_API_KEY")
client = OpenAI(api_key=api_key)

prompt = (
    "Genera 3 ideas creativas de guiones para videos educativos para niños de 5 a 8 años. "
    "Haz que sean divertidas, educativas y fáciles de entender. Incluye título y resumen para cada una."
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Eres un guionista experto en contenido infantil."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.8,
    max_tokens=800,
)

ideas = response.choices[0].message.content

print("📽️ Ideas de guiones para videos infantiles:\n")
print(ideas)

# Guardar en archivo
with open("ideas_guiones.txt", "w", encoding="utf-8") as f:
    f.write(ideas)
