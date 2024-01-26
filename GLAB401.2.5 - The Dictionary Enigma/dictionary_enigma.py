# The Magical Library
library = {
    "Harry Potter": "J.K. Rowling",
    "The Lord of the Rings": "J.R.R. Tolkien",
    "To Kill a Mockingbird": "Harper Lee"
}

print("Our magical library contains the following books:")
for book, author in library.items():
    print(f"{book} by {author}")

print("But wait! A new book has appeared!")
library["The Great Gatsby"] = "F. Scott Fitzgerald"

print("Now our library contains the following books:")
for book, author in library.items():
    print(f"{book} by {author}")
