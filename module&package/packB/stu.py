class student:
        def __init__(self, sid, sname, sgrade):
            self.sid = sid
            self.sname = sname
            self.sgrade = sgrade

        def display(self):
            print(self.sid, self.sname, self.sgrade)

# obj=student(102,'dhiman','A')
# obj.display()