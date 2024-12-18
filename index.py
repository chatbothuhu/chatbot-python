from flask import Flask, render_template, request
import re
import math
import random
import logging

app = Flask(__name__)

# Fungsi percakapan
def handle_conversation(user_text):
    user_text = user_text.lower()
    if "hello" in user_text or "halo" in user_text or "hai" in user_text or "hi" in user_text:
        return "Hai, aku Mathdy! Ada yang bisa aku bantu?"
    elif "terima kasih" in user_text or "thank you" in user_text or "thanks" in user_text:
        return "Sama-sama, senang bisa membantu!"
    elif "tips belajar" in user_text or "tips" in user_text or "tips Mathdy" in user_text:
        return """
        <h3>Tips Belajar Matematika ala Mathdy:</h3>
            <ul>
                <li><h3>Pahami konsep dasar materi</h3></li>
                <li><h3>Belajar dari berbagai sumber</h3></li>
                <li><h3>Rajin latihan soal</h3></li>
                <li><h3>Belajar secara berkelompok</h3></li>
                <li><h3>Buat jadwal belajar rutin</h3></li>
            </ul>
        """  
    elif "rekomendasi aplikasi" in user_text or "aplikasi" in user_text:
         return """
        <h3>Rekomendasi Aplikasi untuk Belajar Matematika ala Mathdy:</h3>
            <ul>
                <li><h3>Photomath: aplikasi ini dapat mendeteksi angka dan simbol yang kamu foto lalu menyajikan hasil dan cara pengerjaannya</li>
                <li><h3>CoLearn: aplikasi ini menyediakan video pembelajaran yang membahas soal matematika dalam bentuk cerita</h3></li>
                <li><h3>Graphing Calculator + Math: aplikasi yang dapat menyelesaikan soal berbentuk persamaan, kurva, dan grafik</h3></li>
                <li><h3>Qanda: aplikasi yang dapat menjawab soal matematika dengan cepat dan dapat memungkinkan pengguna untuk berdiskusi langsung dengan tutor melalui chat</li>
                <li><h3>Math Trick: aplikasi yang menyediakan ratusan rumus dan trik belajar matematika</h3></li>
                <li><h3>Pahamify: aplikasi ini merupakan aplikasi les online yang dimana beberapa fitur juga bisa kita akses secara gratis dan tetap bisa membantu kita</h3></li>
            </ul>
        """ 
    elif "rekomendasi website" in user_text or "website" in user_text:
         return """
        <h3>Rekomendasi Website untuk Belajar Matematika ala Mathdy:</h3>
            <ul>
                <li><h3><a href="https://www.zenius.net/" target="_blank">Zenius</a>: website yang menyediakan video pembelajaran matematika dasar dan fundamental matematika</h3></li>
                <li><h3><a href="https://www.khanacademy.org/" target="_blank">Khan Academy</a>: website yang menyediakan materi pembelajaran matematika yang dibuat oleh pengajar dari berbagai negara</h3></li>
                <li><h3><a href="https://mathcyber1997.com/" target="_blank">Math Cyber 1997</a>: website yang menyediakan materi dan latihan soal dengan berbagai topik</h3></li>
                <li><h3><a href="https://www.m4th-lab.net/" target="_blank">m4th-lab</a>: website yang menyediakan kumpulan soal-soal tidak hanya matematika dan dibagikan secara gratis</h3></li>
            </ul>
        """ 
    elif "rekomendasi channel youtube" in user_text or "youtube" in user_text:
         return """
        <h3>Rekomendasi Channel YouTube untuk Belajar Matematika ala Mathdy:</h3>
            <ul>
                <li><h3><a href="https://www.youtube.com/@MatematikaDasar" target="_blank">Channel Matematika Dasar</a>: channel menyediakan beragam video singkat yang membahas konsep dan materi matematika dasar. Channel ini dapat membantu kamu memperkuat fondasi matematikamu!</h3></li>
                <li><h3><a href="http://www.youtube.com/@BIGCourse" target="_blank">Channel BIG Course</a>: channel yang dapat membantu kamu memahami pelajaran matematika dengana penjelasan yang rinci</h3></li>
                <li><h3><a href="http://www.youtube.com/@PrivatAlFaiz" target="_blank">Channel Prival Al Faiz</a>: channel ini dapat membantu kamu mempelajari soal-soal matematika yang diujikan dalam tes UTBK, CPNS, dll</h3></li>
                <li><h3><a href="http://www.youtube.com/@m4thlab" target="_blank">Channel m4th-lab</a>: channel ini membahas berbagai topik pelajaran matematika yang dilengkapi blog berisi kumpulan soal matematika</h3></li>
                <li><h3><a href="http://www.youtube.com/@miraclesitompul" target="_blank">Channel Miracle Sitompul</a>: channel yang membahas soal-soal matematika dengan menggunakan bahasa sehari-hari yang mudah dipahami. Selain membahas soal, channel ini juga dapat membantu kamu mempelajari kerangka pikir matematika.</h3></li
            </ul>
        """ 
    return "Maaf, aku hanya bisa membantu dengan soal matematika, tips dan bercanda!"

# Fungsi Faktorial
def solve_factorial_expression(user_text):
    try:
        # Periksa apakah input diakhiri dengan "!"
        if user_text.endswith("!"):
            # Ambil angka sebelum "!"
            number = int(user_text[:-1])  # Hapus "!" dan konversi ke integer
            if number < 0:
                return "Bilang negatif tidak memiliki faktorial."
            result = math.factorial(number)
            return f"{number}! = {result}"
        return None  # Kembalikan None jika bukan faktorial
    except ValueError:
        return "Input tidak valid untuk faktorial."


# Fungsi untuk memeriksa apakah input adalah ekspresi matematika
def is_math_expression(user_text):
    math_pattern = r'^[0-9\+\-\/%\s\(\)\.\\*sqrt!]+$'
    return re.match(math_pattern, user_text.strip()) is not None

# Fungsi untuk evaluasi ekspresi matematika
def solve_math_expression(user_text):
    if "!" in user_text:
        return solve_factorial_expression(user_text)
    try:
        user_text = user_text.replace("sqrt(", "math.sqrt(")
        result = eval(user_text)
        return str(result)
    except Exception:
        return "Error solving math expression."

# Daftar jokes
jokes_list = [
    "Kamu itu seperti konstanta Pi, tak terhingga dan selalu bikin aku terpana.",
    "Hubungan kita kayak garis paralel, selalu sejajar dan nggak akan pernah berpisah.",
    "Kalau kamu jadi variabel X, aku bakal jadi Y, biar kita selalu ada dalam persamaan yang sama.",
    "Kamu seperti akar dari -1, nggak nyata tapi selalu ada dalam pikiranku.",
    "Aku boleh nggak jadi turunanmu? Biar aku selalu mengejar perubahan kecil dalam hidupmu.",
    "Kalau kamu sudut, aku pasti 90 derajat, karena aku jatuh tegak lurus mencintaimu.",
    "Aku dan kamu bagaikan himpunan, selalu saling melengkapi dan tak terpisahkan.",
    "Kamu seperti eksponensial, semakin lama semakin membuat hati ini berdegup lebih cepat.",
    "Jangan jadi irasional, biarkan kita jadi satu pasangan sempurna.",
    "Kita itu kayak limit, semakin dekat tanpa batas, walaupun nggak pernah benar-benar bertemu.",
]

# Fungsi utama chatbot response
def chatbot_response(user_text):
    if "joke" in user_text.lower() or "jokes" in user_text.lower():
        return random.choice(jokes_list)
    elif is_math_expression(user_text):
        return solve_math_expression(user_text)
    else:
        return handle_conversation(user_text)

# Route untuk halaman utama
@app.route("/")
def main():
    return render_template("index.html")

# Route untuk halaman kedua (chat)
@app.route("/chat")
def chat():
    return render_template("chat.html")

# Route untuk mendapatkan respon chatbot
@app.route("/get")
def get_chatbot_response():
    user_message = request.args.get('userMessage')
    response = chatbot_response(user_message)
    return str(response)

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True, host='0.0.0.0', port=5000)
