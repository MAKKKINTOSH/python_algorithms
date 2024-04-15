from typing import Callable


class InputParser:
    @staticmethod
    def from_console(data_type: str) -> list[list[int]]:
        data = input()
        parser = InputParser.__get_data_parser(data_type)
        output = parser(data)
        return output

    @staticmethod
    def from_string(data: str, data_type: str) -> list[list[int]]:
        parser = InputParser.__get_data_parser(data_type)
        output = parser(data)
        return output

    @staticmethod
    def __get_data_parser(data_type: str) -> Callable:
        match data_type:
            case "js_array":
                return InputParser.__js_array_parser

    @staticmethod
    def __js_array_parser(data: str) -> list[list[int]]:
        """
            input:  [[1,2],[32,43534],[123,2],...,[31,31]]
            output: list([1,2],[32,43534],[123,2],...,[31,31])
        """
        return [list(map(lambda x: int(x), list(i.split(",")))) for i in data[2:-2].split("],[")]
