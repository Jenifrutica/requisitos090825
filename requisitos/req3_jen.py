class EduConnect:
    def __init__(self, lang="es"):
        self.languages = {
            "es": {
                "welcome": "Bienvenido a la plataforma EduConnect",
                "subscribe": "Suscribirse",
                "exit": "Salir"
            },
            "en": {
                "welcome": "Welcome to the EduConnect platform",
                "subscribe": "Subscribe",
                "exit": "Exit"
            }
        }
        self.current_languaje = lang if lang in self.languages else "es"

    def set_language(self, lang):
        if lang in self.languages:
            self.current_lang = lang
            return True
        return False

    def t(self, key):
        return self.languages[self.current_lang].get(key, f"[{key}]")