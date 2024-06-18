def load_menu_from_file(filename):
    menu = {}
    with open(filename, 'r') as file:
        for line in file:
            item, price = line.strip().split(',')
            menu[item] = float(price)
    return menu

def load_all_menus():
    menus = {}
    menus['fruits'] = load_menu_from_file('fruits.txt')
    menus['vegetables'] = load_menu_from_file('vegetables.txt')
    menus['groceries'] = load_menu_from_file('groceries.txt')
    return menus
def input_items(menus):
    items = []
    while True:
        print("\nCategories: Fruits, Vegetables, Groceries")
        category = input("Enter category (or 'done' to finish): ").lower()
        if category == 'done':
            break
        if category in menus:
            menu = menus[category]
            print(f"\n{category.capitalize()} Menu:")
            for item_name, price in menu.items():
                print(f"{item_name}: ${price:.2f}")

            item_name = input("\nEnter item name (or 'done' to finish): ")
            if item_name.lower() == 'done':
                break
            if item_name in menu:
                quantity = int(input(f"Enter quantity for {item_name}: "))
                items.append((item_name, quantity, menu[item_name]))
            else:
                print("Item not found in the menu. Please try again.")
        else:
            print("Category not found. Please try again.")
    return items
def calculate_total(items):
    total = 0
    for item in items:
        item_name, quantity, price = item
        total += quantity * price
    return total

def calculate_gst(total, gst_rate=0.18):
    return total * gst_rate

def calculate_final_total(total, gst):
    return total + gst
def generate_receipt(items, total, gst, final_total, customer_email):
    receipt_content = "Supermarket Receipt\n"
    receipt_content += "====================\n"
    for item in items:
        item_name, quantity, price = item
        receipt_content += f"{item_name} x{quantity} @ ${price:.2f} each: ${quantity * price:.2f}\n"
    receipt_content += "====================\n"
    receipt_content += f"Total: ${total:.2f}\n"
    receipt_content += f"GST (18%): ${gst:.2f}\n"
    receipt_content += f"Final Total: ${final_total:.2f}\n"
    
    filename = "receipt.txt"
    with open(filename, 'w') as file:
        file.write(receipt_content)
    
    return filename
def display(receipt_filename):
    f=open(receipt_filename,"r")
    print(f.read())
    
import smtplib
def send_email(receipt_filename,customer_email):
    try: 
        f=open(receipt_filename,"r")
        bill=f.read()
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login("atchayaananth2005@gmail.com","olgg nbpz khpm vjdx") 
        message=(f"Your purchaseing bill is {bill} \n Thankyou for visiting our Supermarket")
        s.sendmail("atchayaananth2005@gmail.com",customer_email,message)
        s.quit()
        print("Mail sent successfully")
          
    except: 
        print("Mail not sent")
# Replace with your SMTP server details and credentials
def main():
    menus = load_all_menus()
    items = input_items(menus)
    total = calculate_total(items)
    gst = calculate_gst(total)
    final_total = calculate_final_total(total, gst)
    customer_email = input("Enter customer email: ")
    receipt_filename = generate_receipt(items, total, gst, final_total, customer_email)
    display(receipt_filename)
    send_email(receipt_filename, customer_email)

if __name__ == "__main__":
    main()
