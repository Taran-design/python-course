books = ["maths","science","english","history"]
copies = [2,0,5,3]
fees = [2, 3 , 1 , 4]

def check_library():
    book_copies = copies.copy()
    avaliable_books = list(filter(lambda x : x > 0, book_copies))
    new_fees = list(map(lambda x : x + 1, fees))
    records = list(zip(books, book_copies))

    print("Library checker")
    for book ,copy in records:
        print(book, "-" ,copy, "copies")

    print("avaliable copies:", copies)
    print("updated late fees:", new_fees)

check_library()