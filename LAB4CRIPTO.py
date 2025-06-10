


from Crypto.Cipher import DES, DES3, AES
from Crypto.Util.Padding import pad, unpad
import binascii
import base64

# largos que necesitan cada algoritmo
REQUISITOS = {
    "DES": {"clave": 8, "iv": 8},
    "3DES": {"clave": 24, "iv": 8},
    "AES": {"clave": 32, "iv": 16}
}

# En caso de faltar longitud a la clave se le agrega un padding para completar, en este caso zeropadding
def preparar_clave(clave_txt, largo):
    clave_bytes = clave_txt.encode()
    if len(clave_bytes) < largo:
        clave_bytes += b'\x00' * (largo - len(clave_bytes))
    return clave_bytes[:largo]  # por si es más larga se cortaa

# Mismo caso para el vector en caso de que le falte longitud se le agrega un padding 
def preparar_iv(iv_txt, largo):
    iv_bytes = iv_txt.encode()
    if len(iv_bytes) < largo:
        iv_bytes += b'\x00' * (largo - len(iv_bytes))
    return iv_bytes[:largo]



# Función que cifra el texto (con PKCS7, lo saqué de la documentación de pycryptodome)
def cifrar_texto(nombre_algo, texto, clave, iv):
    if nombre_algo == "DES":
        bloque = 8
        cipher = DES.new(clave, DES.MODE_CBC, iv)
    elif nombre_algo == "3DES":
        bloque = 8
        cipher = DES3.new(clave, DES3.MODE_CBC, iv)
    else:
        bloque = 16
        cipher = AES.new(clave, AES.MODE_CBC, iv)

    texto_padded = pad(texto.encode(), bloque)
    cifrado = cipher.encrypt(texto_padded)

    print("\n Resultados:")
    print("En HEX:", binascii.hexlify(cifrado).decode())
    print("En BASE64:", base64.b64encode(cifrado).decode())




# Función para descifrar, también con PKCS7
def descifrar_texto(nombre_algo, texto_hex, clave, iv):
    cifrado = binascii.unhexlify(texto_hex)

    if nombre_algo == "DES":
        bloque = 8
        cipher = DES.new(clave, DES.MODE_CBC, iv)
    elif nombre_algo == "3DES":
        bloque = 8
        cipher = DES3.new(clave, DES3.MODE_CBC, iv)
    else:
        bloque = 16
        cipher = AES.new(clave, AES.MODE_CBC, iv)

    descifrado_padded = cipher.decrypt(cifrado)
    try:
        descifrado = unpad(descifrado_padded, bloque)
        print("\n Texto original")
        print("Plano:", descifrado.decode())
        print("BASE64:", base64.b64encode(descifrado).decode())
    except ValueError:
        print("No se pudo descifrar. Algo no calza.")


# menú
print("Algoritmos disponibles:")
print("1. DES")
print("2. 3DES")
print("3. AES-256")

opcion = input("Elige uno (1/2/3): ")
if opcion == "1":
    algoritmo = "DES"
elif opcion == "2":
    algoritmo = "3DES"
elif opcion == "3":
    algoritmo = "AES"
else:
    print("Opción inválida.")
    exit()

print("\n¿Quieres cifrar o descifrar?")
print("1. Cifrar")
print("2. Descifrar")
modo = input("Elige uno (1/2): ")

texto = input("\nIngresa el texto: ") if modo == "1" else input("\nIngresa texto HEX: ")
clave = input("Clave (key): ")
vector = input("IV: ")

clave_final = preparar_clave(clave, REQUISITOS[algoritmo]["clave"])
iv_final = preparar_iv(vector, REQUISITOS[algoritmo]["iv"])

print(f"\nClave lista: {binascii.hexlify(clave_final).decode()}")
print(f"IV listo: {binascii.hexlify(iv_final).decode()}")

if modo == "1":
    cifrar_texto(algoritmo, texto, clave_final, iv_final)
else:
    descifrar_texto(algoritmo, texto, clave_final, iv_final)
