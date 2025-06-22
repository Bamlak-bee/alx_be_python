class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    def __del__(self):
        print(f"Deleting {self.title}")
    
    def __str__(self):
        # Returns a human-readable string representation of the Book object, including its title, author, and publication year.
        return (f"{self.title} by {self.author}, published in {self.year}")

    # Returns an unambiguous string representation of the Book object, suitable for debugging and reproduction.
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
