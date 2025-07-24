import streamlit as st
import random
import re

def intercalar_insultos_ligero(texto, insultos=None):
    if insultos is None:
        insultos = ["pelotudo", "boludo", "salame", "inútil", "tarado", "imbécil", "mogólico",
    "flaco", "bobo", "cabeza de termo", "mamerto", "cara de verga", "cara de culo",
    "gil", "soquete", "fantasma", "papanatas", "payaso", "choto", "trucho", "atrasado",
    "forro", "cornudo", "chupapija", "ganso", "chorro", "ladrón", "vendehumo",
    "petiso", "ridículo", "pelo duro", "pancho", "pajero", "careta", "muerto", 
    "concheto", "pichi", "lento", "cascote", "mamarracho", "cara rota", 
    "ñoqui", "ñeri", "gato", "rata", "plaga", "boludón", "triste", 
    "muerto de hambre", "mugriento", "parásito", "morsa", "cucaracha", "culeado",
    "manija", "retrasado", "inservible", "venado", "culebrón", "perro", "desubicado",
    "cara de nada", "sorete", "fiambre", "larva", "lechuga", "burro", "pato criollo"]

    oraciones_raw = re.split(r'(?<=[.!?])\s+', texto)
    resultado = []

    for oracion_completa in oraciones_raw:
        if not oracion_completa.strip():
            continue

        match = re.match(r'(.+?)([.!?])?$', oracion_completa.strip())
        cuerpo = match.group(1)
        puntuacion = match.group(2) or ''

        palabras = cuerpo.split()
        if not palabras:
            continue

        num_insultos = min(len(palabras), random.randint(1, 2))
        posiciones = sorted(random.sample(range(len(palabras)), k=num_insultos))

        for pos in reversed(posiciones):
            insulto = random.choice(insultos)
            palabras.insert(pos + 1, insulto)

        nueva_oracion = ' '.join(palabras) + puntuacion
        resultado.append(nueva_oracion)

    return ' '.join(resultado)

# INTERFAZ
st.title("🤬 Intercalador de Insultos")
texto_usuario = st.text_area("Pegá tu texto aquí:", height=200)

if st.button("Insultar"):
    if texto_usuario.strip():
        resultado = intercalar_insultos_ligero(texto_usuario)
        st.markdown("### Resultado:")
        st.write(resultado)
    else:
        st.warning("Por favor, escribí o pegá un texto primero.")
