# MovieWeb App

## 📌 Beschreibung

Die **MovieWeb App** ist eine einfache Webanwendung, die es Benutzern ermöglicht, ihre Lieblingsfilme zu speichern, zu verwalten und mit anderen zu teilen. Die Anwendung nutzt Flask als Webframework und SQLite als Datenbank.

## 🔥 Features

- Benutzerverwaltung (Hinzufügen & Löschen von Nutzern)
- Speichern von Filmen pro Benutzer mit Titel, Regisseur, Erscheinungsjahr, Bewertung und Poster
- Automatische Filmdetailsuche über die **OMDb API**
- Möglichkeit, Filminformationen zu bearbeiten und zu löschen
- Frontend mit HTML, CSS und Jinja2-Templates

## 🛠️ Technologien

- **Python** (Flask, SQLAlchemy, Requests)
- **SQLite** (Datenbankverwaltung)
- **HTML, CSS, Jinja2** (Frontend)
- **OMDb API** (Filmdaten abrufen)

## 🚀 Installation

### 1️⃣ Klone das Repository:

```sh
git clone https://github.com/dein-repository/movieweb_app.git
cd movieweb_app
```

### 2️⃣ Erstelle eine virtuelle Umgebung:

```sh
python -m venv venv
source venv/bin/activate  # für macOS/Linux
venv\Scripts\activate    # für Windows
```

### 3️⃣ Installiere die Abhängigkeiten:

```sh
pip install -r requirements.txt
```

### 4️⃣ Setze die Umgebungsvariablen:

Erstelle eine `.env` Datei und füge deinen **OMDb API Key** hinzu:

```sh
OMDB_API_KEY=your_api_key_here
```

### 5️⃣ Starte die Anwendung:

```sh
python app.py
```

Die Anwendung läuft nun unter [**http://localhost:5000**](http://localhost:5000) 🎬

## 📂 Projektstruktur

```
movieweb_app/
│── data_management/        # Datenbankverwaltung (SQLite, SQLAlchemy)
│── static/                 # Statische Dateien (CSS, Bilder)
│── templates/              # HTML-Templates für Flask
│── app.py                  # Hauptanwendung
│── requirements.txt         # Abhängigkeiten
│── README.md               # Dokumentation
│── .env                    # API-Schlüssel (nicht in Git einchecken!)
```

## 🔑 API & Datenbank

- **OMDb API** wird verwendet, um Filmdaten abzurufen.
- **SQLite** speichert Benutzer- und Filmdaten.


