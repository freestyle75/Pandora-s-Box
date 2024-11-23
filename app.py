from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

crosshair_database = {
    "free$tyle": "CSGO-FPDob-Onu7p-QCOsN-X0ty5-sTqhH",
    "s1mple": "CSGO-m2Yew-4oLYL-XrYD2-idTCT-meapG",
    "xantares": "CSGO-xbpe2-E24RJ-YXNuO-pQvt8-ppNAK",
    "donk": "CSGO-t6h2T-UZ2KR-ODLXc-sh8PF-pEUSH",
    "mONESY": "CSGO-s5Qbj-nvF89-cJjDd-mRdSG-5Yt4N",
    "niko": "CSGO-jZEM9-7LFM5-VEqXb-Gh73i-3oAQL",
    "ropz": "CSGO-MMQuh-Hs3Sj-Qv9zd-VaCmc-3QqNO",
    "karrigan": "CSGO-b7bY7-KyoTu-Lkf7W-rNQqd-m7VeL",
    "frozen": "CSGO-CVN3f-b405k-5m9LT-45v9z-ZO88F",
    "wonderful": "CSGO-24iAH-MrEyK-YGpap-q2TkS-vFmDA",
    "Twistzz": "CSGO-zWRiZ-W5HP2-N4e2z-AVQTL-kj74E",
    "jL": "CSGO-9nZqk-V38NE-bcR4d-B52Vo-Mv5qB",
    "kennys": "CSGO-Z6Hz8-HYoHS-ZQHKA-yeeeE-WBjLJ",
    "b1t": "CSGO-74q7o-bvpfG-mvA6s-6bAtd-OnMHA",
    "Zywoo": "CSGO-BxYA4-u8xrB-voGTj-t6Jyr-ruWPA",
    "Scream": "CSGO-tQzxf-sRm6S-UyM7p-dJTsO-d4iz0",
    "cadiaN": "CSGO-Wji2E-fZG8e-CAq8z-fVZOm-9R88F",
    "GeT_RiGhT": "CSGO-qy3Kw-bB5Ta-28yx7-TyHDp-970tQ",
    "fOrest": "CSGO-sWkRt-oGCxB-WVY6J-bJTun-CPLoD",
    "olofmeister": "CSGO-oucDm-ooWYL-6TAv7-ufwU8-oSqNO",
    "shroud": "CSGO-kWDAF-wz6wP-NwxWZ-iPXzS-F6XDJ",
    "Lobanjica": "CSGO-mTDFx-GjdWu-hC7XY-UQ6uu-OESZQ",
    "sh1ro": "CSGO-eRYWm-Fdw6c-eTj9v-TfUdf-9ApEM",
    "electronic": "CSGO-hyGTZ-LuE7X-wAmdJ-D5wt3-9DmDA",
    "FalleN": "CSGO-AXZCv-AS25R-ZVnXz-o5cBX-wHH8D",
    "EliGE": "CSGO-rKc4z-te705-rS5zZ-5kZye-BQQhG",
    "dupreeh": "CSGO-tssX4-u2fwE-VX345-X2TmU-YF5RG"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/password-generator')
def password_generator():
    return render_template('password_generator.html')

@app.route('/generate-password', methods=['POST'])
def generate_password():
    length = int(request.form['length'])
    include_special = 'include_special' in request.form
    password = generate_random_password(length, include_special)
    return render_template('password_generator.html', password=password)

def generate_random_password(length, include_special):
    import random
    import string

    characters = string.ascii_letters + string.digits
    if include_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/snake-game')
def snake_game():
    return render_template('snake.html')

@app.route('/crosshair-app')
def crosshair_app():
    return render_template('crosshair_app.html')

@app.route('/crosshair-result', methods=['POST'])
def crosshair_result():
    nickname = request.form['nickname']
    crosshair_code = crosshair_database.get(nickname)
    return render_template('crosshair_result.html', nickname=nickname, crosshair_code=crosshair_code)

@app.route('/update-crosshair', methods=['POST'])
def update_crosshair():
    nickname = request.form['nickname']
    crosshair_code = request.form['crosshair_code']
    crosshair_database[nickname] = crosshair_code
    return redirect(url_for('crosshair_app'))

if __name__ == '__main__':
    app.run(debug=True)
