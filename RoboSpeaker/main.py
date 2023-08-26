import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.0, created by Sudarshan")
    while True:
        x = input("Enter what you want me to speak : ")
        if x == "q":
            os.system("say 'bye bye'")
            break
        command = f"say {x}"
        os.system(command)