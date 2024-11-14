
# Ejercicio Avanzado

#### Generación y Gestión de Claves para Cifrado y Firma Digital en un Sistema de Mensajería Segura

## Instrucciones

### Parte 1: Generación de Claves de Usuario y Configuración Inicial

1. **Generar una clave simétrica de 64 bytes para el cifrado de mensajes:**

   Usa `openssl rand` para crear una clave de 64 bytes en formato hexadecimal y guarda esta clave en un archivo llamado `clave_simetrica.hex`.

   ```bash
   openssl rand -hex 64 -out clave_simetrica.hex
   ```

2. **Generar un par de claves asimétricas (pública y privada) para cada usuario**

   Cada usuario (por ejemplo, Bonilla y Rubén) debe tener su propio par de claves para firmar y verificar los mensajes.

   - Genera el par de claves RSA de 2048 bits para **Bonilla** y guárdalos en los archivos `bonilla_privada.pem` y `bonilla_publica.pem`.

     ```bash
     openssl genpkey -algorithm RSA -out bonilla_privada.pem -pkeyopt rsa_keygen_bits:2048
     openssl rsa -pubout -in bonilla_privada.pem -out bonilla_publica.pem
     ```

   - Repite los pasos anteriores para **Rubén**, guardando sus claves en `ruben_privada.pem` y `ruben_publica.pem`.

### Parte 2: Envío de Mensajes Cifrados y Firmados

1. **Cifrar un mensaje**

   - Crea un mensaje en un archivo llamado `mensaje.txt` con el texto “Confidencial: Proyecto secreto”.

   - Utiliza la clave simétrica generada en la Parte 1 para cifrar el mensaje usando AES-256-CBC y guarda el mensaje cifrado en `mensaje_cifrado.enc`.

     ```bash
     openssl enc -aes-256-cbc -in mensaje.txt -out mensaje_cifrado.enc -pass file:clave_simetrica.hex
     ```

2. **Firmar el mensaje cifrado**

   - Usa la clave privada de **Bonilla** (`bonilla_privada.pem`) para crear una firma digital del mensaje cifrado.

   - Almacena la firma en un archivo llamado `firma_mensaje.bin`.

     ```bash
     openssl dgst -sha256 -sign bonilla_privada.pem -out firma_mensaje.bin mensaje_cifrado.enc
     ```

3. **Compartir la clave simétrica de forma segura**

   - Cifra el archivo `clave_simetrica.hex` con la clave pública de **Rubén** para que solo él pueda descifrarla. Guarda el resultado en `clave_simetrica_cifrada.enc`.

     ```bash
     openssl rsautl -encrypt -inkey ruben_publica.pem -pubin -in clave_simetrica.hex -out clave_simetrica_cifrada.enc
     ```

### Parte 3: Recepción y Verificación de Mensajes

1. **Descifrar la clave simétrica**

   - **Rubén** recibe `clave_simetrica_cifrada.enc` y usa su clave privada (`ruben_privada.pem`) para descifrar la clave simétrica y guardarla en `clave_simetrica_ruben.hex`.

     ```bash
     openssl rsautl -decrypt -inkey ruben_privada.pem -in clave_simetrica_cifrada.enc -out clave_simetrica_ruben.hex
     ```

2. **Descifrar el mensaje**

   - Con la clave simétrica descifrada, **Rubén** puede descifrar el mensaje original usando AES-256-CBC, y guarda el mensaje en `mensaje_descifrado.txt`.

     ```bash
     openssl enc -d -aes-256-cbc -in mensaje_cifrado.enc -out mensaje_descifrado.txt -pass file:clave_simetrica_ruben.hex
     ```

3. **Verificar la firma del mensaje**

   - **Rubén** verifica la autenticidad del mensaje cifrado utilizando la clave pública de **Bonilla** (`bonilla_publica.pem`).

     ```bash
     openssl dgst -sha256 -verify bonilla_publica.pem -signature firma_mensaje.bin mensaje_cifrado.enc
     ```

   - Si la firma es válida, **Rubén** sabe que el mensaje fue enviado por **Bonilla** y no ha sido alterado. 

--- 

Este sistema garantiza la confidencialidad, autenticidad e integridad de los mensajes en el sistema de mensajería.