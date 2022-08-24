class NotTriangleException(Exception):
    def __init__(self):
        super().__init__("This is not rectangle")