class InvalidIntException(Exception):
    def __init__(self, arg):
        super().__init__('정수가 아닙니다. : {0}'.format(arg))

def convert_to_integer(text):
    if text.isdigit():
        return int(text)
    else:
        raise InvalidIntException(text)

if __name__ == '__main__':
    try:
        print('숫자를 입력하세요')
        text = input()
        text_type = type(text)
        print(text_type)
        number = convert_to_integer(text)
    except InvalidIntException as err:
        print('예외발생 ({0})'.format(err))
    else:
        print('정수형으로 변환되었습니다.{0}{1}'.format(number, type(number)))