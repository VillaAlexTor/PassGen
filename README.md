# PassGen - Generador de Contraseñas Seguras

PassGen es una aplicación de escritorio diseñada para generar contraseñas robustas y seguras de manera sencilla. Utiliza una interfaz gráfica intuitiva construida con Python para facilitar su uso a cualquier persona.

## Características

- **Longitud Personalizable:** Genera contraseñas desde 8 hasta 128 caracteres.
- **Tipos de Caracteres Seleccionables:**
  - Letras Mayúsculas (A-Z)
  - Letras Minúsculas (a-z)
  - Dígitos (0-9)
  - Caracteres Especiales (!@#$%...)
- **Interfaz Intuitiva:** Barra deslizante para longitud y botones rápidos para selección.
- **Copia Rápida:** Botón dedicado para copiar la contraseña generada al portapapeles.
- **Diseño Moderno:** Ventana centrada y organizada para una mejor experiencia de usuario.

## Herramientas Utilizadas

- **Lenguaje:** Python 3
- **Interfaz Gráfica (GUI):** `tkinter` y `tkinter.ttk`.
- **Seguridad:** Módulo `secrets` para generación de números aleatorios criptográficamente seguros.

## Seguridad (Punto Crítico)

La seguridad es la prioridad de este proyecto. A diferencia de otros generadores que utilizan el módulo `random` (el cual es determinista y no apto para seguridad), PassGen utiliza el módulo **`secrets`** de Python.

> [!IMPORTANT]
> El módulo `secrets` se utiliza para generar números aleatorios criptográficamente fuertes adecuados para gestionar datos como contraseñas, autenticación de cuentas, tokens de seguridad y secretos relacionados. Esto garantiza que las contraseñas generadas sean prácticamente imposibles de predecir.

## Instalación y Uso

1. Asegúrate de tener Python instalado en tu sistema.
2. Clona este repositorio o descarga el archivo `passgen.py`.
3. Ejecuta la aplicación desde la terminal:
   ```bash
   python passgen.py
   ```

## Recomendaciones para una Contraseña Segura

- Utiliza al menos **12 caracteres**.
- Combina **todos los tipos de caracteres** (mayúsculas, minúsculas, números y símbolos).
- No compartas tus contraseñas y cámbialas periódicamente.

---
*Desarrollado con enfoque en la seguridad y facilidad de uso.*
