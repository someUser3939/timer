import logging
from abc import ABC, abstractmethod

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class TimeSpendInterface(ABC):
    @abstractmethod
    def tick(self) -> int:
        pass

class Timer(TimeSpendInterface):
    def __init__(self, duration_seconds: int = 60, step: int = 1):
        self.duration_seconds = duration_seconds
        self.current_time = duration_seconds
        self.step = step
        self.is_running = False

    def start(self, duration: int):
        self.duration_seconds = duration
        self.current_time = duration
        self.is_running = True

    def stop(self):
        self.is_running = False

    def tick(self) -> int:
        """Зменшує час на один крок. Викликається з GUI щосекунди."""
        if self.is_running and self.current_time > 0:
            self.current_time -= self.step
            if self.current_time <= 0:
                self.is_running = False
                logging.info("Час вийшов!")
        return self.current_time

class TimerConverter:
    MINUTE = 60
    HOUR = MINUTE * 60
    DAY = HOUR * 24

    @classmethod
    def to_seconds(cls, days: int = 0, hours: int = 0, minutes: int = 0) -> int:
        return (days * cls.DAY) + (hours * cls.HOUR) + (minutes * cls.MINUTE)



            
        


