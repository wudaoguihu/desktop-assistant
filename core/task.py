from abc import ABC, abstractmethod

class Task(ABC):
    name: str = "未命名任务"

    @abstractmethod
    def run(self, context: dict) -> str:
        """执行任务，返回结果描述"""
        pass