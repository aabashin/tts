from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="TTS",
    settings_files=["settings.toml"],
)
