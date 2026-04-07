# استيراد مكتبة Streamlit لبناء واجهة الويب بسرعة.
import streamlit as st
# استيراد مكوّن HTML لعرض لعبة JavaScript داخل الصفحة.
import streamlit.components.v1 as components
from pathlib import Path

# ضبط عنوان الصفحة الذي يظهر في التبويب.
st.set_page_config(page_title="Plane Battle - Kids", page_icon="✈️", layout="wide")

# عنوان رئيسي للتطبيق.
st.title("✈️ لعبة حرب الطيارات - نموذج بسيط")
# شرح سريع لطريقة اللعب.
st.write("استخدم الأسهم للتحريك، ومسافة Space لإطلاق الصاروخ.")
st.markdown(
    """
### طريقة اللعب السريعة
- التحريك: `Arrow Up` `Arrow Down` `Arrow Left` `Arrow Right`
- الضرب بالصاروخ: زر `Space`
- الهدف: اضرب الطيارات اللي جاية من اليمين.
- كل ضربة صحيحة = 10 نقاط.
- عند انتهاء الأرواح اضغط `إعادة اللعب`.
"""
)

# قراءة صور الأطفال من مجلد images وعرضها داخل الشاشة.
images_dir = Path(__file__).parent / "images"
local_images = sorted([p for p in images_dir.glob("*") if p.suffix.lower() in [".png", ".jpg", ".jpeg", ".webp"]])
if local_images:
    selected_name = st.selectbox("اختار صورة الطفل من مجلد images", [p.name for p in local_images])
    st.image(str(images_dir / selected_name), caption=f"صورة الطفل: {selected_name}", width=220)
else:
    st.warning("لا توجد صور داخل 01_plane_battle/images")

# HTML + CSS + JavaScript للعبة كاملة داخل Canvas.
# الكود التالي مصمم بسيطًا ليكون مناسبًا للتعليم للأطفال.
game_html = """
<!DOCTYPE html>
<html>
<head>
  <meta charset='UTF-8' />
  <style>
    body {
      margin: 0;
      background: radial-gradient(circle at top, #0f2d56, #050915 70%);
      color: white;
      font-family: 'Trebuchet MS', sans-serif;
      overflow: hidden;
    }
    .hud {
      position: absolute;
      top: 8px;
      left: 10px;
      z-index: 10;
      font-size: 18px;
      background: rgba(0, 0, 0, 0.3);
      padding: 6px 10px;
      border-radius: 10px;
    }
    .game-over {
      position: absolute;
      inset: 0;
      display: none;
      align-items: center;
      justify-content: center;
      flex-direction: column;
      font-size: 32px;
      background: rgba(0, 0, 0, 0.55);
      z-index: 20;
      text-align: center;
    }
    button {
      margin-top: 12px;
      padding: 10px 14px;
      border: none;
      border-radius: 8px;
      background: #ffbf3c;
      cursor: pointer;
      font-weight: bold;
    }
    canvas {
      display: block;
      margin: 0 auto;
      border: 2px solid rgba(255, 255, 255, 0.25);
      border-radius: 14px;
      box-shadow: 0 12px 35px rgba(0, 0, 0, 0.4);
      margin-top: 12px;
    }
  </style>
</head>
<body>
  <div class='hud'>النقاط: <span id='score'>0</span> | الأرواح: <span id='lives'>3</span></div>
  <canvas id='game' width='960' height='540'></canvas>
  <div class='game-over' id='gameOver'>
    <div>انتهت اللعبة</div>
    <div style='font-size:22px;margin-top:8px;'>نتيجتك: <span id='finalScore'>0</span></div>
    <button onclick='restartGame()'>إعادة اللعب</button>
  </div>

<script>
  const canvas = document.getElementById('game');
  const ctx = canvas.getContext('2d');
  const scoreEl = document.getElementById('score');
  const livesEl = document.getElementById('lives');
  const gameOverEl = document.getElementById('gameOver');
  const finalScoreEl = document.getElementById('finalScore');

  const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

  function beep(freq, duration, type='square', gain=0.04) {
    const osc = audioCtx.createOscillator();
    const g = audioCtx.createGain();
    osc.type = type;
    osc.frequency.value = freq;
    g.gain.value = gain;
    osc.connect(g);
    g.connect(audioCtx.destination);
    osc.start();
    osc.stop(audioCtx.currentTime + duration);
  }

  const player = { x: 90, y: 260, w: 65, h: 34, speed: 7 };
  let missiles = [];
  let enemies = [];
  let explosions = [];
  const keys = {};

  let score = 0;
  let lives = 3;
  let frame = 0;
  let gameOver = false;

  window.addEventListener('keydown', (e) => {
    keys[e.code] = true;
    if (e.code === 'Space' && !gameOver) {
      missiles.push({ x: player.x + player.w - 3, y: player.y + player.h / 2 - 2, w: 14, h: 4, speed: 12 });
      beep(550, 0.07, 'sawtooth', 0.03);
    }
    audioCtx.resume();
  });

  window.addEventListener('keyup', (e) => {
    keys[e.code] = false;
  });

  function drawStars() {
    for (let i = 0; i < 60; i++) {
      const x = (i * 131 + frame * 2) % canvas.width;
      const y = (i * 79) % canvas.height;
      ctx.fillStyle = 'rgba(255,255,255,0.5)';
      ctx.fillRect(canvas.width - x, y, 2, 2);
    }
  }

  function drawPlayer() {
    ctx.fillStyle = '#53d8fb';
    ctx.beginPath();
    ctx.moveTo(player.x, player.y + player.h / 2);
    ctx.lineTo(player.x + player.w - 10, player.y);
    ctx.lineTo(player.x + player.w, player.y + player.h / 2);
    ctx.lineTo(player.x + player.w - 10, player.y + player.h);
    ctx.closePath();
    ctx.fill();

    ctx.fillStyle = '#ffb703';
    ctx.fillRect(player.x - 10, player.y + 12, 10, 10);
  }

  function drawMissiles() {
    ctx.fillStyle = '#ffd166';
    missiles.forEach((m) => {
      ctx.fillRect(m.x, m.y, m.w, m.h);
    });
  }

  function drawEnemies() {
    enemies.forEach((e) => {
      ctx.fillStyle = '#ff5c8a';
      ctx.fillRect(e.x, e.y, e.w, e.h);
      ctx.fillStyle = '#ffd6e0';
      ctx.fillRect(e.x + 6, e.y + 8, 12, 4);
    });
  }

  function drawExplosions() {
    explosions.forEach((ex) => {
      ctx.beginPath();
      ctx.arc(ex.x, ex.y, ex.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(255, ${Math.max(80, 220 - ex.r * 18)}, 30, 0.8)`;
      ctx.fill();
      ex.r += 1.7;
    });
    explosions = explosions.filter((ex) => ex.r < 20);
  }

  function hit(a, b) {
    return a.x < b.x + b.w && a.x + a.w > b.x && a.y < b.y + b.h && a.y + a.h > b.y;
  }

  function update() {
    if (gameOver) return;

    if (keys['ArrowUp']) player.y -= player.speed;
    if (keys['ArrowDown']) player.y += player.speed;
    if (keys['ArrowLeft']) player.x -= player.speed;
    if (keys['ArrowRight']) player.x += player.speed;

    player.x = Math.max(0, Math.min(canvas.width - player.w, player.x));
    player.y = Math.max(0, Math.min(canvas.height - player.h, player.y));

    missiles.forEach((m) => m.x += m.speed);
    missiles = missiles.filter((m) => m.x < canvas.width + 30);

    if (frame % 45 === 0) {
      const h = 28 + Math.random() * 20;
      enemies.push({ x: canvas.width + 20, y: Math.random() * (canvas.height - h), w: 44, h: h, speed: 3 + Math.random() * 2 });
    }

    enemies.forEach((e) => e.x -= e.speed);

    enemies = enemies.filter((e) => {
      if (e.x + e.w < 0) {
        lives -= 1;
        beep(180, 0.15, 'triangle', 0.05);
        return false;
      }
      return true;
    });

    for (let i = missiles.length - 1; i >= 0; i--) {
      for (let j = enemies.length - 1; j >= 0; j--) {
        if (hit(missiles[i], enemies[j])) {
          explosions.push({ x: enemies[j].x + enemies[j].w / 2, y: enemies[j].y + enemies[j].h / 2, r: 4 });
          score += 10;
          missiles.splice(i, 1);
          enemies.splice(j, 1);
          beep(90, 0.09, 'sawtooth', 0.06);
          break;
        }
      }
    }

    for (let j = enemies.length - 1; j >= 0; j--) {
      if (hit(player, enemies[j])) {
        explosions.push({ x: player.x + player.w / 2, y: player.y + player.h / 2, r: 6 });
        enemies.splice(j, 1);
        lives -= 1;
        beep(120, 0.12, 'square', 0.06);
      }
    }

    scoreEl.textContent = score;
    livesEl.textContent = lives;

    if (lives <= 0) {
      gameOver = true;
      finalScoreEl.textContent = score;
      gameOverEl.style.display = 'flex';
    }
  }

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawStars();
    drawPlayer();
    drawMissiles();
    drawEnemies();
    drawExplosions();
  }

  function loop() {
    frame++;
    update();
    draw();
    requestAnimationFrame(loop);
  }

  function restartGame() {
    player.x = 90;
    player.y = 260;
    missiles = [];
    enemies = [];
    explosions = [];
    score = 0;
    lives = 3;
    frame = 0;
    gameOver = false;
    scoreEl.textContent = score;
    livesEl.textContent = lives;
    gameOverEl.style.display = 'none';
    beep(700, 0.06, 'triangle', 0.04);
  }

  loop();
</script>
</body>
</html>
"""

# عرض اللعبة داخل Streamlit.
components.html(game_html, height=620, scrolling=False)

# ملاحظة تعليمية تحت اللعبة.
st.info("مجلد الصور لهذا النموذج: 01_plane_battle/images")
