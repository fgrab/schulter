# Katjas Schulterpause

Kleine Web-App (PWA) mit geführten Routinen zum Lockern, Dehnen und Kräftigen von Schulter, Nacken und oberer Brust – gegen Schreibtisch- und Lenkerhaltung.

- **Routinen:** Morgens (≈4 Min), Schreibtisch (≈2 Min), Nach dem Radfahren (≈7 Min), Abends auf der Matte (≈10 Min), Kräftigung (≈7 Min)
- **Hilfsmittel wählbar:** Theraband, Faszienrolle, Yoga-Block – sonst werden Alternativen ohne genommen
- **Geführter Timer** mit Skizzen, Seitenwechsel, Ton und Vibration
- Läuft offline und lässt sich auf dem Handy zum Homescreen hinzufügen

## Aufbau

- `app.html` – die ganze App (Übungen, Routinen, Skizzen, Player). Hier wird geändert.
- `build.py` – baut daraus die PWA nach `docs/` (index.html, Manifest, Service Worker, Icons). Braucht Python 3 mit Pillow.
- `docs/` – wird von GitHub Pages ausgeliefert.

Nach einer Änderung an `app.html`:

```bash
python3 build.py
```

Dann `VERSION` in `build.py` hochzählen, damit installierte Apps die neue Version laden.

## Hinweis

Dehnen soll ziehen, aber nicht wehtun. Bei Kribbeln, ausstrahlenden oder anhaltenden Schmerzen bitte ärztlich oder physiotherapeutisch abklären lassen.
