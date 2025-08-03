import datetime

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        try:
            self.file = open(self.filename, "r")
            self.users = {}
            for line in self.file:
                if line.strip():  # Skip empty lines
                    try:
                        email, password, name, created = line.strip().split(";")
                        self.users[email] = (password, name, created)
                    except ValueError:
                        print(f"Skipping malformed line: {line.strip()}")
            self.file.close()
        except FileNotFoundError:
            # Create the file if it doesn't exist
            open(self.filename, "w").close()
            self.users = {}

    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return -1

    def add_user(self, email, password, name):
        if email.strip() not in self.users:
            self.users[email.strip()] = (
                password.strip(),
                name.strip(),
                DataBase.get_date()
            )
            self.save()
            return 1
        else:
            print("Email already exists")
            return -1

    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(f"{user};{self.users[user][0]};{self.users[user][1]};{self.users[user][2]}\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]
