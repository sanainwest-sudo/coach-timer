# Архитектура

```
app/
  index.html     — весь интерфейс и логика
  audio/         — stop.mp3, ready.mp3, letsgo.mp3
tools/
  make_voices.py — генерация голосовых файлов
```

Звук: `<audio id=music>` → MediaElementSource → musicGain → destination.
Команды: fetch → decodeAudioData → BufferSource → destination (поверх музыки).
Таймер: хранит время окончания фазы (`phaseEnd`), проверка каждые 250 мс + на событии `timeupdate` музыки.
