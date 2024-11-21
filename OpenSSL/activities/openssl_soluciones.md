# OPENSSL SOLUCIONES

### EXERICICI 1 
a)  Codifica una imatge PNG qualsevol que tinguis disponible al sistema en Base64. Això ho pots fer executant la comanda `openssl enc -e -a -in foto.png -out foto.png.b64` (en aquest exemple la imatge s'anomena "foto.png"). ¿Quin és el contingut de l'arxiu "foto.png.b64" (obre'l amb un editor de text)?


```bash
bonilla@bonilla ~/D/M/O/activities (main)> openssl enc -e -a -in foto.png -out foto.png.b64
bonilla@bonilla ~/D/M/O/activities (main)> ll
total 128K
-rw-rw-r-- 1 bonilla bonilla 13K nov 21 20:10 foto.png
-rw-rw-r-- 1 bonilla bonilla 18K nov 21 20:12 foto.png.b64
-rw-rw-r-- 1 bonilla bonilla 88K nov 21 20:06 openssl_exercicis.pdf
-rw-rw-r-- 1 bonilla bonilla 359 nov 21 20:11 openssl_soluciones.md
```
- Aquest es el contingut del arxiu `foto.png.64`.
![Text alternatiu](fotos_md/foto_fotobase64.png)

b) Elimina uns quants caràcters qualssevol ubicats al mig del contingut de "foto.png.b64" (ha de ser al mig per tal de no modificar el "magic number" del fitxer) i genera la imatge corresponent a partir d'aquest fitxer modificat executant la comanda `openssl enc -d -a -in foto.png.b64 -out novafoto.png`  Intenta obrir amb un visor de fotos (per exemple, "eog") el fitxer "novafoto.png". ¿Què veus? ¿Què et diu la comanda file novafoto.png?

```bash
bonilla@bonilla ~/D/M/O/activities (main)> openssl enc -d -a -in foto.png.b64 -out novafoto.png
bonilla@bonilla ~/D/M/O/activities (main)> ll
total 244K
-rw-rw-r-- 1 bonilla bonilla  97K nov 21 20:14 foto_fotobase64.png
-rw-rw-r-- 1 bonilla bonilla  13K nov 21 20:10 foto.png
-rw-rw-r-- 1 bonilla bonilla  18K nov 21 20:19 foto.png.b64
-rw-rw-r-- 1 bonilla bonilla  13K nov 21 20:20 novafoto.png
-rw-rw-r-- 1 bonilla bonilla  88K nov 21 20:06 openssl_exercicis.pdf
-rw-rw-r-- 1 bonilla bonilla 1,3K nov 21 20:19 openssl_soluciones.md
```
- Pel tipus de ubuntu no es pot obrir.
![Text alternatiu](fotos_md/cap_novafoto.png)

