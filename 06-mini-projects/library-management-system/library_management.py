
BOOKS_FILE = "books.txt"
USERS_FILE = "users.txt"
LOANS_FILE = "loans.txt"



def create_files():
    """Create the required data files if they do not already exist."""

    for file in [BOOKS_FILE, USERS_FILE, LOANS_FILE]:

        try:
            open(file, "x").close()

        except FileExistsError:
            pass



def get_integer(prompt):
    """Read an integer from the user, returning None for invalid input."""

    try:
        return int(input(prompt))

    except ValueError:
        print("Ogiltig inmatning.")

        return None




def load_books():
    """Load book records from the books data file."""
    books = []

    with open(BOOKS_FILE, "r") as file:

        for line in file:
            data = line.strip().split(";")

            book = {
                "id": int(data[0]),
                "title": data[1],
                "first_name": data[2],
                "last_name": data[3],
                "loaned": int(data[4])
            }

            books.append(book)

    return books


def save_books(books):
    """Save book records to the books data file."""

    with open(BOOKS_FILE, "w") as file:

        for book in books:

            file.write(
                f"{book['id']};"
                f"{book['title']};"
                f"{book['first_name']};"
                f"{book['last_name']};"
                f"{book['loaned']}\n"
            )


def load_users():
    """Load user records from the users data file."""
    users = []

    with open(USERS_FILE, "r") as file:

        for line in file:
            data = line.strip().split(";")

            user = {
                "id": int(data[0]),
                "first_name": data[1],
                "last_name": data[2],
                "loans": int(data[3])
            }

            users.append(user)

    return users


def save_users(users):
    """Save user records to the users data file."""

    with open(USERS_FILE, "w") as file:

        for user in users:

            file.write(
                f"{user['id']};"
                f"{user['first_name']};"
                f"{user['last_name']};"
                f"{user['loans']}\n"
            )


def load_loans():
    """Load active loan records from the loans data file."""
    loans = []

    with open(LOANS_FILE, "r") as file:

        for line in file:

            data = line.strip().split(";")

            loan = {
                "id": int(data[0]),
                "book_id": int(data[1]),
                "user_id": int(data[2]),
            }

            loans.append(loan)

    return loans


def save_loans(loans):
    """Save active loan records to the loans data file."""

    with open(LOANS_FILE, "w") as file:

        for loan in loans:

            file.write(
                f"{loan['id']};"
                f"{loan['book_id']};"
                f"{loan['user_id']}\n"
            )



def get_next_id(items):
    """Return the next available ID for a collection of records."""

    if not items:
        return 1

    return max(item["id"] for item in items)+1

def pause():
    """Wait for the user before returning to the menu."""
    input("Tryck Enter för att återgå till menyn...")


def find_book(books, book_id):
    """Find and return a book by ID, or None if it is not found."""

    for book in books:

        if book["id"] == book_id:
            return book

    return None


def find_user(users, user_id):
    """Find and return a user by ID, or None if it is not found."""

    for user in users:

        if user["id"] == user_id:
            return user

    return None


def show_menu():
    """Display the available library system menu options."""
    print("==============================")
    print("        LIBRARY SYSTEM")
    print("==============================")
    print()
    print("1. Lista böcker")
    print("2. Lägg till bok")
    print("3. Ta bort bok")
    print("4. Registrera användare")
    print("5. Låna bok")
    print("6. Lämna tillbaka bok")
    print("7. Sök bok")
    print("8. Visa statistik")
    print("9. Exportera rapport")
    print("10. Ta bort användare")
    print("0. Avsluta")
    print()


def get_title(book):
    """Return a book title for use as a sorting key."""
    return book["title"]


def list_books(books):
    """Display books alphabetically, including author and loan status."""

    books = sorted(books, key=get_title)

    print(f"{'ID':<5}{'Titel':<44}{'Författare':<30}{'Status'}")

    for book in books:

        author = f"{book['first_name']} {book['last_name']}".strip()

        if book["loaned"] == 1:
            status = "Utlånad"
        else:
            status = "Tillgänglig"

        print(
            f"{book['id']:<5}"
            f"{book['title']:<44}"
            f"{author:<30}"
            f"{status}"
        )

    pause()


def add_book(books):
    """Add a new book and save the updated book list."""

    title = input("Titel: ")
    first_name = input("Författarens förnamn: ")
    last_name = input("Författarens efternamn: ")

    book_id = get_next_id(books)

    book = {
        "id": book_id,
        "title": title,
        "first_name": first_name,
        "last_name": last_name,
        "loaned": 0
    }

    books.append(book)

    save_books(books)

    print("Boken har lagts till.")
    print(f"ID: {book_id}")

    pause()


def delete_book(books):
    """Delete a book if it exists and is not currently loaned out."""

    book_id = get_integer("Bok-ID: ")

    if book_id is None:
        return

    book = find_book(books, book_id)

    if book is None:
        print("Boken finns inte.")
        pause()
        return

    if book["loaned"] == 1:
        print("Boken är utlånad och kan inte tas bort.")
        pause()
        return

    books.remove(book)

    save_books(books)

    print("Boken har tagits bort.")

    pause()


def register_user(users):
    """Register a new user and save the updated user list."""

    first_name = input("Förnamn: ")
    last_name = input("Efternamn: ")

    user_id = get_next_id(users)

    user = {
        "id": user_id,
        "first_name": first_name,
        "last_name": last_name,
        "loans": 0
    }

    users.append(user)

    save_users(users)

    print("Användaren har registrerats.")
    print(f"ID: {user_id}")

    pause()


def loan_book(books, users, loans):
    """Loan a book after validating the book, user, and borrowing rules."""

    book_id = get_integer("Bok-ID: ")
    if book_id is None:
        return

    user_id = get_integer("Användar-ID: ")
    if user_id is None:
        return

    book = find_book(books, book_id)
    user = find_user(users, user_id)

    if book is None:
        print("Boken finns inte.")
        pause()
        return

    if user is None:
        print("Användaren finns inte.")
        pause()
        return

    if book["loaned"] == 1:
        print("Boken är redan utlånad.")
        pause()
        return

    if user["loans"] >= 5:
        print("Användaren har redan maximalt antal lån.")
        pause()
        return

    loan = {
        "id": get_next_id(loans),
        "book_id": book_id,
        "user_id": user_id
    }

    loans.append(loan)

    book["loaned"] = 1
    user["loans"] += 1

    save_books(books)
    save_users(users)
    save_loans(loans)

    print("Boken har lånats ut.")
    pause()


def return_book(books, users, loans):
    """Return a loaned book and update the related records."""

    book_id = get_integer("Bok-ID: ")
    if book_id is None:
        return

    book = find_book(books, book_id)

    if book is None:
        print("Boken finns inte.")
        pause()
        return

    if book["loaned"] == 0:
        print("Boken är inte utlånad.")
        pause()
        return

    loan = None
    for current_loan in loans:
        if current_loan["book_id"] == book_id:
            loan = current_loan
            break

    if loan is None:
        print("Inget matchande lån hittades.")
        pause()
        return

    user = find_user(users, loan["user_id"])

    if user is None:
        print("Användaren finns inte.")
        pause()
        return

    loans.remove(loan)
    book["loaned"] = 0
    user["loans"] -= 1

    save_books(books)
    save_users(users)
    save_loans(loans)

    print("Boken har återlämnats.")
    pause()


def search_books(books):
    """Search for books by title or author."""

    search_term = input("Sökterm: ").lower()

    found = False

    print(f"{'ID':<5}{'Titel'}")

    for book in books:
        author = f"{book['first_name']} {book['last_name']}"

        if search_term in book["title"].lower() or search_term in author.lower():
            print(f"{book['id']:<5}{book['title']}")
            found = True

    if not found:
        print("Inga böcker hittades.")

    pause()


def create_statistics(books, users, loans):
    """Calculate and format statistics about books, users, and loans."""

    total_books = len(books)
    total_users = len(users)
    active_loans = len(loans)

    loaned_books = sum(book["loaned"] for book in books)
    available_books = total_books - loaned_books

    if users:
        max_loans = max(user["loans"] for user in users)
    else:
        max_loans = 0

    top_users = [user for user in users if user["loans"] == max_loans]

    author_counts = {}

    for book in books:

        author = f"{book['first_name']} {book['last_name']}"

        author_key = author.lower()

        if author_key not in author_counts:
            author_counts[author_key] = {"name": author, "count": 0}

        author_counts[author_key]["count"] += 1

    if author_counts:
        max_author_books = max(
            author["count"] for author in author_counts.values()
        )
    else:
        max_author_books = 0

    top_authors = [
        author["name"]
        for author in author_counts.values()
        if author["count"] == max_author_books
    ]

    lines = []

    lines.append(f"Antal böcker: {total_books}\n")
    lines.append(f"Antal användare: {total_users}\n")
    lines.append(f"Antal aktiva lån: {active_loans}\n")
    lines.append(f"Tillgängliga böcker: {available_books}\n")
    lines.append(f"Utlånade böcker: {loaned_books}\n")

    lines.append("Användare med flest lån:\n")
    for user in top_users:
        name = f"{user['first_name']} {user['last_name']}"
        lines.append(f"{name} ({max_loans})")

    lines.append("\nFörfattare med flest böcker:\n")
    for author in top_authors:
        lines.append(f"{author} ({max_author_books})\n")

    return "\n".join(lines)

def show_statistics(books, users, loans):
    """Display the library statistics."""

    statistics = create_statistics(books, users, loans)

    print(statistics)

    pause()


def export_report(books, users, loans):
    """Export the library statistics to a text report."""

    report_text = create_statistics(books, users, loans)

    with open("report.txt", "w") as file:
        file.write(report_text)

    print("Rapporten exporterad till report.txt")
    pause()


def delete_user(users, loans):
    """Delete a user if they have no active loans."""

    user_id = get_integer("Användar-ID: ")
    if user_id is None:
        return

    user = find_user(users, user_id)

    if user is None:
        print("Användaren finns inte.")
        pause()
        return

    for loan in loans:
        if loan["user_id"] == user_id:
            print("Användaren har aktiva lån och kan inte tas bort.")
            pause()
            return

    users.remove(user)

    save_users(users)

    print("Användaren har tagits bort.")
    pause()

create_files()

books = load_books()
users = load_users()
loans = load_loans()


def main():
    """Run the main menu loop and dispatch the selected action."""

    while True:

        show_menu()

        try:
            choice = int(input("Val: "))
        except ValueError:
            print("Ogiltigt val. Ange en siffra mellan 0 och 10.")
            continue

        if choice == 0:
            print("Programmet avslutas.")
            break

        if choice < 0 or choice > 10:
            print("Ogiltigt val. Ange en siffra mellan 0 och 10.")
            continue

        if choice == 1:
            list_books(books)

        elif choice == 2:
            add_book(books)

        elif choice == 3:
            delete_book(books)

        elif choice == 4:
            register_user(users)

        elif choice == 5:
            loan_book(books, users, loans)

        elif choice == 6:
            return_book(books, users, loans)

        elif choice == 7:
            search_books(books)

        elif choice == 8:
            show_statistics(books, users, loans)

        elif choice == 9:
            export_report(books, users, loans)

        elif choice == 10:
            delete_user(users, loans)


main()
