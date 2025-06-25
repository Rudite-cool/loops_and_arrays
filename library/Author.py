
class Author():
    def __init__(self, name="", surname="", birth_year=0):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def __str__(self):
        return f"name {self.name}, surname {self.surname}, birth_year {self.birth_year}"
