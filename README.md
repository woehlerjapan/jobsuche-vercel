# Vercel FastAPI Variante

Backend: FastAPI als Serverless Function unter `/api/index.py`.  
Frontend: statische Seite in `public/index.html`, ruft `/api/jobs`.

## Lokal testen
```bash
pip install -r requirements.txt
uvicorn api.index:app --reload --host 0.0.0.0 --port 8000
# Frontend öffnen: http://localhost:8000/api/jobs?what=... (nur API)
# oder statisch ausliefern, z.B. mit `python -m http.server` im public/ Ordner
```

## Vercel Deployment
```bash
npm install -g vercel
vercel dev   # lokaler Test inkl. API
vercel deploy --prod
```
Vercel erkennt `api/` automatisch als Python-Function (vercel-python Runtime) und `public/` als statische Assets.
