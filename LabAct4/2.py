import csv

def load_exchange_rates(filename):
    rates = {}
    try:
        with open(filename, newline='', encoding='latin-1') as file:  # Changed encoding to latin-1
            reader = csv.DictReader(file)
            for row in reader:
                rates[row["code"].strip().upper()] = float(row["rate"])  # Store rate by code
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except UnicodeDecodeError:
        print("Error: Unable to decode file. Try opening and re-saving it as UTF-8.")
        return None
    return rates

# Make sure the file path is correct
filename = r"C:\Users\nicol\Desktop\IT0011_Choy\LabAct4\currency.csv"
exchange_rates = load_exchange_rates(filename)

if exchange_rates:
    try:
        amount = float(input("How much dollar do you have? "))
        currency_code = input("What currency you want to have? ").strip().upper()

        if currency_code in exchange_rates:
            converted_amount = amount * exchange_rates[currency_code]
            print(f"{amount} USD is equivalent to {converted_amount:.2f} {currency_code}")
        else:
            print("Currency code not found in the exchange rates.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the amount.")