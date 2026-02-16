from flask import Flask, render_template_string

app = Flask(__name__)

# আপনার গেমিং ইন্টারফেসের ডিজাইন
GAME_LAYOUT = """
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Apon Gaming Platform</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #2c003e; color: white; margin: 0; padding: 0; text-align: center; }
        .top-nav { background: #4b0082; padding: 15px; display: flex; justify-content: space-between; align-items: center; }
        .balance { background: #ffcc00; color: black; padding: 5px 15px; border-radius: 20px; font-weight: bold; }
        .container { padding: 20px; }
        .card { background: #3d0066; border-radius: 15px; padding: 20px; margin-bottom: 20px; border: 1px solid #5e0099; }
        .btn-join { background: #00c853; color: white; border: none; padding: 10px 25px; border-radius: 5px; font-size: 16px; cursor: pointer; }
        .footer-nav { position: fixed; bottom: 0; width: 100%; background: #1a0029; display: flex; justify-content: space-around; padding: 10px 0; border-top: 2px solid #4b0082; }
        .nav-item { color: #b39ddb; text-decoration: none; font-size: 12px; }
    </style>
</head>
<body>
    <div class="top-nav">
        <span>Apon Gaming</span>
        <div class="balance">৳ ২.০০</div>
    </div>

    <div class="container">
        <h2>স্পিড লুডু টুর্নামেন্ট</h2>
        
        <div class="card">
            <h3>Bronze Arena</h3>
            <p>এন্ট্রি ফি: ৳ ২৮ | প্রাইজ: ৳ ৫০</p>
            <button class="btn-join">জয়েন করুন</button>
        </div>

        <div class="card">
            <h3>Gold Zone</h3>
            <p>এন্ট্রি ফি: ৳ ১২৫ | প্রাইজ: ৳ ২২৫</p>
            <button class="btn-join">জয়েন করুন</button>
        </div>
    </div>

    <div class="footer-nav">
        <a href="#" class="nav-item">🏠 হোম</a>
        <a href="#" class="nav-item">🏆 টুর্নামেন্ট</a>
        <a href="#" class="nav-item">💰 ওয়ালেট</a>
        <a href="#" class="nav-item">👤 প্রোফাইল</a>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(GAME_LAYOUT)

if __name__ == '__main__':
    app.run(debug=True)
