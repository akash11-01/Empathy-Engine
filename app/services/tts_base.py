from abc import ABC, abstractmethod

class BaseTTSService(ABC):
    @abstractmethod
    def synthesize(self, text: str, voice_params: dict, output_path: str) -> str:
        pass

    @abstractmethod
    def provider_name(self) -> str:
        pass