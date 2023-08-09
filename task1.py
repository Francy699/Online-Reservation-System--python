from collections import UserDict,UserList, UserString
from os import name
import sys
import datetime
import sqlite3
import mysql.connector
from random import *


#login form
users={
    "user1":{"password":"pass1","name":"Randy"},
    "user2":{"password":"pass2","name":"Keny"}
}
def login():
    while True:
        username=input("username:")
        password=input("password:")
        if username in users and users[username]["password"]==password:
            print("welcome",username)
            return username
        else:
            print("Invalid username or password.Please try again.")

#login form
def user_login():
    def create_user():
        
       print("===== Create New User =====")
       username = input("Enter a username: ")
       password = input("Enter a password: ")
       users[username] = password
       print("User created successfully.")

    def login():
       
       print("===== User Login =====")
       username = input("Enter your username: ")
       password = input("Enter your password: ")

       if username in users and users[username] == password:
           print("Login successful. Welcome,", username)
       else:
           print("Login failed. Incorrect username or password.")
        
#Reservation Form
class Train:
    def __init__(self, name, schedule, total_seats):
        self.name = name
        self.schedule = schedule
        self.total_seats = total_seats
        self.available_seats = total_seats

class RailwayTicketReservationSystem:
    def __init__(self):
        self.trains = []

    def add_train(self, name, schedule, total_seats):
        train = Train(name, schedule, total_seats)
        self.trains.append(train)

    def display_trains(self):
        print("Available Trains:")
        for i, train in enumerate(self.trains, start=1):
            print(f"{i}. {train.name} - Schedule: {train.schedule} - Available Seats: {train.available_seats}")

    def book_ticket(self, train_index, num_tickets):
        if 1 <= train_index <= len(self.trains):
            train = self.trains[train_index - 1]
            if train.available_seats >= num_tickets:
                train.available_seats -= num_tickets
                print(f"Successfully booked {num_tickets} tickets for {train.name}.")
            else:
                print("Sorry, there are not enough seats available for the selected train.")
        else:
            print("Invalid train selection")
            

#cancellation form
def cancel_ticket():
    ticket_number = input("Enter Ticket Number: ")
    passenger_name = input("Enter Passenger Name: ")
    cancellation_reason = input("Enter Cancellation Reason: ")

    # Replace the following with your actual ticket cancellation logic
    if ticket_number and passenger_name and cancellation_reason:
        # Simulate ticket cancellation process (print the details)
        print(f"Ticket Number: {ticket_number}")
        print(f"Passenger Name: {passenger_name}")
        print(f"Cancellation Reason: {cancellation_reason}")
        print("Ticket cancellation successful!")
    else:
        print("Please fill in all the fields.")
       
def main():
    print("Welcome to the online reservation system")
     #dictionary to store the credentials
    login() #calling the login()
    reservation_system = RailwayTicketReservationSystem()

    # Adding sample trains to the system
    reservation_system.add_train("Express 101", "10:00 AM", 100)
    reservation_system.add_train("Fast Train 202", "2:30 PM", 150)
    reservation_system.add_train("Local 303", "6:45 PM", 80)
    while True:
        print("1. Make Reservation")
        print("2.cancel Reservation")
        print("3.logout")
        choice=int(input("enter your choice:"))
        
        if choice == 1:
            reservation_system.display_trains()
        elif choice == 2:
            reservation_system.display_trains()
            train_index = int(input("Enter the number of the train you want to book: "))
            num_tickets = int(input("Enter the number of tickets you want to book: "))
            reservation_system.book_ticket(train_index, num_tickets)
        elif choice == 3:
            print("Thank you for using the Railway Ticket Reservation System. Have a great day!")
        elif choice == 4:
            cancel_ticket()
        elif choice == 5:
            print("logging out...")
            break
        else:
            print("Invalid choice.Please try again.")
if __name__=="__main__":
    main()
    



            
    