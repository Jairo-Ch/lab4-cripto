# Laboratorio 4 - Cifrado Simétrico en Python

Este proyecto consiste en un programa desarrollado en Python que permite cifrar y descifrar mensajes utilizando tres algoritmos de cifrado simétrico:

- **DES**
- **3DES**
- **AES-256**

El programa utiliza el modo de operación **CBC** (Cipher Block Chaining) y padding **PKCS#7** para el texto, mientras que ajusta automáticamente la longitud de la clave (key) e IV si son demasiado cortos o largos.

## Requisitos
- Python 3.x
- Librería `pycryptodome`

Es recomendable crear un entorno virtual antes de instalar los paquetes:

```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install pycryptodome
```
## Como usarlo ?
1. Ejecuta el archivo Python desde la terminal:
   ```bash
      python LAB4CRIPTO.py
   ```
2. El programa solicitará:
    * El algoritmo a usar (DES, 3DES, AES-256)
    * La operación a realizar (cifrar o descifrar)
    * El texto, la clave (key) y el vector de inicialización (IV)
3. Como salida, se mostrará el texto cifrado (o descifrado en formato):
    * Hex
    * BASE64

  
