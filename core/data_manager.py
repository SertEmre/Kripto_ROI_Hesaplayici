import pandas as pd
import sqlite3
import hashlib
import os

DB_FILE = "data/kripto_veritabani.db"

def veritabani_baglantisi_al():
    if not os.path.exists("data"):
        os.makedirs("data")
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    return conn

def tablolar_olustur():
    conn = veritabani_baglantisi_al()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS portfoy (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            sembol TEXT,
            miktar REAL,
            maliyet REAL,
            tarih TEXT,
            FOREIGN KEY (username) REFERENCES users(username)
        )
    """)
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    conn = veritabani_baglantisi_al()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", 
                       (username, hash_password(password)))
        conn.commit()
        return True, "Kayıt başarılı! Lütfen giriş yapın."
    except sqlite3.IntegrityError:
        return False, "Bu kullanıcı adı zaten mevcut!"
    finally:
        conn.close()

def verify_user(username, password):
    conn = veritabani_baglantisi_al()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password_hash = ?", 
                   (username, hash_password(password)))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def verileri_yukle(username):
    conn = veritabani_baglantisi_al()
    query = "SELECT sembol as Sembol, miktar as Miktar, maliyet as Maliyet, tarih as Tarih FROM portfoy WHERE username = ?"
    df = pd.read_sql_query(query, conn, params=(username,))
    conn.close()
    
    if df.empty:
        return pd.DataFrame(columns=["Sembol", "Miktar", "Maliyet", "Tarih"])
    return df

def veri_ekle(username, sembol, miktar, maliyet, tarih):
    conn = veritabani_baglantisi_al()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO portfoy (username, sembol, miktar, maliyet, tarih) 
        VALUES (?, ?, ?, ?, ?)
    """, (username, sembol, miktar, maliyet, tarih))
    conn.commit()
    conn.close()
    return True

def verileri_sifirla(username):
    conn = veritabani_baglantisi_al()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM portfoy WHERE username = ?", (username,))
    conn.commit()
    conn.close()
    return True

tablolar_olustur()