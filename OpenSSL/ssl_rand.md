# OPENSSL
## MÉTODO RAND

### Herramienta de generación de números pseudoaleatorios con OpenSSL

---

### NOMBRE
`openssl rand` → Genera datos pseudoaleatorios con OpenSSL.

### DESCRIPCIÓN
El comando `openssl rand` genera datos pseudoaleatorios, útiles para la creación de:
- Claves criptográficas.
- Tokens de sesión.
- Otros datos de seguridad.

### EJECUCIÓN Y SINTAXIS

```bash
openssl rand [-out archivo] [-hex|-base64] [-engine motor] nobytes
```

- **nobytes**: Número de bytes a generar.
- **-out archivo**: Especifica un archivo para guardar la salida.
- **-hex**: Formato de salida en hexadecimal.
- **-base64**: Formato de salida en Base64.
- **-engine motor**: Especifica el motor de hardware que se utilizará para la generación de números aleatorios, si está disponible.

---

## PLANTEAMIENTO DE ACTIVIDAD

#### Ejercicio Avanzado:

Generación y Gestión de Claves para Cifrado y Firma Digital en un Sistema de Mensajería Segura

#### Objetivo
Implementar un sistema de mensajería segura utilizando claves criptográficas generadas con `openssl rand`. Este ejercicio tiene como objetivo aplicar conceptos de:
- Criptografía simétrica y asimétrica.
- Generación de claves seguras.
- Autenticación de mensajes.

#### Escenario
Eres parte del equipo de seguridad de una empresa que necesita proteger su sistema de mensajería para evitar que los mensajes sean interceptados, alterados o enviados por usuarios no autorizados. Para ello, implementarás un sistema de cifrado y firma digital basado en claves generadas con OpenSSL.