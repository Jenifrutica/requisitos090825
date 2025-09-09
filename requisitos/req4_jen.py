class EduConnectPayments:
    def __init__(self):
        self.extensionCourses = {
            "Cursito 1": 100.000,
            "Cursito 2": 55.000,
            "Cursito 3": 70.000
        }

    def listOfExtensionCourses(self):
        return self.extensionCourses

    def PaymentProcess(self, courseName, user):
        if courseName not in self.extensionCourses:
            return f"El curso '{courseName}' no existe."

        amount = self.extensionCourses[courseName]
        print(f"[Simulación] Usuario {user} paga {amount} COP por {courseName}")
        return f"Pago de {amount} COP por '{courseName}' realizado con éxito (simulado)."
