class ContactRequest:
    def __init__(self, name="", email="", category="", priority="", message=""):
        self.name = name
        self.email = email
        self.category = category
        self.priority = priority
        self.message = message

    def __str__(self):
        return f"name:{self.name} email:{self.email} category:{self.category} priority:{self.priority} message:{self.message}"
