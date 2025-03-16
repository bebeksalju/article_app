# FastAPI CRUD API 🚀

![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-blue?style=flat-square&logo=fastapi)  
API sederhana menggunakan **FastAPI** dan **PostgreSQL** untuk mengelola artikel.  

## 📌 Fitur  
✅ **CRUD Artikel** (Create, Read, Update, Delete)  
✅ **Validasi Data dengan Pydantic**  
✅ **Database PostgreSQL dengan SQLAlchemy**  
✅ **Swagger UI dan Redoc otomatis**  

## 🚀 Instalasi  

### 1. Clone Repo  
```bash
git clone https://github.com/username/repo-fastapi-crud.git
cd repo-fastapi-crud
```
### 2. Buat Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Buat File .env
Buat file .env di root proyek dan tambahkan konfigurasi berikut:
```bash
DATABASE_URL=postgresql://user:password@localhost:5432/db_name
```
### 5. Jalankan Server
```bash
uvicorn main:app --reload
```
Server akan berjalan di http://127.0.0.1:8000

### 📖 Dokumentasi API
FastAPI menyediakan dokumentasi otomatis:_  
🔹 Swagger UI: http://127.0.0.1:8000/docs_  
🔹 Redoc: http://127.0.0.1:8000/redoc

### 🔧 Struktur Proyek
```bash
📂 fastapi-crud
 ┣ 📂 models          # Model database
 ┣ 📂 schemas         # Schema Pydantic
 ┣ 📂 routes          # Routing API
 ┣ 📜 main.py         # Entry point FastAPI
 ┣ 📜 database.py     # Koneksi database
 ┣ 📜 requirements.txt # Dependensi proyek
 ┣ 📜 .env            # Konfigurasi rahasia
 ┣ 📜 .gitignore      # File yang diabaikan git
 ┗ 📜 README.md       # Dokumentasi ini
```

### 📌 Endpoint API
Method	Endpoint:
```bash
GET	/articles               # Get semua artikel
GET	/articles/{id}          # Get artikel by ID
POST	/articles              # Buat artikel baru
PUT	/articles/{id}          # Update artikel
DELETE	/articles/{id}       # Hapus artikel
```

### 🌟 Kontribusi
Pull request sangat diterima!
