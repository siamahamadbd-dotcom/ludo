from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Anas Gaming Platform</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0d0d1a; color: white; text-align: center; margin: 0; padding: 20px; }
            .header { margin-bottom: 30px; }
            .header h1 { color: #00d2ff; text-transform: uppercase; letter-spacing: 2px; }
            .balance-card { background: linear-gradient(135deg, #1e1e3f, #2b2b5e); border-radius: 15px; padding: 20px; display: inline-block; margin-bottom: 40px; border: 1px solid #444; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
            .balance-card h2 { margin: 0; font-size: 1.2rem; color: #bbb; }
            .balance-card p { font-size: 2.5rem; margin: 10px 0; color: #00ff88; font-weight: bold; }
            .arena-container { display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; }
            .card { background: #1a1a2e; border: 2px solid #333; border-radius: 20px; width: 280px; padding: 25px; transition: 0.3s; position: relative; overflow: hidden; }
            .card:hover { transform: translateY(-10px); border-color: #00d2ff; box-shadow: 0 10px 20px rgba(0,210,255,0.3); }
            .bronze { border-color: #cd7f32; }
            .gold { border-color: #ffd700; }
            .card h3 { margin-top: 0; font-size: 1.5rem; }
            .bronze h3 { color: #cd7f32; }
            .gold h3 { color: #ffd700; }
            .fee { font-size: 1.1rem; margin: 15px 0; color: #eee; }
            .btn { background: #00d2ff; color: #000; border: none; padding: 12px 30px; border-radius: 50px; font-weight: bold; cursor: pointer; text-transform: uppercase; transition: 0.3s; }
            .btn:hover { background: #00ff88; }
            footer { margin-top: 50px; color: #666; font-size: 0.9rem; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Anas Gaming Platform</h1>
        </div>

        <div class="balance-card">
            <h2>আপনার বর্তমান ব্যালেন্স</h2>
            <p>৳ ২.০০</p>
        </div>

        <div class="arena-container">
            <div class="card bronze">
                <h3>BRONZE ARENA</h3>
                <p>লুডু টুর্নামেন্ট</p>
                <div class="fee">এন্ট্রি ফি: ৳ ২০</div>
                <button class="btn">JOIN NOW</button>
            </div>

            <div class="card gold">
                <h3>GOLD ZONE</h3>
                <p>লুডু টুর্নামেন্ট</p>
                <div class="fee">এন্ট্রি ফি: ৳ ১০০</div>
                <button class="btn">JOIN NOW</button>
            </div>
        </div>

        <footer>
            <p>© ২০২৬ Anas Gaming Platform | সর্বস্বত্ব সংরক্ষিত</p>
        </footer>
    </body>
    </html>
    """
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
