# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 10:24:04 2018

@author: Jing
"""

import Car

class MaxHeap(object):
    
    def __init__(self):
        self.__Array__ = [Car.Car(0,0,0,0,0)] *100
        self.heapSize = 0
        
    def __heapify__(self, parent):
        Lson = 2*parent + 1
        Rson = 2*parent +2
        if self.__Array__[Lson].Price > self.__Array__[parent].Price and Lson <= self.heapSize - 1:
            largest = Lson
        else:
            largest = parent
        if self.__Array__[Rson].Price > self.__Array__[largest].Price and Rson <= self.heapSize - 1:
            largest = Rson
        if largest != parent:
            temp = self.__Array__[parent]
            self.__Array__[parent] = self.__Array__[largest]
            self.__Array__[largest] = temp
            self.__heapify__(largest)
            
    def __buildHeap__(self):
        for i in range(int((self.heapSize - 1)/2), -1, -1):
            self.__heapify__(i)
            
    def extractMax(self):
        Max = self.__Array__[0]
        self.__Array__[0] = self.__Array__[self.heapSize - 1]
        self.heapSize = self.heapSize - 1
        self.__heapify__(0)
        return Max
    
    def heapInsert(self, newCar):
        self.heapSize = self.heapSize + 1
        i = self.heapSize -1
        parent = int((i - 1)/2)
        while i > 0 and self.__Array__[parent].Price < newCar.Price:
            self.__Array__[i] = self.__Array__[parent]
            i = parent
            parent = int((i - 1)/2)
        self.__Array__[i] = newCar
        
    def printHeap(self):
        for i in range(self.heapSize):
            print("Make: %s, Model: %s, Year: %d, Mileage: %.0f, Price: %.0f" %(self.__Array__[i].Make, self.__Array__[i].Model, self.__Array__[i].Year, self.__Array__[i].Mileage, self.__Array__[i].Price))