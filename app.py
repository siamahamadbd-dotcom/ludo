from flask import Flask, render_template_string

app = Flask(__name__)

# আপনার স্ক্রিনশটের মতো গেমিং ইন্টারফেস
GAME_LAYOUT = """
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Apon Gaming Platform</title>
    <style>
        body { font-family: Arial; background: #1a0033; color: white; margin: 0; padding-bottom: 80px; }
        .top-nav { background: #2d004d; padding: 15px; display: flex; justify-content: space-between; align-items: center; }
        .balance-chip { background: #00c853; padding: 6px 15px; border-radius: 20px; font-weight: bold; }
        .banner-card { background: linear-gradient(135deg, #6600cc, #2d004d); margin: 15px; padding: 25px; border-radius: 20px; text-align: center; }
        .play-now { background: white; color: #1a0033; border: none; padding: 12px 45px; border-radius: 30px; font-size: 18px; font-weight: bold; cursor: pointer; margin-top: 15px; }
        .table-card { background: #2d004d; margin: 10px 15px; padding: 18px; border-radius: 15px; display: flex; justify-content: space-between; align-items: center; border-left: 6px solid #ff00ff; }
        .prize-tag { color: #00ff00; font-weight: bold; font-size: 18px; }
        .entry-fee { background: white; color: black; border: none; padding: 8px 20px; border-radius: 10px; font-weight: bold; }
        .bottom-nav { position: fixed; bottom: 0; width: 100%; background: #2d004d; display: flex; justify-content: space-around; padding: 12px 0; border-top: 1px solid #3d007a; }
        .nav-link { color: #b366ff; text-decoration: none; font-size: 12px; text-align: center; }
        .active { color: white; }
    </style>
</head>
<body>
    <div class="top-nav">
        <div><b>Aponbai1</b><br><small style="color:gold;">Profile ▶</small></div>
        <div class="balance-chip">৳ ২.০০ +</div>
    </div>

    <div class="banner-card">
        <img src="https://i.ibb.co/VWVm0Rz/ludo-icon.png" width="90"><br>
        <button class="play-now">PLAY NOW</button>
    </div>

    <div style="padding: 0 15px;">
        <h3 style="color:#b366ff;">🏆 স্পিড লুডু টুর্নামেন্ট</h3>
        
        <div class="table-card">
            <div><b>Bronze Arena</b><br><small>সময়: ৫ মিনিট</small></div>
            <div class="prize-tag">৳ ৫০.০</div>
            <button class="entry-fee">৳ ২৮.০</button>
        </div>

        <div class="table-card" style="border-left-color: gold;">
            <div><b>Gold Zone</b><br><small>সময়: ৫ মিনিট</small></div>
            <div class="prize-tag">৳ ২২৫.০</div>
            <button class="entry-fee">৳ ১২৫.০</button>
        </div>
    </div>

    <div class="bottom-nav">
        <a href="/" class="nav-link active">🏠<br>Home</a>
        <a href="#" class="nav-link">💰<br>Add Cash</a>
        <a href="#" class="nav-link">📢<br>Refer</a>
        <a href="#" class="nav-link">💳<br>Wallet</a>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(GAME_LAYOUT)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
