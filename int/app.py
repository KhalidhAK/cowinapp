import os
from model.User import User
from model.Instructor import Instructor


users = []
instructors = []

def user_login():
    global users
    user_id = input('Enter UserId: ')
    for x in users:
        if user_id==x.user_id:
            print('user logged in')
            user_landing_page()
        else:
            print('User not found...Create new account')


def instructor_login():
    global instructors
    instructor_id=input('Enter InstructorId: ')
    for x in instructors:
        if instructor_id==x.instructor_id:
            print('Instructor logged in')
            instructor_landing_page()
        else:
            print('Instructor not found...Create new account')


def create_new_account():
    global users
    print('Creating new account...1.User 2.Instructor 3.Back')
    option = input()
    if option=='1':
        new_user = User()
        new_user.user_name = input('Enter User Name: ')
        while True:
            try:
                new_user.user_id = input('Enter User Id: ')
                if not users:
                    break
                else:
                    for x in users:
                        if new_user.user_id == x.user_id:
                            print("UserId already present...Please select another userId")
                            raise Exception
            except Exception:
                continue
            break
        users.append(new_user)

    elif option=='2':
        new_instructor = Instructor()
        new_instructor.instructor_name = input('Enter Instructor Name: ')
        while True:
            try:
                new_instructor.instructor_id = input('Enter Instructor Id: ')
                if not instructors:
                    break
                else:
                    for x in instructors:
                        if new_instructor.instructor_id == x.instructor_id:
                            print("InstructorId already present...Please select another InstructorId")
                            raise Exception
            except Exception:
                continue
            break
        instructors.append(new_instructor)
    elif option=='3':
        return
    else:
        print("Enter valid option")


def user_landing_page():
    print("USER LANDING PAGE")
    print("1.View Course 2.Logout")


def instructor_landing_page():
    print("INSTRUCTOR PAGE")


while True:
    print('Login as 1.User 2.Instructor 3.Create new account 4.Exit')
    option = input()
    if option == '1':
        user_login()
    elif option == '2':
        instructor_login()
    elif option == '3':
        create_new_account()
    elif option == '4':
        os._exit(1)
    else:
        print("Enter valid option")
