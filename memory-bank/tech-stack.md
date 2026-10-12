# Стек

- Один HTML-файл `app/index.html` (HTML + CSS + JS), без фреймворков и сборки.
- Web Audio API: музыка `<audio>` → GainNode (громкость/приглушение), голосовые команды — AudioBuffer в том же AudioContext. Так звук и команды идут и при выключенном экране.
- Screen Wake Lock API — опция «не гасить экран».
- Media Session API — управление с экрана блокировки.
- Голоса: сгенерированы Microsoft Edge TTS (python `edge-tts`, голос en-US neural), MP3 в `app/audio/`.
- Хостинг: нужен HTTPS (Wake Lock, установка на главный экран). План — GitHub Pages (только с разрешения Романа).
