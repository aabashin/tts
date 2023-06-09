![Python version](https://img.shields.io/badge/python-%3E%3D3.8-green)
[![Issues](https://img.shields.io/github/issues-raw/aabashin/tts)](https://github.com/aabashin/tts/issues)

![Linter](https://github.com/aabashin/tts/workflows/Linter/badge.svg)
![Formatter](https://github.com/aabashin/tts/workflows/Formatter/badge.svg)

# Text-To-Speech

Simple TTS service based on [russian neural model](https://github.com/snakers4/silero-models) and [normalize neural model](https://github.com/snakers4/russian_stt_text_normalization) by Silero

## Up and running

```bash
git clone https://github.com/aabashin/tts.git
cd tts
docker-compose up -d
```

You can try to send POST request on `http://127.0.0.1:7700` with body like this:

```bash
{"text": "Текст для проверки произношения."}
```

## Settings

All settings in `settings.toml`

You can change speaker's voice or sample rate of out wave file.

## Down service

Execute to stop service:

```bash
docker-compose down
```

## Troubleshouting

You can change log level to `debug` in `settings.toml` by `LOG_LEVEL = "debug"` and restart your docker container by:

```bash
docker-compose restart
```

Log file located in `./logs/tts.log`
