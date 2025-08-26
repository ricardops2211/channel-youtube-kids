import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = (
    "Genera 3 ideas creativas de guiones para videos educativos para niños de 5 a 8 años. "
    "Haz que sean divertidas, educativas y fáciles de entender. Incluye título y resumen para cada una."
)

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Eres un guionista experto en contenido infantil."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.8,
    max_tokens=800,
)

ideas = response['choices'][0]['message']['content']

print("📽️ Ideas de guiones para videos infantiles:\n")
print(ideas)

# Opcional: Guardar en archivo
with open("ideas_guiones.txt", "w", encoding="utf-8") as f:
    f.write(ideas)
