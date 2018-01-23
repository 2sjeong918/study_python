try:
    print(1/0)
except:
    print('예외')

my_list = [1,2,3]

def do_try():
    try:
        print('첨자를 입력하세요')
        index = int(input())
        print(my_list[index])
    except ZeroDivisionError as err:
        print("0으로 나눌 수 없습니다. ({0})".format(err))
    except IndexError:
        print('잘못된 첨자입니다.')
    # except ValueError:
    #     print('숫자만 입력가능합니다')
    except:
        print('뭔가 잘못됬습니다.')
        return
    else:
        print("리스트의 요소 출력에 성공했습니다.")

    finally:
        print("어떤 일이 있어도 마무리합니다.")

do_try()

# raise Exception('예외입니다.')

try:
    raise Exception('예외입니다.')
except Exception as err:
    print('예외: {0}'.format(err))

