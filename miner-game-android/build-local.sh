#!/usr/bin/env bash
# Compilación local (requiere Node 20, JDK 17 y el SDK de Android con ANDROID_HOME configurado)
set -e
npm install
[ -d android ] || npx cap add android
npx capacitor-assets generate --android
python3 tools/patch_android.py android
npx cap sync android
(cd android && ./gradlew assembleDebug)
cp android/app/build/outputs/apk/debug/app-debug.apk the-miner-game.apk
echo "Listo: the-miner-game.apk"
