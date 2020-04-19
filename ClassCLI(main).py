# cli - command line interface aplikacji
# gui - graphical user interface
from controller.tm_controller import TaskManagerController

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
                             "\n(3) - usuń zadanie \n(4) - zmień hasło \n(5) - dodaj podzadanie "
                        "\n(6) - zmodyfikuj podzadanie \n(7) - usuń podzadanie \n(8) - usuń zadanie "
                             "\n(Q) - cofnij").upper()
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
            elif (decision == "5"):
                self.tmc.insertSubtaskForTask(
                    input("podaj nazwę: "),
                    input("podaj date rozpoczęcia: "),
                    input("podaj datę zakończenia: "),
                    input("podaj id głownego zadania: ")
                )
            elif (decision == "6"):
                self.tmc.updateSubtaskByDateStop(
                    input("podaj id podzadania, które chcesz zmodyfikować: "),
                    input('podaj id zadania głownego: '),
                    input('podaj nowa date zakończenia podzadania: ')
                )
            elif (decision == "7"):
                self.tmc.deleteSubtaskById(
                    input("podaj id podzadania, które chcesz usunąć: "),
                    input("podaj id zadania głównego do którego nalezy to podzadanie: ")
                )
            elif (decision == "8"):
                self.tmc.deleteTaskWithAllSubtasks(
                    input("Podaj id zadania głownego które chcesz usunąć")
                )
            elif (decision == "Q"):
                break
            else:
                print("błędny wybor")


cli = CLI()   # utworzenie obiektu klasy CLI