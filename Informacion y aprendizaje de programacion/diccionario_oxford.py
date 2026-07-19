import json
import os

RUTA_DICCIONARIO = "diccionario.json"

CATEGORIAS_VALIDAS = ["noun", "verb", "adjective", "adverb", "phrase", "other"]

DICCIONARIO_INICIAL = [
    {"english": "apple", "spanish": "manzana", "category": "noun"},
    {"english": "house", "spanish": "casa", "category": "noun"},
    {"english": "car", "spanish": "coche", "category": "noun"},
    {"english": "dog", "spanish": "perro", "category": "noun"},
    {"english": "cat", "spanish": "gato", "category": "noun"},
    {"english": "computer", "spanish": "ordenador", "category": "noun"},
    {"english": "run", "spanish": "correr", "category": "verb"},
    {"english": "eat", "spanish": "comer", "category": "verb"},
    {"english": "drink", "spanish": "beber", "category": "verb"},
    {"english": "sleep", "spanish": "dormir", "category": "verb"},
    {"english": "beautiful", "spanish": "bonito", "category": "adjective"},
    {"english": "big", "spanish": "grande", "category": "adjective"},
    {"english": "small", "spanish": "pequeño", "category": "adjective"},
    {"english": "fast", "spanish": "rápido", "category": "adjective"},
    {"english": "slow", "spanish": "lento", "category": "adjective"},
    {"english": "thank you", "spanish": "gracias", "category": "phrase"},
    {"english": "good morning", "spanish": "buenos días", "category": "phrase"},
    {"english": "good night", "spanish": "buenas noches", "category": "phrase"},
    {"english": "see you later", "spanish": "hasta luego", "category": "phrase"},
    {"english": "excuse me", "spanish": "perdón", "category": "phrase"}
]

def cargar_diccionario():
    if not os.path.exists(RUTA_DICCIONARIO):
        dic = {"entries": DICCIONARIO_INICIAL.copy()}
        guardar_diccionario(dic)
        return dic
    with open(RUTA_DICCIONARIO, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_diccionario(dic):
    with open(RUTA_DICCIONARIO, "w", encoding="utf-8") as f:
        json.dump(dic, f, indent=4, ensure_ascii=False)

def mostrar_entrada(e):
    print(f"EN: {e['english']}  →  ES: {e['spanish']}  ({e['category']})")

def mostrar_todas(dic):
    entradas = dic["entries"]
    if not entradas:
        print("❌ No hay palabras en el diccionario.")
        return
    print("\n📘 Todas las palabras (ordenadas por inglés):")
    for e in sorted(entradas, key=lambda x: x["english"]):
        mostrar_entrada(e)

def buscar(dic):
    palabra = input("Introduce la palabra (EN o ES): ").strip().lower()
    encontrados = []
    for e in dic["entries"]:
        if e["english"].lower() == palabra or e["spanish"].lower() == palabra:
            encontrados.append(e)
    if not encontrados:
        print("❌ Palabra no encontrada.")
        return
    print("\n🔎 Resultados:")
    for e in encontrados:
        mostrar_entrada(e)

def buscar_por_letra(dic):
    letra = input("Introduce la letra inicial (A-Z): ").strip().lower()
    if len(letra) != 1 or not letra.isalpha():
        print("❌ Letra no válida.")
        return
    encontrados = [e for e in dic["entries"] if e["english"].lower().startswith(letra)]
    if not encontrados:
        print(f"❌ No hay palabras que empiecen por '{letra}'.")
        return
    print(f"\n📚 Palabras que empiezan por '{letra}':")
    for e in sorted(encontrados, key=lambda x: x["english"]):
        mostrar_entrada(e)

def buscar_por_categoria(dic):
    print("\nCategorías disponibles:")
    for c in CATEGORIAS_VALIDAS:
        print(f"- {c}")
    cat = input("Introduce la categoría: ").strip().lower()
    if cat not in CATEGORIAS_VALIDAS:
        print("❌ Categoría no válida.")
        return
    encontrados = [e for e in dic["entries"] if e["category"].lower() == cat]
    if not encontrados:
        print(f"❌ No hay palabras en la categoría '{cat}'.")
        return
    print(f"\n📂 Palabras en la categoría '{cat}':")
    for e in sorted(encontrados, key=lambda x: x["english"]):
        mostrar_entrada(e)

def añadir(dic):
    eng = input("Palabra en inglés: ").strip()
    esp = input("Traducción en español: ").strip()
    print("\nCategorías posibles:")
    for c in CATEGORIAS_VALIDAS:
        print(f"- {c}")
    cat = input("Categoría (noun/verb/adjective/adverb/phrase/other): ").strip().lower()
    if cat not in CATEGORIAS_VALIDAS:
        cat = "other"
    nueva = {"english": eng, "spanish": esp, "category": cat}
    dic["entries"].append(nueva)
    guardar_diccionario(dic)
    print("✔ Palabra añadida correctamente.")

def main():
    dic = cargar_diccionario()
    while True:
        print("\n=== Oxford Pocket Casero ===")
        print("1. Mostrar todas las palabras")
        print("2. Buscar palabra (EN/ES)")
        print("3. Buscar por letra inicial")
        print("4. Buscar por categoría")
        print("5. Añadir nueva palabra")
        print("6. Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            mostrar_todas(dic)
        elif opcion == "2":
            buscar(dic)
        elif opcion == "3":
            buscar_por_letra(dic)
        elif opcion == "4":
            buscar_por_categoria(dic)
        elif opcion == "5":
            añadir(dic)
        elif opcion == "6":
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    main()
