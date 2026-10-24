#!/usr/bin/env python3
"""Ajustes del proyecto Android generado por Capacitor: horizontal, pantalla completa inmersiva,
cámara con muesca, vibración y pantalla siempre encendida. Se ejecuta tras `npx cap add android`."""
import glob, os, re, sys
root = sys.argv[1] if len(sys.argv) > 1 else 'android'
def edit(path, fn):
    s = open(path, encoding='utf-8').read(); n = fn(s)
    if n != s: open(path, 'w', encoding='utf-8').write(n); print('OK  ', path)
    else: print('=   ', path, '(sin cambios)')
# Manifiesto: orientación horizontal + vibración
man = os.path.join(root, 'app/src/main/AndroidManifest.xml')
def f_man(s):
    if 'screenOrientation' not in s: s = s.replace('<activity ', '<activity android:screenOrientation="sensorLandscape" ', 1)
    if 'VIBRATE' not in s: s = s.replace('<application', '<uses-permission android:name="android.permission.VIBRATE"/>\n    <application', 1)
    return s
edit(man, f_man)
# Tema: pantalla completa y uso de la zona de la muesca
for st in glob.glob(os.path.join(root, 'app/src/main/res/values/styles.xml')):
    def f_st(s):
        if 'windowFullscreen' in s: return s
        return re.sub(r'(<style name="AppTheme\.NoActionBar"[^>]*>)(.*?)(</style>)',
            lambda m: m.group(1) + m.group(2) + '    <item name="android:windowFullscreen">true</item>\n    <item name="android:windowLayoutInDisplayCutoutMode">shortEdges</item>\n' + m.group(3), s, count=1, flags=re.S)
    edit(st, f_st)
# Actividad: modo inmersivo y pantalla encendida
for ja in glob.glob(os.path.join(root, 'app/src/main/java/**/MainActivity.java'), recursive=True):
    def f_ja(s):
        if 'IMMERSIVE_STICKY' in s: return s
        body = '''public class MainActivity extends BridgeActivity {
  @Override protected void onCreate(android.os.Bundle b) {
    super.onCreate(b);
    getWindow().addFlags(android.view.WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
  }
  @Override public void onWindowFocusChanged(boolean hasFocus) {
    super.onWindowFocusChanged(hasFocus);
    if (hasFocus) getWindow().getDecorView().setSystemUiVisibility(
      android.view.View.SYSTEM_UI_FLAG_LAYOUT_STABLE | android.view.View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
      | android.view.View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN | android.view.View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
      | android.view.View.SYSTEM_UI_FLAG_FULLSCREEN | android.view.View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY);
  }
}'''
        return re.sub(r'public class MainActivity extends BridgeActivity\s*\{\s*\}', body, s, count=1)
    edit(ja, f_ja)
