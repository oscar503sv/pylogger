from utils.Logger import Logger
import traceback

number1 = 10
number2 = 0

def main():
    try:
        result = number1 / number2
        Logger.add_to_log('info', 'Result is: {}'.format(result))
    except Exception as ex:
        Logger.add_to_log('error', traceback.format_exc())
        Logger.add_to_log('error', str(ex))
        print("Cannot divide by 0")

if __name__ == "__main__":
    main()
