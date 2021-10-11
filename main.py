## Imports
import math
import os

## Vars
allowed_users = {
"test" : "abc",
}

## Class
class Menu():
    def __init__(self):
        self.current_state = "4"
        self.main_table = ["hi",50,100]

        while True:
            os.system("PAUSE")
            os.system("cls")

            if self.current_state == "0":
                exit()
            elif self.current_state == "1":
                self.page_additem()
            elif self.current_state == "2":
                self.page_list()
            elif self.current_state == "3":
                self.page_remitem()
            elif self.current_state == "4":
                self.page_menu()


    def page_menu(self):
        print("-------")
        print("Menu")
        print("-------")
        print("1. Add Item")
        print("2. View Items")
        print("3. Remove Item")
        print("0. Exit")
        print("-------")
            
        page = input(">>> ")

        if page in ["0","1","2","3"]:
            self.current_state = page
        else:
            self.current_state = "4"
            
    def page_additem(self):
        print("-------")
        print("Add New Item")
        print("-------")
        print("YOUR TABLE")
        self.print_table()
        print("-------")
        print("1. Add to index")
        print("2. Add to end")
        print("3. Add to beginning")
        print("0. Back")
        print("-------")

        user_select = int(input(">>> "))

        if user_select in [0]:
            self.current_state = "4"
        elif user_select == 1:
            index = int(input("Index: "))
            item = input("Add: ")
            try:
                self.main_table[index] = item
            except:
                print("Index too far")
        elif user_select == 2:
            item = input("Add: ")
            self.main_table.append(item)
        elif user_select == 3:
            item = input("Add: ")
            try:
                self.main_table[0] = item
            except:
                self.main_table.append(item)
            
        
    def page_list(self):
        print("-------")
        print("List Items")
        print("-------")
        print("1. List All")
        print("2. List Simmilar")
        print("3. List Index's")
        print("0. Back")
        print("-------")

        user_select = int(input(">>> "))

        if user_select in [0]:
            self.current_state = "4"
        elif user_select == 1:
            self.print_table()
        elif user_select == 2:
            sim = input("Simmilar: ")
            for item in self.main_table:
                if str(item) == str(sim):
                    print(item)
        elif user_select == 3:
            ind = input("(seperate by /) Index's: ")
            t = ind.split("/")

            newt = []

            for item in t:
                try:
                    newt.append(self.main_table[int(item)])
                except:
                    print("index "+str(item)+" doesnt exist")

            print(newt)
            
        
    def page_remitem(self):
        print("-------")
        print("Remove Item")
        print("-------")
        print("YOUR TABLE")
        self.print_table()
        print("-------")
        print("1. Remove Index")
        print("2. Clear Table")
        print("0. Back")
        print("-------")

        user_select = int(input(">>> "))

        if user_select in [0]:
            self.current_state = "4"
        elif user_select == 1:
            index = int(input("Index: "))
            try:
                self.main_table.pop(index)
            except:
                print("List index does not exist")
        elif user_select == 2:
            self.main_table = []

    def print_table(self):
        print(self.main_table)

myMenu = Menu()
os.system("PAUSE")

