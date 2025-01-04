from flask import Flask, request, redirect, render_template, url_for
import sqlite3
import string
import random
from datetime import datetime

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS urls
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         original_url TEXT NOT NULL,
         short_code TEXT NOT NULL UNIQUE,
         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
         clicks INTEGER DEFAULT 0)
    ''')
    conn.commit()
    conn.close()

def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choice(chars) for _ in range(length))
        # Check if code already exists
        conn = sqlite3.connect('urls.db')
        c = conn.cursor()
        existing = c.execute('SELECT 1 FROM urls WHERE short_code = ?', (code,)).fetchone()
        conn.close()
        if not existing:
            return code

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        if not original_url.startswith(('http://', 'https://')):
            original_url = 'https://' + original_url
            
        short_code = generate_short_code()
        
        conn = sqlite3.connect('urls.db')
        c = conn.cursor()
        c.execute('INSERT INTO urls (original_url, short_code) VALUES (?, ?)',
                 (original_url, short_code))
        conn.commit()
        conn.close()
        
        short_url = request.host_url + short_code
        return render_template('index.html', short_url=short_url)
    
    return render_template('index.html')

@app.route('/<short_code>')
def redirect_to_url(short_code):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    result = c.execute('SELECT original_url FROM urls WHERE short_code = ?', 
                      (short_code,)).fetchone()
    
    if result:
        original_url = result[0]
        c.execute('UPDATE urls SET clicks = clicks + 1 WHERE short_code = ?', 
                 (short_code,))
        conn.commit()
        conn.close()
        return redirect(original_url)
    conn.close()
    return "URL not found", 404

@app.route('/stats')
def stats():
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    urls = c.execute('''
        SELECT short_code, original_url, created_at, clicks 
        FROM urls 
        ORDER BY created_at DESC
    ''').fetchall()
    conn.close()
    return render_template('stats.html', urls=urls)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
