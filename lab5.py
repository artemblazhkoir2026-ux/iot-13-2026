class TimeConverter:
    def __init__(self):
        pass

    def __del__(self):
        pass 
        
    @staticmethod
    def time_to_seconds(time_str):
        hours, minutes, seconds = map(int, time_str.split(":"))
        return hours * 3600 + minutes * 60 + seconds

    @staticmethod
    def seconds_to_time(total):
        hours = total // 3600
        minutes = (total % 3600) // 60
        seconds = total % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    @staticmethod
    def output_converted_time(*args):
        if len(args) == 1 and isinstance(args[0], str):
            print(f"{args[0]} -> {TimeConverter.time_to_seconds(args[0])}")
        elif len(args) == 1:
            print(f"{args[0]} -> {TimeConverter.seconds_to_time(args[0])}")
        elif len(args) == 3:
            hours, minutes, seconds = args
            total = hours * 3600 + minutes * 60 + seconds
            print(f"{hours:02d}:{minutes:02d}:{seconds:02d} -> {total}")
        else:
            raise TypeError("Expected a string, one number or three numbers")


TimeConverter.output_converted_time("01:30:45")
TimeConverter.output_converted_time(5445)
TimeConverter.output_converted_time(23, 59, 59)
