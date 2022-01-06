import cv2
from typing import List

from helper import Typed, Validatable, ImageUtils


class Input(Typed, Validatable):
    def __init__(self, data):
        self.data = data


class ImageInput(Input, ImageUtils):
    def __init__(self, base64_image: str):
        super().__init__(base64_image)

    def type(self):
        return 'image'

    def validate_data(self, data) -> bool:
        return self.validate_base64_image(data)

    @classmethod
    def from_file(cls, file_path):
        return cls.from_cv2_image(cv2.imread(file_path))


class TextInput(Input):
    def __init__(self, text: str):
        super().__init__(text)

    def type(self):
        return 'text'

    def validate_data(self, data) -> bool:
        return isinstance(data, str)


class GenericInput(Input):
    def __init__(self, data):
        super().__init__(data)

    def type(self) -> str:
        return 'generic'

    def validate_data(self, data) -> bool:
        return True


class GenericArrayInput(GenericInput):
    def __init__(self, data: List):
        super().__init__(data)

    def type(self) -> str:
        return 'generic_array'

    def validate_data(self, data) -> bool:
        return isinstance(data, list)


class NamedInput(Input):
    def __init__(self, name: str, input: Input):
        self.name = name
        self.input = input
        super().__init__(input.data)

    def type(self) -> str:
        return self.input.type()

    def validate_data(self, data) -> bool:
        return self.input.validate_data(data)


class CompositeInput(Input):
    def __init__(self, inputs: List[NamedInput]):
        result = {}
        for i in inputs:
            result[i.name] = i.input.data
        super().__init__(result)

    def type(self) -> str:
        return 'composite'

    def validate_data(self, data) -> bool:
        return all([i.validate_data(data) for i in self.data.values()])

# TODO SoundInput(sound en formato estandar, metadata)
