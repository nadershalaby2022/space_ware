# شرح تفصيلي سطر بسطر - app.py

## الهدف من الملف
- هذا الملف هو التطبيق الرئيسي للنموذج ويحتوي على منطق التشغيل والواجهة.

## شرح البلوكات الرئيسية
- استيراد المكتبات الأساسية.
- إعداد واجهة التطبيق وعرض البيانات.
- منطق الحسابات/الاصطدامات/التحليل حسب النموذج.
- عرض النتائج للمستخدم.

## شرح كل سطر برمجي
- السطر 1: `﻿# استيراد مكتبة Streamlit لبناء واجهة الويب بسرعة.`
  السبب/الوظيفة: سطر تنفيذي ضمن منطق التطبيق.
- السطر 2: `import streamlit as st`
  السبب/الوظيفة: استيراد مكتبة/وحدة مطلوبة في التطبيق.
- السطر 3: `# استيراد مكوّن HTML لعرض لعبة JavaScript داخل الصفحة.`
  السبب/الوظيفة: تعليق توضيحي للمطور.
- السطر 4: `import streamlit.components.v1 as components`
  السبب/الوظيفة: استيراد مكتبة/وحدة مطلوبة في التطبيق.
- السطر 5: `from pathlib import Path`
  السبب/الوظيفة: استيراد مكتبة/وحدة مطلوبة في التطبيق.
- السطر 6: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 7: `# ضبط عنوان الصفحة الذي يظهر في التبويب.`
  السبب/الوظيفة: تعليق توضيحي للمطور.
- السطر 8: `st.set_page_config(page_title="Plane Battle - Kids", page_icon="✈️", layout="wide")`
  السبب/الوظيفة: سطر يتعامل مع واجهة Streamlit وعرض البيانات.
- السطر 9: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 10: `# عنوان رئيسي للتطبيق.`
  السبب/الوظيفة: تعليق توضيحي للمطور.
- السطر 11: `st.title("✈️ لعبة حرب الطيارات - نموذج بسيط")`
  السبب/الوظيفة: سطر يتعامل مع واجهة Streamlit وعرض البيانات.
- السطر 12: `# شرح سريع لطريقة اللعب.`
  السبب/الوظيفة: تعليق توضيحي للمطور.
- السطر 13: `st.write("استخدم الأسهم للتحريك، ومسافة Space لإطلاق الصاروخ.")`
  السبب/الوظيفة: سطر يتعامل مع واجهة Streamlit وعرض البيانات.
- السطر 14: `st.markdown(`
  السبب/الوظيفة: سطر يتعامل مع واجهة Streamlit وعرض البيانات.
- السطر 15: `    """`
  السبب/الوظيفة: سطر تنفيذي ضمن منطق التطبيق.
- السطر 16: `### طريقة اللعب السريعة`
  السبب/الوظيفة: تعليق توضيحي للمطور.
- السطر 17: `- التحريك: 'Arrow Up' 'Arrow Down' 'Arrow Left' 'Arrow Right'`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 18: `- الضرب بالصاروخ: زر 'Space'`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 19: `- الهدف: اضرب الطيارات اللي جاية من اليمين.`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 20: `- كل ضربة صحيحة = 10 نقاط.`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 21: `- عند انتهاء الأرواح اضغط 'إعادة اللعب'.`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 22: `"""`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 23: `)`
  السبب/الوظيفة: سطر تنفيذي ضمن منطق التطبيق.
- السطر 24: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 25: `# قراءة صور الأطفال من مجلد images وعرضها داخل الشاشة.`
  السبب/الوظيفة: تعليق توضيحي للمطور.
- السطر 26: `images_dir = Path(__file__).parent / "images"`
  السبب/الوظيفة: إسناد قيمة لمتغير لاستخدامها لاحقاً.
- السطر 27: `local_images = sorted([p for p in images_dir.glob("*") if p.suffix.lower() in [".png", ".jpg", ".jpeg", ".webp"]])`
  السبب/الوظيفة: إسناد قيمة لمتغير لاستخدامها لاحقاً.
- السطر 28: `if local_images:`
  السبب/الوظيفة: شرط منطقي لتنفيذ كود عند تحقق الحالة.
- السطر 29: `    selected_name = st.selectbox("اختار صورة الطفل من مجلد images", [p.name for p in local_images])`
  السبب/الوظيفة: سطر يتعامل مع واجهة Streamlit وعرض البيانات.
- السطر 30: `    st.image(str(images_dir / selected_name), caption=f"صورة الطفل: {selected_name}", width=220)`
  السبب/الوظيفة: سطر يتعامل مع واجهة Streamlit وعرض البيانات.
- السطر 31: `else:`
  السبب/الوظيفة: شرط منطقي لتنفيذ كود عند تحقق الحالة.
- السطر 32: `    st.warning("لا توجد صور داخل 01_plane_battle/images")`
  السبب/الوظيفة: سطر يتعامل مع واجهة Streamlit وعرض البيانات.
- السطر 33: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 34: `# HTML + CSS + JavaScript للعبة كاملة داخل Canvas.`
  السبب/الوظيفة: تعليق توضيحي للمطور.
- السطر 35: `# الكود التالي مصمم بسيطًا ليكون مناسبًا للتعليم للأطفال.`
  السبب/الوظيفة: تعليق توضيحي للمطور.
- السطر 36: `game_html = """`
  السبب/الوظيفة: إسناد قيمة لمتغير لاستخدامها لاحقاً.
- السطر 37: `<!DOCTYPE html>`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 38: `<html>`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 39: `<head>`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 40: `  <meta charset='UTF-8' />`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 41: `  <style>`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 42: `    body {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 43: `      margin: 0;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 44: `      background: radial-gradient(circle at top, #0f2d56, #050915 70%);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 45: `      color: white;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 46: `      font-family: 'Trebuchet MS', sans-serif;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 47: `      overflow: hidden;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 48: `    }`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 49: `    .hud {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 50: `      position: absolute;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 51: `      top: 8px;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 52: `      left: 10px;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 53: `      z-index: 10;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 54: `      font-size: 18px;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 55: `      background: rgba(0, 0, 0, 0.3);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 56: `      padding: 6px 10px;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 57: `      border-radius: 10px;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 58: `    }`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 59: `    .game-over {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 60: `      position: absolute;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 61: `      inset: 0;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 62: `      display: none;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 63: `      align-items: center;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 64: `      justify-content: center;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 65: `      flex-direction: column;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 66: `      font-size: 32px;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 67: `      background: rgba(0, 0, 0, 0.55);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 68: `      z-index: 20;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 69: `      text-align: center;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 70: `    }`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 71: `    button {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 72: `      margin-top: 12px;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 73: `      padding: 10px 14px;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 74: `      border: none;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 75: `      border-radius: 8px;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 76: `      background: #ffbf3c;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 77: `      cursor: pointer;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 78: `      font-weight: bold;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 79: `    }`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 80: `    canvas {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 81: `      display: block;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 82: `      margin: 0 auto;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 83: `      border: 2px solid rgba(255, 255, 255, 0.25);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 84: `      border-radius: 14px;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 85: `      box-shadow: 0 12px 35px rgba(0, 0, 0, 0.4);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 86: `      margin-top: 12px;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 87: `    }`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 88: `  </style>`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 89: `</head>`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 90: `<body>`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 91: `  <div class='hud'>النقاط: <span id='score'>0</span> | الأرواح: <span id='lives'>3</span></div>`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 92: `  <canvas id='game' width='960' height='540'></canvas>`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 93: `  <div class='game-over' id='gameOver'>`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 94: `    <div>انتهت اللعبة</div>`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 95: `    <div style='font-size:22px;margin-top:8px;'>نتيجتك: <span id='finalScore'>0</span></div>`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 96: `    <button onclick='restartGame()'>إعادة اللعب</button>`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 97: `  </div>`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 98: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 99: `<script>`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 100: `  const canvas = document.getElementById('game');`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 101: `  const ctx = canvas.getContext('2d');`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 102: `  const scoreEl = document.getElementById('score');`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 103: `  const livesEl = document.getElementById('lives');`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 104: `  const gameOverEl = document.getElementById('gameOver');`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 105: `  const finalScoreEl = document.getElementById('finalScore');`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 106: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 107: `  const audioCtx = new (window.AudioContext || window.webkitAudioContext)();`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 108: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 109: `  function beep(freq, duration, type='square', gain=0.04) {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 110: `    const osc = audioCtx.createOscillator();`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 111: `    const g = audioCtx.createGain();`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 112: `    osc.type = type;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 113: `    osc.frequency.value = freq;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 114: `    g.gain.value = gain;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 115: `    osc.connect(g);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 116: `    g.connect(audioCtx.destination);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 117: `    osc.start();`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 118: `    osc.stop(audioCtx.currentTime + duration);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 119: `  }`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 120: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 121: `  const player = { x: 90, y: 260, w: 65, h: 34, speed: 7 };`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 122: `  let missiles = [];`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 123: `  let enemies = [];`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 124: `  let explosions = [];`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 125: `  const keys = {};`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 126: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 127: `  let score = 0;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 128: `  let lives = 3;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 129: `  let frame = 0;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 130: `  let gameOver = false;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 131: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 132: `  window.addEventListener('keydown', (e) => {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 133: `    keys[e.code] = true;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 134: `    if (e.code === 'Space' && !gameOver) {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 135: `      missiles.push({ x: player.x + player.w - 3, y: player.y + player.h / 2 - 2, w: 14, h: 4, speed: 12 });`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 136: `      beep(550, 0.07, 'sawtooth', 0.03);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 137: `    }`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 138: `    audioCtx.resume();`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 139: `  });`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 140: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 141: `  window.addEventListener('keyup', (e) => {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 142: `    keys[e.code] = false;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 143: `  });`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 144: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 145: `  function drawStars() {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 146: `    for (let i = 0; i < 60; i++) {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 147: `      const x = (i * 131 + frame * 2) % canvas.width;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 148: `      const y = (i * 79) % canvas.height;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 149: `      ctx.fillStyle = 'rgba(255,255,255,0.5)';`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 150: `      ctx.fillRect(canvas.width - x, y, 2, 2);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 151: `    }`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 152: `  }`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 153: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 154: `  function drawPlayer() {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 155: `    ctx.fillStyle = '#53d8fb';`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 156: `    ctx.beginPath();`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 157: `    ctx.moveTo(player.x, player.y + player.h / 2);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 158: `    ctx.lineTo(player.x + player.w - 10, player.y);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 159: `    ctx.lineTo(player.x + player.w, player.y + player.h / 2);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 160: `    ctx.lineTo(player.x + player.w - 10, player.y + player.h);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 161: `    ctx.closePath();`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 162: `    ctx.fill();`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 163: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 164: `    ctx.fillStyle = '#ffb703';`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 165: `    ctx.fillRect(player.x - 10, player.y + 12, 10, 10);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 166: `  }`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 167: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 168: `  function drawMissiles() {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 169: `    ctx.fillStyle = '#ffd166';`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 170: `    missiles.forEach((m) => {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 171: `      ctx.fillRect(m.x, m.y, m.w, m.h);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 172: `    });`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 173: `  }`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 174: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 175: `  function drawEnemies() {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 176: `    enemies.forEach((e) => {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 177: `      ctx.fillStyle = '#ff5c8a';`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 178: `      ctx.fillRect(e.x, e.y, e.w, e.h);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 179: `      ctx.fillStyle = '#ffd6e0';`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 180: `      ctx.fillRect(e.x + 6, e.y + 8, 12, 4);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 181: `    });`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 182: `  }`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 183: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 184: `  function drawExplosions() {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 185: `    explosions.forEach((ex) => {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 186: `      ctx.beginPath();`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 187: `      ctx.arc(ex.x, ex.y, ex.r, 0, Math.PI * 2);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 188: `      ctx.fillStyle = 'rgba(255, ${Math.max(80, 220 - ex.r * 18)}, 30, 0.8)';`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 189: `      ctx.fill();`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 190: `      ex.r += 1.7;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 191: `    });`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 192: `    explosions = explosions.filter((ex) => ex.r < 20);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 193: `  }`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 194: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 195: `  function hit(a, b) {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 196: `    return a.x < b.x + b.w && a.x + a.w > b.x && a.y < b.y + b.h && a.y + a.h > b.y;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 197: `  }`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 198: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 199: `  function update() {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 200: `    if (gameOver) return;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 201: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 202: `    if (keys['ArrowUp']) player.y -= player.speed;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 203: `    if (keys['ArrowDown']) player.y += player.speed;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 204: `    if (keys['ArrowLeft']) player.x -= player.speed;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 205: `    if (keys['ArrowRight']) player.x += player.speed;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 206: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 207: `    player.x = Math.max(0, Math.min(canvas.width - player.w, player.x));`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 208: `    player.y = Math.max(0, Math.min(canvas.height - player.h, player.y));`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 209: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 210: `    missiles.forEach((m) => m.x += m.speed);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 211: `    missiles = missiles.filter((m) => m.x < canvas.width + 30);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 212: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 213: `    if (frame % 45 === 0) {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 214: `      const h = 28 + Math.random() * 20;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 215: `      enemies.push({ x: canvas.width + 20, y: Math.random() * (canvas.height - h), w: 44, h: h, speed: 3 + Math.random() * 2 });`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 216: `    }`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 217: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 218: `    enemies.forEach((e) => e.x -= e.speed);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 219: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 220: `    enemies = enemies.filter((e) => {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 221: `      if (e.x + e.w < 0) {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 222: `        lives -= 1;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 223: `        beep(180, 0.15, 'triangle', 0.05);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 224: `        return false;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 225: `      }`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 226: `      return true;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 227: `    });`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 228: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 229: `    for (let i = missiles.length - 1; i >= 0; i--) {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 230: `      for (let j = enemies.length - 1; j >= 0; j--) {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 231: `        if (hit(missiles[i], enemies[j])) {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 232: `          explosions.push({ x: enemies[j].x + enemies[j].w / 2, y: enemies[j].y + enemies[j].h / 2, r: 4 });`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 233: `          score += 10;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 234: `          missiles.splice(i, 1);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 235: `          enemies.splice(j, 1);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 236: `          beep(90, 0.09, 'sawtooth', 0.06);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 237: `          break;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 238: `        }`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 239: `      }`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 240: `    }`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 241: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 242: `    for (let j = enemies.length - 1; j >= 0; j--) {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 243: `      if (hit(player, enemies[j])) {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 244: `        explosions.push({ x: player.x + player.w / 2, y: player.y + player.h / 2, r: 6 });`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 245: `        enemies.splice(j, 1);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 246: `        lives -= 1;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 247: `        beep(120, 0.12, 'square', 0.06);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 248: `      }`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 249: `    }`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 250: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 251: `    scoreEl.textContent = score;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 252: `    livesEl.textContent = lives;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 253: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 254: `    if (lives <= 0) {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 255: `      gameOver = true;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 256: `      finalScoreEl.textContent = score;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 257: `      gameOverEl.style.display = 'flex';`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 258: `    }`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 259: `  }`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 260: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 261: `  function draw() {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 262: `    ctx.clearRect(0, 0, canvas.width, canvas.height);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 263: `    drawStars();`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 264: `    drawPlayer();`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 265: `    drawMissiles();`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 266: `    drawEnemies();`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 267: `    drawExplosions();`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 268: `  }`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 269: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 270: `  function loop() {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 271: `    frame++;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 272: `    update();`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 273: `    draw();`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 274: `    requestAnimationFrame(loop);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 275: `  }`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 276: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 277: `  function restartGame() {`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 278: `    player.x = 90;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 279: `    player.y = 260;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 280: `    missiles = [];`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 281: `    enemies = [];`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 282: `    explosions = [];`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 283: `    score = 0;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 284: `    lives = 3;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 285: `    frame = 0;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 286: `    gameOver = false;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 287: `    scoreEl.textContent = score;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 288: `    livesEl.textContent = lives;`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 289: `    gameOverEl.style.display = 'none';`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 290: `    beep(700, 0.06, 'triangle', 0.04);`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 291: `  }`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 292: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 293: `  loop();`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 294: `</script>`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 295: `</body>`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 296: `</html>`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 297: `"""`
  السبب/الوظيفة: سطر ضمن قالب HTML/CSS/JavaScript لواجهة تفاعلية.
- السطر 298: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 299: `# عرض اللعبة داخل Streamlit.`
  السبب/الوظيفة: تعليق توضيحي للمطور.
- السطر 300: `components.html(game_html, height=620, scrolling=False)`
  السبب/الوظيفة: سطر يتعامل مع واجهة Streamlit وعرض البيانات.
- السطر 301: ``
  السبب/الوظيفة: سطر فارغ لتنظيم الكود.
- السطر 302: `# ملاحظة تعليمية تحت اللعبة.`
  السبب/الوظيفة: تعليق توضيحي للمطور.
- السطر 303: `st.info("مجلد الصور لهذا النموذج: 01_plane_battle/images")`
  السبب/الوظيفة: سطر يتعامل مع واجهة Streamlit وعرض البيانات.

## ملاحظات للشرح مع الأطفال
- ابدأ بالواجهة أولاً ثم انتقل لمنطق الكود.
- غيّر قيمة بسيطة (لون/سرعة/نص) واشرح الفرق.
- اربط بين كل مدخل في الواجهة والنتيجة الظاهرة.