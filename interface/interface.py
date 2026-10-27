import os
import sys

import customtkinter as ctk

if __package__ in (None, ""):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    from interface.components import TimerComponents
    from models.timer import Timer, TimerConverter
else:
    from .components import TimerComponents
    from models.timer import Timer, TimerConverter


class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry('400x350')
        self.title('Timer App')
        
        # Ініціалізуємо бізнес-логіку таймера
        self.timer_logic = Timer()
        
        # Створюємо графічні компоненти
        self.timer_view = TimerComponents(
            parent=self, 
            start_callback=self.press_start, 
            reset_callback=self.press_reset
        )
        self.timer_view.pack(pady=20, fill="both", expand=True)

    def press_start(self):
        try:
            # Припускаємо, що користувач вводить хвилини
            minutes = int(self.timer_view.pole_vvoda_time.get())
            # Переводимо хвилини в секунди за допомогою вашого конвертера
            seconds = TimerConverter.to_seconds(minutes=minutes)
            
            self.timer_logic.start(seconds)
            self.update_timer()  # Запускаємо цикл оновлення в GUI
        except ValueError:
            self.timer_view.pokaz_time.configure(text="Помилка вводу!")

    def press_reset(self):
        self.timer_logic.stop()
        self.timer_logic.current_time = 0
        self.timer_view.pokaz_time.configure(text="00:00")
        self.timer_view.pole_vvoda_time.delete(0, 'end')

    def update_timer(self):
        """Головний неблокуючий цикл таймера для GUI"""
        if self.timer_logic.is_running:
            # Робимо "тік" логіки таймера
            current_seconds = self.timer_logic.tick()
            
            # Красиво форматуємо секунди у формат ХХ:ХХ
            mins, secs = divmod(current_seconds, 60)
            self.timer_view.pokaz_time.configure(text=f"{mins:02d}:{secs:02d}")
            
            if current_seconds > 0:
                # Плануємо наступний виклик цієї ж функції рівно через 1 секунду (1000 мс)
                self.after(1000, self.update_timer)
            else:
                self.timer_view.pokaz_time.configure(text="Час вийшов!")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = Interface()
    app.mainloop()

