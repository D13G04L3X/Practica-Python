import datetime
import random
import operator

class SmartChatbot:
    def __init__(self):
        self.memory = {}
        self.mood = "neutral"
        self.reminders = [] # Lista de recordatorios

        self.responses = {
            "hola": ["¡Hola! ¿Cómo te sientes hoy? 😊", "¡Hey! ¿Qué tal?", "¡Hola! ¿Cómo va tu día? 🌟"],
            "bien": ["Súper, escribe lo que quieras saber!"],
            "estado": ["Estoy bien, gracias por preguntar. ¿Y tú?", "¡Todo en orden! ¿Cómo te ha ido hoy?", "Me siento genial, ¿qué tal tú?"],
            "nombre": ["Puedes llamarme Bot, pero si quieres, dime otro nombre. 🤖", "Soy un chatbot, pero dime cómo quieres que me llame."],
            "ayuda": ["Dime en qué necesitas ayuda y veré qué puedo hacer. 💡", "Estoy aquí para ayudarte, pregunta lo que quieras."],
            "hora": lambda: f"La hora actual es {datetime.datetime.now().strftime('%H:%M:%S')} ⏰",
            "chiste": ["¿Por qué el libro de matemáticas estaba triste? Porque tenía demasiados problemas. 😂", "¿Qué hace una abeja en el gimnasio? ¡Zum-ba! 🐝"],
            "triste": ["Lo siento mucho 😢, ¿quieres hablar de ello?", "Ánimo, aquí estoy para escucharte. 💙"],
            "feliz": ["¡Me alegra saber eso! 🎉", "¡Genial! Cuéntame, ¿qué te tiene tan feliz? 😊"],
            "cansado": ["Tal vez deberías descansar un poco. 💤", "¡Recuerda tomar pausas! Relájate un poco. ☕"],
            "recordar": self.set_reminder,
            "ver recordatorios": self.show_reminders,
            "película": self.recommend_movie,
            "música": self.recommend_song,
            "calcular": self.calculate_expression
        }

    def set_reminder(self):
        recordatorio = input("¿Qué quieres que recuerde? 📝: ")
        self.reminders.append(recordatorio)
        return "¡Listo! He guardado tu recordatorio. ✅"
    
    def show_reminders(self):
        if not self.reminders:
            return "No tienes recordatorios pendientes. 📌"
        return "Aquí están tus recordatorios: " + ", ".join(self.reminders)
    
    def recommend_movie(self):
        peliculas = ["Inception", "El Padrino", "Interstellar", "Matrix", "Parasite"]
        return f"Te recomiendo ver '{random.choice(peliculas)}'. 🍿"
    
    def recommend_song(self):
        musica = ["Bohemian Rhapsody - Queen", "Shape of You - Ed Sheeran", "Blinding Lights - The Weeknd"]
        return f"Te recomiendo escuchar '{random.choice(musica)}'. 🎶"
    
    def calculate_expression(self):
        try:
            calcular = input("Escribe una operación matemática (ejemplo: 5 + 3): ")
            operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

            for symbol, func in operators.items():
                if symbol in calcular:
                    num1, num2 = map(float, calcular.split(symbol))
                    return f"El resultado es: {func(num1, num2)}"
            
            return "Error, operación no válida"
        except Exception as e:
            return "Hubo un error en el cáluclo, Asegúrate de ingresar una operación válida."
        

    def analyze_input(self, user_input):
        user_input = user_input.lower()
        
        if user_input.startswith("me llamo"):
            name = user_input.split("me llamo", 1)[1].strip()
            self.memory["nombre"] = name
            return f"¡Mucho gusto, {name}! 😊 ¿Cómo te sientes hoy?"

        if "cómo me llamo" in user_input:
            return f"Me dijiste que te llamas {self.memory.get('nombre', 'pero no recuerdo que lo hayas mencionado. 🤔')}"

        for key, responses in self.responses.items():
            if key in user_input:
                if isinstance(responses, list):
                    return random.choice(responses)
                elif callable(responses):
                    return responses()
                elif isinstance(responses, dict):
                    for mood_key, mood_responses in responses.items():
                        if mood_key in user_input:
                            return random.choice(mood_responses)

        return "Mmm... no estoy seguro de qué decir sobre eso. 🤔 Cuéntame más."

    def chat(self):
        print("🤖 ¡Hola! Soy un chatbot avanzado. Hablemos. (Escribe 'adiós' para salir)")

        while True:
            user_input = input("Tú: ")
            response = self.analyze_input(user_input)
            print(f"Chatbot: {response}")

            if "adiós" in user_input:
                print("Chatbot: ¡Nos vemos! Que tengas un excelente día. 👋")
                break
    
bot = SmartChatbot()
bot.chat()


