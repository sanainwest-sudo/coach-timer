"""Генерирует голосовые команды в app/audio/ через Microsoft Edge TTS.
Запуск: python tools/make_voices.py  (нужен pip install edge-tts)
"""
import asyncio
import base64
from pathlib import Path

import edge_tts

VOICE = "en-US-GuyNeural"
OUT = Path(__file__).resolve().parent.parent / "app" / "audio"

PHRASES = {
    "stop": ("Stop!", "+10%", "+0Hz"),
    "ready": ("Are you ready?", "+0%", "+0Hz"),
    "letsgo": ("Let's go!", "+10%", "+0Hz"),
}


async def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, (text, rate, pitch) in PHRASES.items():
        if (OUT / f"{name}.mp3").exists():  # удалить файл, чтобы перегенерировать
            continue
        tts = edge_tts.Communicate(text, VOICE, rate=rate, pitch=pitch, volume="+0%")
        await tts.save(str(OUT / f"{name}.mp3"))
        print("saved", name)
    # voices.js: те же файлы в base64, чтобы index.html работал даже открытым как файл (file://)
    lines = ["// Сгенерировано tools/make_voices.py — не править руками", "window.VOICES = {"]
    for name in PHRASES:
        data = base64.b64encode((OUT / f"{name}.mp3").read_bytes()).decode()
        lines.append(f'  {name}: "{data}",')
    lines.append("};")
    (OUT.parent / "voices.js").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("saved voices.js")


asyncio.run(main())
