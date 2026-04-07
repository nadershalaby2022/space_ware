# شرح نموذج 1 - لعبة الطيارات

## التشغيل
```bash
streamlit run app.py
```

## طريقة الاستخدام للطفل
1. افتح اللعبة وانتظر ظهور شاشة اللعب.
2. حرّك الطيارة بالأسهم:
   - أعلى: `Arrow Up`
   - أسفل: `Arrow Down`
   - يمين: `Arrow Right`
   - شمال: `Arrow Left`
3. اضرب بالصاروخ بزر `Space`.
4. كل طيارة عدو تضربها = `10` نقاط.
5. إذا خلصت الأرواح اضغط زر `إعادة اللعب`.

## وظيفة كل بلوك برمجي
- `import streamlit` و `components`: لتجهيز واجهة Streamlit وحقن لعبة HTML/JS.
- `st.set_page_config`: يضبط اسم التبويب والأيقونة.
- `st.title` و `st.write`: يطبع عنوان وتعليمات اللعب.
- `game_html`: يحتوي واجهة اللعبة (HTML + CSS + JavaScript).
- `components.html(...)`: يعرض اللعبة داخل التطبيق.
- `st.info`: يذكّر بمجلد الصور الخاص بالأطفال.

## وظيفة أهم سطور JavaScript داخل اللعبة
- `const canvas = ...`: إنشاء مساحة الرسم.
- `const audioCtx = ...`: توليد أصوات بدون ملفات خارجية.
- `function beep(...)`: تشغيل صوت إطلاق أو انفجار.
- `const player = {...}`: خصائص طيارة اللاعب.
- `let missiles = []`: تخزين الصواريخ.
- `let enemies = []`: تخزين الطيارات المعادية.
- `window.addEventListener('keydown'...)`: استقبال الأسهم و`Space`.
- `function update()`: تحديث الحركة والاصطدامات والنقاط.
- `function draw()`: رسم جميع العناصر في كل إطار.
- `requestAnimationFrame(loop)`: تكرار اللعبة بسلاسة.
- `function restartGame()`: بدء جولة جديدة.
