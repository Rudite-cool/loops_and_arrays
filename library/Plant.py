class Plant():
    def __init__(self, name="", latin_name="", one_year=False, continent="", height=0.0, eatable=False):
        self.name = name
        self.latin_name = latin_name
        self.one_year = one_year
        self.continent = continent
        self.height = height
        self.eatable = eatable

    def __str__(self):
        one_year_text = "Yes" if self.one_year else "No"
        eatable_text = "Yes" if self.eatable else "No"
        return (f"{self.name} ({self.latin_name}), "
                f"one_year: {one_year_text}, "
                f"continent: {self.continent}, "
                f"height: {self.height} m, "
                f"eatable: {eatable_text}")

