"""Baut die installierbare PWA nach docs/ aus app.html (GitHub Pages)."""
from pathlib import Path
from PIL import Image, ImageDraw

root = Path(__file__).parent
out = root / "docs"
out.mkdir(exist_ok=True)
app = (root / "app.html").read_text(encoding="utf-8")
VERSION = "2"

head = """<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#0E6B66">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Schulterpause">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon-192.png">
<link rel="apple-touch-icon" href="icon-180.png">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}[hidden]{display:none!important}</style>
</head>
<body>
"""
tail = """
<script>if ("serviceWorker" in navigator) navigator.serviceWorker.register("sw.js");</script>
</body>
</html>
"""
(out / "index.html").write_text(head + app + tail, encoding="utf-8")

(out / "manifest.webmanifest").write_text("""{
  "name": "Katjas Schulterpause",
  "short_name": "Schulterpause",
  "lang": "de",
  "start_url": "./",
  "scope": "./",
  "display": "standalone",
  "background_color": "#EEF3F2",
  "theme_color": "#0E6B66",
  "icons": [
    { "src": "icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable" }
  ]
}
""", encoding="utf-8")

(out / "sw.js").write_text(f"""const CACHE = "schulterpause-v{VERSION}";
const FILES = ["./", "index.html", "manifest.webmanifest", "icon-192.png", "icon-512.png", "icon-180.png"];
self.addEventListener("install", e => {{ e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES))); self.skipWaiting(); }});
self.addEventListener("activate", e => {{ e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))); self.clients.claim(); }});
self.addEventListener("fetch", e => {{
  if (e.request.method !== "GET") return;
  e.respondWith(caches.match(e.request).then(hit => hit || fetch(e.request).then(res => {{
    if (res.ok && (e.request.url.startsWith(self.location.origin) || e.request.url.includes("fonts.g"))) {{
      const copy = res.clone(); caches.open(CACHE).then(c => c.put(e.request, copy));
    }}
    return res;
  }}).catch(() => caches.match("index.html"))));
}});
""", encoding="utf-8")

def icon(size):
    s = 4  # supersampling
    S = size * s
    im = Image.new("RGB", (S, S), "#0E6B66")
    d = ImageDraw.Draw(im)
    w = int(S * 0.07)
    # Kopf
    r = S * 0.11
    cx, cy = S / 2, S * 0.36
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill="#EEF3F2")
    # Schulterbogen
    d.arc([S * 0.2, S * 0.52, S * 0.8, S * 1.0], 200, 340, fill="#EEF3F2", width=w)
    im.resize((size, size), Image.LANCZOS).save(out / f"icon-{size}.png")

for n in (180, 192, 512):
    icon(n)
print("PWA gebaut in", out)
