
from TaskManagerController import TaskManagerController

class CLI:
    def __init__(self):
        self.tmc = TaskManagerController()
        while(True):
            print("Witaj w aplikacji TASK MANAGER")
            decision = input("(L) - logowanie \n(R) - rejestracja \n(Q) - wyjście").upper()
            if(decision == "L"):
                log = self.tmc.login(input("podaj email:"), input("podaj password"))    # zwraca bool -> decyzja, int -> user_id
                if(log[0]):
                    self.menu(log[1])
            elif(decision == "R"):
                print("Jeszcze nie jest aktywna rejestrcja")
            else:
                print("Wyjście")
                break               # gdy program napotka break wychodzi z aktualnie wykonywanej pętli
    def menu(self, user_id):
        while(True):
            decision = input("(1) - dodaj zadanie \n(2) - wypisz zadania "
                             "\n(3) - usuń zadanie \n(4) - zmień hasło \n(Q) - cofnij").upper()
            if(decision == "1"):
                self.tmc.insertTaskByUser(
                    input("podaj nazwę "),
                    input("podaj opis "),
                    input("podaj kategorię ('SQL', 'Git', 'Python', 'PythonLib', 'ML') "),
                    user_id)
            elif(decision == "2"):
                self.tmc.selectTasks()
            elif (decision == "3"):
                self.tmc.selectTasks()
                self.tmc.deleteTaskById(int(input("podaj id zadania")))
            elif (decision == "4"):
                self.tmc.updateUserPassword(user_id, input("podaj nowe hasło"))
            elif (decision == "Q"):
                break
            else:
                print("błędny wybor")


cli = CLI()