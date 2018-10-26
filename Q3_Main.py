# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 11:06:58 2018

@author: Jing
"""

import Car
import MaxHeap
# Test 
menulist = ['Enter: ',
		'1  for Extrat Max', 
		'2  for Insert', 
		'3  for Print']
def menu():
	for i in range(len(menulist)):
		print(menulist[i])
	return int(input())

def Main():
    MH = MaxHeap.MaxHeap()
    try:
        fo = open("Cars.txt", "r")
    except IOError:
        print("No such file!")
    else:
        for line in fo.readlines():
            info = line.split()
            Make = info[0]
            Model = info[1]
            Year = int(info[2])
            Mileage = float(info[3])
            Price = float(info[4])
            newCar = Car.Car(Make, Model, Year, Mileage, Price)
            MH.heapInsert(newCar)
        fo.close()
    print("Cars information in the system are as follows:")
    MH.printHeap()    
    s = menu()
    while s in range(1,4):
        if s == 1:
            if MH.heapSize > 0:
                oldCar = MH.extractMax()
                print("The car information with the max price are Make: %s, Model: %s, Year: %d, Mileage: %.0f, Price: %.0f" %(oldCar.Make, oldCar.Model, oldCar.Year, oldCar.Mileage, oldCar.Price))
            else:
                print("Empty heap!")
        if s == 2:
            print("Enter the new car information you want to insert:")
            Make = input("Make: ")
            Model = input("Model: ")
            Year = int(input("Year: "))
            Mileage = float(input("Mileage: "))
            Price = float(input("Price: "))
            newCar = Car.Car(Make, Model, Year, Mileage, Price)
            MH.heapInsert(newCar)
            print("Cars information in the system are as follows:")
            MH.printHeap()
        if s == 3:
            MH.printHeap()
        s = menu()
Main()