def currency_converter():
    rates = {
        'USD': 1.0,
        'EUR': 0.91,
        'GBP': 0.79,
        'NGN': 775.0,
        'JPY': 144.0,
        'CAD': 1.35
    }

    print('supported currences', ", ".join(rates.keys()))

    while True:
        try:
            amount = float(input("Enter the amount to convert: "))
            from_currency = input("From currency (e.g USD): ").upper()
            to_currency = input("To currency (e.g EUR): ").upper()

            if from_currency not in rates or to_currency not in rates:
                print("Invalid Currency code, Try again Please")
                continue

            amount_in_usd = amount / rates[from_currency]
            converted_amount = amount_in_usd * rates[to_currency]
            print(
                f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")

            again = input(
                "Do you want to convert another amount? (yes/no): ").lower()
            if again != 'yes':
                print("Thank you for using the currency converter!")
                break

        except ValueError:
            print("Invalid amount. Please enter a number.")


currency_converter()
