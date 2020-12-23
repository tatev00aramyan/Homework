import operator
import logging
LOG_FORMAT = " %(levelname)s::%(asctime)s:: ----- %(message)s"
logging.basicConfig(filename="C:\\git\\Homework\\homework1\\log\\test.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')

logging.info("My first message! ")

def error_msg(token, values):
    return f'Error: {token} takes 2 values.'.format (token)


stack = []
operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,

}
print(" ----->Polish Notaion Calculator\n",
      "----->Do not forget to set spaces after operands and operators.\n",
      "----->GOOD LUCK!\n",
      "----->If you want to quit -> enter 'q' or 'exit'\n")
if __name__ == '__main__':
    while True:
        expression = input("# enter an expression in polish notation >>>>  ")

        if expression in ('q',  'exit'):
            break
        exp = expression.split()
        # print(exp)
        exp.reverse()

        for token in exp:
            if token in operators:
                try:
                    stack.append(operators[token](stack.pop(-1), stack.pop()))
                except:
                    logging.exception(error_msg(token, operators[token]))
                    print(error_msg(token, operators[token]))
            else:
                 try:
                    stack.append(float(token))
                 except ValueError:
                    print("ERROR: Only Real Numbers Or ['+', '-','*','/']")
                    logging.exception("ERROR: Only Real Numbers Or ['+', '-','*','/']")
                    logging.info("1")

        if len(stack) == 1:
            print("Result : ", str(stack.pop()))
            logging.info("1")
        else:
            print("ERROR: INVALID EXPRESSION")