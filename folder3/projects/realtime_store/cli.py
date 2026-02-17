from scrapper.scrape import scrape_all_categories
from database.insert import insert_products
from database.operations import (
    search_products,
    filter_by_price,
    filter_by_rating,
    get_stats,
    get_categories,
    sort_by_price
)

def main():
    while True:
        print("\n====== PRODUCT ENGINE ======")
        print("1. Update database from website")
        print("2. Search product")
        print("3. Filter by price")
        print("4. Filter by rating")
        print("5. Show statistics")
        print("6. Show categories")
        print("7. Sort by price")
        print("8. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            data = scrape_all_categories()
            insert_products(data)

        elif choice == "2":
            keyword = input("Enter keyword: ")
            results = search_products(keyword)
            print(results)

        elif choice == "3":
            max_price = float(input("Enter max price: "))
            results = filter_by_price(max_price)
            print(results)

        elif choice == "4":
            rating = int(input("Minimum rating: "))
            results = filter_by_rating(rating)
            print(results)

        elif choice == "5":
            stats = get_stats()
            print(stats)

        elif choice == "6":
            categories = get_categories()
            print(categories)

        elif choice == "7":
            order = input("asc or desc: ")
            results = sort_by_price(order)
            print(results)

        elif choice == "8":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
