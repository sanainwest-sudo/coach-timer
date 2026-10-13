# Архитектура

```
app/
  index.html     — весь интерфейс и логика
  audio/         — stop.mp3, ready.mp3, letsgo.mp3 (исходники голосов)
  voices.js      — те же голоса в base64 (их и использует index.html, работает даже как файл)
tools/
  make_voices.py — генерация голосовых файлов
```

Звук: `<audio id=music>` → MediaElementSource → musicGain → destination.
Команды: fetch → decodeAudioData → BufferSource → destination (поверх музыки).
Плейлист: IndexedDB `coachTimer` → store `tracks` {id, name, blob}; при загрузке → object URL.
Языки: словарь L = {kk, en} в index.html, элементы с data-t / data-t-aria, applyLang() перерисовывает всё; S.lang в localStorage.
Сигналы: cue(событие) → CUES.voice (голос из voices.js) или CUES.gong (bell()/clap(), синтез).
Таймер: хранит время окончания фазы (`phaseEnd`), проверка каждые 250 мс + на событии `timeupdate` музыки.
