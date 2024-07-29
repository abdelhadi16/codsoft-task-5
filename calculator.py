import tkinter as tk
from tkinter import messagebox

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation )
    



def evaluate_calculator():
    global calculation
    try:
        result = evaluate_expression(calculation)
        if result is not None:
            calculation = str(result)
            text_result.delete(1.0, "end")
            text_result.insert(1.0, calculation)
        else:
            raise ValueError
    except Exception as e:
        clear_field()
        text_result.insert(1.0, "ERROR")
       
def evaluate_expression(expression):
    try:
        # Split the expression by operators and keep the operators in a separate list
        numbers = []
        operators = []
        i = 0
        while i < len(expression):
            if expression[i].isdigit() or expression[i] == '.':
                j = i
                while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                    j += 1
                numbers.append(float(expression[i:j]))
                i = j
            else:
                operators.append(expression[i])
                i += 1
        
        i = 0
        while i < len(operators):
            if operators[i] == '*':
                numbers[i] = numbers[i] * numbers[i + 1]
                numbers.pop(i + 1)
                operators.pop(i)
            elif operators[i] == '/':
                if numbers[i + 1] == 0:
                    return None
                numbers[i] = numbers[i] / numbers[i + 1]
                numbers.pop(i + 1)
                operators.pop(i)
            else:
                i += 1

        #  addition and subtraction
        result = numbers[0]
        for i in range(len(operators)):
            if operators[i] == '+':
                result += numbers[i + 1]
            elif operators[i] == '-':
                result -= numbers[i + 1]
        
        return result
    except:
        return None


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0,"end")





root = tk.Tk()
root.geometry("300x350")
root.title("calculator")
root.resizable(width=0,height=0)
text_result = tk.Text(root,height=2,width=16,font=("Arial",24))
text_result.grid(columnspan=5)
bt_1 = tk.Button(root,text='1',command=lambda:add_to_calculation(1),width=5 , font=("Arial",14) )
bt_1.grid(row=2, column=1)
bt_2 = tk.Button(root,text='2',command=lambda:add_to_calculation(2),width=5 , font=("Arial",14) )
bt_2.grid(row=2,column= 2)
bt_3 = tk.Button(root,text='3',command=lambda:add_to_calculation(3),width=5 , font=("Arial",14) )
bt_3.grid(row=2,column=3)
bt_4 = tk.Button(root,text='4',command=lambda:add_to_calculation(4),width=5 , font=("Arial",14) )
bt_4.grid(row=3,column=1)
bt_5 = tk.Button(root,text='5',command=lambda:add_to_calculation(5),width=5 , font=("Arial",14) )
bt_5.grid(row=3,column=2)
bt_6 = tk.Button(root,text='6',command=lambda:add_to_calculation(6),width=5 , font=("Arial",14) )
bt_6.grid(row=3,column=3)
bt_7 = tk.Button(root,text='7',command=lambda:add_to_calculation(7),width=5 , font=("Arial",14) )
bt_7.grid(row=4,column=1)
bt_8 = tk.Button(root,text='8',command=lambda:add_to_calculation(8),width=5 , font=("Arial",14) )
bt_8.grid(row=4,column=2)
bt_9 = tk.Button(root,text='9',command=lambda:add_to_calculation(9),width=5 , font=("Arial",14) )
bt_9.grid(row=4,column=3)
bt_0 = tk.Button(root,text='0',command=lambda:add_to_calculation(0),width=5 , font=("Arial",14) )
bt_0.grid(row=5,column=2)
bt_plus = tk.Button(root,text='+',command=lambda:add_to_calculation('+'),width=5 , font=("Arial",14) )
bt_plus.grid(row=2,column=4)
bt_minos = tk.Button(root,text='-',command=lambda:add_to_calculation('-'),width=5 , font=("Arial",14) )
bt_minos.grid(row=3,column=4)
bt_mul= tk.Button(root,text='x',command=lambda:add_to_calculation('*'),width=5 , font=("Arial",14) )
bt_mul.grid(row=4,column=4)
bt_div = tk.Button(root,text='/',command=lambda:add_to_calculation('/'),width=5 , font=("Arial",14) )
bt_div.grid(row=5,column=4)
bt_open = tk.Button(root,text='(',command=lambda:add_to_calculation('('),width=5 , font=("Arial",14) )
bt_open.grid(row=5,column=1)
bt_close = tk.Button(root,text=')',command=lambda:add_to_calculation(')'),width=5 , font=("Arial",14) )
bt_close.grid(row=5,column=3)
bt_equel = tk.Button(root,text='=',command=evaluate_calculator,width=10 , font=("Arial",14) )
bt_equel.grid(row=6,column=3,columnspan=2)
bt_clear = tk.Button(root,text='C',command=clear_field,width=10 , font=("Arial",14) )
bt_clear.grid(row=6,column=1, columnspan=2)
root.mainloop()


