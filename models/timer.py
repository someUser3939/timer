import logging
import time
from abc import ABC, abstractmethod

# Налаштовуємо логування
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class TimeSpendInterface(ABC):
    @abstractmethod
    def countdown(self) -> int:
        pass


class Timer(TimeSpendInterface):
    def __init__(self, duration_seconds: int = 60, step: int = 1):
        self.duration_seconds = duration_seconds
        self.step = step

    def countdown(self) -> int:
        current_time = self.duration_seconds

        while current_time > 0:
            print(f"Залишилось часу: {current_time} сек.")
            time.sleep(self.step)
            current_time -= self.step

        logging.info("Час вийшов!")
        return current_time


class TimerConverter:
    MINUTE = 60
    HOUR = MINUTE * 60
    DAY = HOUR * 24

    @classmethod
    def to_seconds(cls, days: int = 0, hours: int = 0, minutes: int = 0) -> int:
        return (days * cls.DAY) + (hours * cls.HOUR) + (minutes * cls.MINUTE)


# Приклад використання:
if __name__ == "__main__":
    # Запускаємо таймер на 5 секунд для перевірки
    my_timer = Timer(duration_seconds=5)
    my_timer.countdown()


            
        


