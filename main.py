import random
import hashlib
import socket 
import os 

def send_otp():
    otp = random.randint(1000, 9999)
    print(f"[System] OTP sent: {otp}")
    return str(otp)

def check_access(role):
    if role == "Admin":
        print("Access: Manage Users")
    elif role == "Developer":
        print("Access: Source Code Repository")
    elif role == "HR":
        print("Access: Employee Data")
    else:
        print("Access: View Public Info")

def login(users):
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username not in users:
        print("Login failed: User not found.")
        return None, None

    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    if hashed_pw != users[username]['password']:
        print("Login failed: Incorrect password.")
        print (f"Try Again....\n")
        exit (0)
        return None, None
        

    otp_sent = send_otp()
    otp_input = input("Enter the OTP sent to your device: ").strip()
    if otp_input != otp_sent:
        print("Login failed: Incorrect OTP.quitting....")
        exit (0)
        

    print(f"Login successful! Welcome, {username}")
    return username, users[username]["role"]

def shell(username, role):
    print(f"\n[{username}@SecureIAM - {role}] Shell access granted. Type 'man' for commands. Type 'exit' to logout.")
    while True:
        cmd = input(f"{username}@SecureIAM> ").strip().lower()
        if cmd == "man":
            print("Available commands: man, role, access, whoami, exit")
        elif cmd == "role":
            print(f"Your role is: {role}")
        elif cmd == "access":
            check_access(role)
        elif cmd == "whoami":
            print (f"ip addr: {socket.gethostbyname(socket.gethostname())}")
        elif cmd == "exit":
            print("Logging out...")
            break
        # elif cmd == "shell":
        #     os.system(bin//sh)
        #     break
        else:
            print(f"Unknown command: {cmd}")
            SystemError
            SystemExit

if __name__ == "__main__":
    users = {
        "alice": {"password": hashlib.sha256("password1234#myDog".encode()).hexdigest(), "role": "Admin"},
        "bob": {"password": hashlib.sha256("devpass".encode()).hexdigest(), "role": "Developer"},
        "carol": {"password": hashlib.sha256("hrsecure".encode()).hexdigest(), "role": "HR"},
    }

    username, role = login(users)
    shell(username, role)
