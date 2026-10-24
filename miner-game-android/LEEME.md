# The Miner Game · APK de Android

Proyecto Capacitor: el juego (www/index.html) se empaqueta como una app Android independiente,
sin navegador, en horizontal y a pantalla completa. Funciona sin conexión (la música y los sonidos se generan en el propio juego).

## Opción A — sin instalar nada (recomendada): GitHub Actions
1. Crea un repositorio en GitHub (puede ser privado) y sube TODO el contenido de esta carpeta, incluida la carpeta oculta `.github`.
2. Abre la pestaña **Actions** → «Build APK». Se lanza sola con cada subida (tarda unos 5–8 minutos). Si no, pulsa «Run workflow».
3. Al terminar tienes el APK de dos formas:
   - **Releases** del repositorio → «The Miner Game (última build)» → `the-miner-game.apk` (descargable desde el propio móvil).
   - Dentro de la ejecución, en **Artifacts** → `the-miner-game-apk` (un .zip con el APK).
4. En el móvil: abre el .apk y permite «Instalar apps de origen desconocido» para el navegador/gestor de archivos.

## Opción B — en tu ordenador
Requisitos: Node 20, JDK 17, Android SDK (variable ANDROID_HOME). Ejecuta `./build-local.sh`; el resultado es `the-miner-game.apk`.

## Notas
- Es una build de **depuración**: sirve para instalar y jugar. Para Google Play hay que firmar un paquete de lanzamiento (.aab).
- La partida se guarda en el propio dispositivo (se conserva al actualizar la app instalando encima del APK anterior).
- Para actualizar el juego: sustituye `www/index.html` y vuelve a lanzar la compilación.
