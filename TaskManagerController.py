  
# klasa obsługująca żądania użytkownika aplikacji
# ALT + Enter -> auto-podpowiedź
from datetime import datetime, time

from config.tm_connect import ConnectionConfig

'''
        result = [
        [id_0,name_0,lastname_0, email_0, password_0,registration_0, enable_0],
        [id_1,name_1,lastname_1, email_1, password_1,registration_1, enable_1],
        [id_2,name_2,lastname_2, email_2, password_2,registration_2, enable_2],
        [id_3,name_3,lastname_3, email_3, password_3,registration_3, enable_3]
        ]
'''

class TaskManagerController:
    def __init__(self):
        self.conn = ConnectionConfig().connection()
        self.c = self.conn.cursor()
    def login(self, email, passwd):
        # wykonanie zapytania
        self.c.execute("SELECT * FROM user WHERE email = %s AND password = %s", (email, passwd))
        # pobranie wyniku zwracanego przez zapytanie (resultset)
        result = self.c.fetchone()
        if(result):
            print("zalogowano: " + result[3])
            return True, result[0]
        else:
            print("niezalogowano")
            return False, None
    def insertTaskByUser(self, task_name, task_description, task_category, user_id):
        self.c.execute("insert into task values(default, %s, %s, %s, %s)",
                       (task_name, task_description, task_category, user_id))
        # ?
        decision = input("potwierdź dodanie taska (T/N)").upper()
        if(decision == 'T'):
            self.conn.commit()      # zatwierdź i wprowadź do bazy danych
            print("dodano nowego taska: " + task_name)
            self.selectTasks()      # wywołanie metody selectTasks() w metodzie insertTaskByUser()
        else:
            self.conn.rollback()    # odrzuć dane i nie wprowadzaj do bazy danych
            print("nic nie dodano")
        # ?
    def selectTasks(self):
        self.c.execute("SELECT * FROM task")
        tasks = self.c.fetchall()
        for task in tasks:    # iteruje po rekordach
            # %s -> w to miejsce wprowadzam string
            # %15s -> w to miejsce wprowadzam string ale rezerwuje 15 znaków na jego reprezentacje
            task_id = task[0]
            task_name = task[1]
            task_description = task[2]
            task_category = task[3]
            user_id = task[4]
            print("| %3s | %15s | %30s | %15s | %15s |" %
                  (task_id, task_name, task_description, task_category, self.selectUserById(user_id)))
    def selectUserById(self, user_id):
        self.c.execute("SELECT name, lastname FROM user WHERE user_id = %s", str(user_id))
        selectedUser = self.c.fetchone()
        return selectedUser[0] + " " + selectedUser[1]
    def deleteTaskById(self, task_id):
        self.c.execute("DELETE FROM task WHERE task_id = %s", str(task_id))
        self.conn.commit()
        self.selectTasks()
    def updateUserPassword(self, user_id, newPassword):
        # update
        self.c.execute("UPDATE user SET password = %s WHERE user_id = %s", (newPassword, user_id))
        self.conn.commit()
        # dane użytkownika z nowym haslem
        print("hasło zostało zmienione")
        print(self.getUserById(user_id))
    def getUserById(self, user_id):
        self.c.execute("SELECT * FROM user WHERE user_id = %s", str(user_id))
        return self.c.fetchone()
    def insertSubtaskForTask(self, subtask_name, subtask_date_start, subtask_date_stop, task_id):      # dodaj podzadanie
        # YYYY-MM-dd
        self.c.execute("INSERT INTO subtask VALUES(default, %s, %s, %s, %s)",
                       (subtask_name, subtask_date_start, subtask_date_stop, task_id))
        self.conn.commit()
        self.selectTasksWithSubtasks()
    def deleteSubtaskById(self, subtask_id, task_id):         # usuń podzadanie
        self.c.execute("DELETE FROM subtask WHERE task_id = %s AND subtask_id = %s", (str(task_id), str(subtask_id)))
        self.conn.commit()
        self.selectTasksWithSubtasks()
    def selectTasksWithSubtasks(self):
        self.c.execute("SELECT t.*,s.* FROM task t left join subtask s ON (t.task_id = s.task_id) ORDER BY t.task_name;")
        for row in self.c.fetchall():
            print("| %2s | %10s | %10s | %10s | %2s | %10s | %10s | %10s | %10s |" %
                  (row[0],row[1],row[2],row[3], row[4],row[5],row[6], row[7], row[8]))
    def deleteTaskWithAllSubtasks(self,task_id): # usuń zadanie z wszystkimi jego podzadaniami
        self.c.execute('DELETE subtask FROM subtask LEFT JOIN task ON subtask.task_id = task.task_id WHERE task.task_id = %s',
            str(task_id))
        self.c.execute("DELETE FROM task WHERE task_id = %s", str(task_id))
        self.conn.commit()
        self.selectTasksWithSubtasks()
    def updateSubtaskByDateStop(self, subtask_id, task_id, dateStop):      # zmień datę zakończenia podzadania
        self.c.execute("UPDATE subtask SET subtask_date_stop = %s WHERE task_id = %s AND subtask_id = %s",
                       (dateStop, str(task_id), str(subtask_id)))
        self.conn.commit()
        self.selectTasksWithSubtasks()
tmc = TaskManagerController()
tmc.login('mk@mk.pl', 'mk')         # ok
tmc.insertTaskByUser("test111","test111","Python",1)
tmc.deleteTaskById(16)
tmc.updateUserPassword(1,"cba")
