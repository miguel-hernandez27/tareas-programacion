def contador_palabras():
    
    # Palabras a ignorar
    palabras_ignoradas = {'el', 'la', 'de', 'y', 'a', 'un', 'una'}
    
    # Signos de puntuación a eliminar
    puntuacion = '.,;:!?'
    
    while True:
        print("\n" + "="*60)
        print("CONTADOR DE PALABRAS - El Quijote 2.0")
        print("="*60)
        
        # 1. Solicitar texto al usuario
        texto = input("\nIngrese el texto a analizar ('salir' para terminar):\n> ")
        
        if texto.lower() == 'salir':
            print("\n¡Gracias por usar el Contador de Palabras!")
            break
        
        if not texto.strip():
            print(" Por favor, ingrese un texto válido.")
            continue
        
        # 2. Convertir a minúsculas y eliminar puntuación
        texto_procesado = texto.lower()
        
        # Reemplazar signos de puntuación por espacios
        for signo in puntuacion:
            texto_procesado = texto_procesado.replace(signo, ' ')
        
        # 3. Separar el texto en palabras
        palabras = texto_procesado.split()
        
        # 4. Filtrar palabras ignoradas
        palabras_filtradas = [
            palabra for palabra in palabras 
            if palabra not in palabras_ignoradas and palabra.strip()
        ]
        
        # 5. Contar frecuencias manualmente
        if not palabras_filtradas:
            print("\nNo hay palabras válidas para analizar después de filtrar.")
            continue
        
        # Crear diccionario de frecuencias sin usar Counter
        frecuencias = {}
        for palabra in palabras_filtradas:
            if palabra in frecuencias:
                frecuencias[palabra] += 1
            else:
                frecuencias[palabra] = 1
        
        # Mostrar resultados
        print("\n" + "-"*60)
        print("RESULTADOS DEL ANÁLISIS")
        print("-"*60)
        
        # Cantidad total de palabras (sin contar ignoradas)
        total_palabras = len(palabras_filtradas)
        print(f"\nCantidad total de palabras (sin contar palabras ignoradas): {total_palabras}")
        
        # Cantidad de palabras únicas
        palabras_unicas = len(frecuencias)
        print(f"Cantidad de palabras únicas: {palabras_unicas}")
        
        # Top 5 palabras más repetidas (ordenar manualmente)
        print(f"\nTop 5 palabras más repetidas:")
        print("-"*60)
        
        # Ordenar frecuencias de mayor a menor
        palabras_ordenadas = []
        for palabra, freq in frecuencias.items():
            palabras_ordenadas.append((palabra, freq))
        
        # Ordenamiento por burbuja (sin usar sorted)
        for i in range(len(palabras_ordenadas)):
            for j in range(i + 1, len(palabras_ordenadas)):
                if palabras_ordenadas[j][1] > palabras_ordenadas[i][1]:
                    palabras_ordenadas[i], palabras_ordenadas[j] = palabras_ordenadas[j], palabras_ordenadas[i]
        
        # Mostrar top 5
        top_5 = palabras_ordenadas[:5]
        
        if top_5:
            for i, (palabra, frecuencia) in enumerate(top_5, 1):
                print(f"{i}. {palabra} -> {frecuencia}")
        
        print("-"*60)

if __name__ == "__main__":
    contador_palabras()