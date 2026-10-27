import customtkinter as ctk

class TimerComponents(ctk.CTkFrame):
    def __init__(self, parent, start_callback, reset_callback):
        super().__init__(parent)
        
        # Поле введення часу
        self.pole_vvoda_time = ctk.CTkEntry(self, placeholder_text="Введіть хвилини")
        self.pole_vvoda_time.pack(pady=10, padx=10)
        
        # Текстова мітка для показу відліку
        self.pokaz_time = ctk.CTkLabel(self, text="00:00", font=("Arial", 28, "bold"))
        self.pokaz_time.pack(pady=15)
        
        # Кнопка запуску
        self.button_start = ctk.CTkButton(self, text="Старт", command=start_callback)
        self.button_start.pack(pady=5)
        
        # Кнопка обнулення
        self.button_obnul = ctk.CTkButton(self, text="Обнулити", command=reset_callback, fg_color="gray")
        self.button_obnul.pack(pady=5)
