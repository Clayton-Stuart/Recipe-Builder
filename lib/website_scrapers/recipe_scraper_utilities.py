import re

class recipe:
    def __init__(self, name: str, ingredients: any, titles: list, steps: list):
        self.name = name
        self.ingredients = ingredients
        self.titles = titles
        self.steps = steps

    def changeName(self, name) -> None:
        self.name = name

    def changeIngredients(self, ingredients) -> None:
        self.ingredients = ingredients

    def changeTitles(self, titles) -> None:
        self.titles = titles

    def changeSteps(self, steps) -> None:
        self.steps = steps

    def verify(self) -> bool:
        if (len(self.steps) == (len(self.titles))):
            return True
        return False
    
    def stripIngredientFormatting(self) -> None:
        for i in range(len(self.ingredients)):
            self.ingredients[i] = self.ingredients[i].strip()
            if self.ingredients[i][:3] == "<h>":
                self.ingredients[i] = self.ingredients[i][3:]



def extract_domain(url):
  # Define a regular expression pattern for extracting the domain
  pattern = r"(https?://)?(www\d?\.)?(?P<domain>[\w\.-]+\.\w+)(/\S*)?"
  # Use re.match to search for the pattern at the beginning of the URL
  match = re.match(pattern, url)
  # Check if a match is found
  if match:
  # Extract the domain from the named group "domain"
    domain = match.group("domain")
    return domain
  else:
    return ""