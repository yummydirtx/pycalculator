#!/usr/bin/env python3
import sys
import PySimpleGUI as sg
# this is a program written in the summer of 2020 by Alex Frutkin

operation = ""
firstNumber = 0.0
secondNumber = 0.0
layout = []

def calculate():
    layout = [[sg.Text("What is your first number?"), sg.InputText(key='firstnum')],
              [sg.Text("What operation do you want to do? (+, -, /, *)"), sg.InputText(key='op')],
              [sg.Text("What is your second number?"), sg.InputText(key='secondnum')],
              [sg.Submit(), sg.Cancel()]]
    window = sg.Window('PyCalculator', layout)
    event, values = window.read()
    window.close()
    firstNumber = float(values['firstnum'])
    operation = values['op']
    secondNumber = float(values['secondnum'])
    if operation == "+":
        print("The answer is " + str((firstNumber + secondNumber)))
        answer = firstNumber + secondNumber
    if operation == "-":
        print("The answer is " + str((firstNumber - secondNumber)))
        answer = firstNumber - secondNumber
    if operation == "/":
        print("The answer is " + str((firstNumber / secondNumber)))
        answer = firstNumber / secondNumber
    if operation == "*":
        print("The answer is " + str((firstNumber * secondNumber)))
        answer = firstNumber * secondNumber
    sg.popup(str(firstNumber) + " " + operation + " " + str(secondNumber) + " = " + str(answer))

print("PyCalculator, written in 2020 by yummyDev")
calculate()
#while operation != "q" and operation != "Q":
#   operation = input("What do you want to do? (+, -, /, *, q(uit)): ")
#    if operation != "+" and operation != "-" and operation != "/" and operation != "*" and operation != "q" and operation != "Q":
#        print("Error: " + operation + " is not recognized.")
#        break
#    if operation == "q" or operation == "Q":
#        break
#    print("Ok, you have selected the following operation: " + operation)
#    firstNumber = float(input("What is the first number you want to use? "))
#    secondNumber = float(input("What is the second number you want to use? "))
#    if operation == "+":
#        print("The answer is " + str((firstNumber + secondNumber)))
#    if operation == "-":
#        print("The answer is " + str((firstNumber - secondNumber)))
#    if operation == "/":
#        print("The answer is " + str((firstNumber / secondNumber)))
#    if operation == "*":
#        print("The answer is " + str((firstNumber * secondNumber)))
