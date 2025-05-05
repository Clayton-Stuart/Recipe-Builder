class step:
    def __init__(self, title, text):
        self.title = title
        self.text = text

    def changeText(self, text) -> None:
        self.text = text

    def changeTitle(self, title) -> None:
        self.title = title
    