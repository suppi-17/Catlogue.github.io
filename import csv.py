import csv
import webbrowser

def load_products(filename):
    products = []
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
         products.append(row)
    return products

def display_catalogue(products):
    print("Spare Parts Catalogue")
    print("----------------------")
    for index, product in enumerate(products):
        print(f"ID: {product['id']}")
        print(f"Name: {product['name']}")
        print(f"Description: {product['description']}")
        print(f"Price: {product['price']}")
        print(f"Image Link: {product['image_link']}")
        print(f"Part Link: {product['C:\Users\s8513154\description.html']})
        print("----------------------")
     # user for a product ID to view more details
    selected_id = input("Enter the ID of the part you want to view (or 'exit' to quit): ")
    return selected_id

def open_links(products, selected_id):
    for product in products:
        if product['id'] == selected_id:
            print(f"Opening image link: {product['C:\Users\s8513154\description.html']})
            webbrowser.open(product['image_link'])
            print(f"Opening part link: {product['part_link']}")
            webbrowser.open(product['part_link'])
            return
    print("Invalid ID. Please try again.")
    