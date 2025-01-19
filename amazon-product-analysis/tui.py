import ai

print("\nWelcome to the Amazon Product Description Generator!")
print("\nThis tool is designed to help you create optimized product listings for Amazon.")
print("Simply provide a searchable product title and a brief description of your item.")
print("\nThe generator will:")
print("1. Scrape Amazon's top products related to your search.")
print("2. Analyze product titles, descriptions, prices, and SEO keywords.")
print("3. Generate five optimized product titles, descriptions, prices, and SEO keyword suggestions tailored to your product.")
print("\nLet's get started!")

while (1):
    user_input = input(
        "Do you want to generate a new product description? [y/n]\n")
    if user_input == "y":
        title = input("Enter a Product Title\n")
        description = input("Enter a Product Description\n")
        response = ai.suggestion_gen(title, description)
        ai.print_response(response)

    elif user_input == "n":
        user_input = input("Do you want to exit? [y/n]\n")
        if user_input == "y":
            break
        elif user_input == "n":
            pass
        else:
            print("Invalid Input\n")
            pass
    else:
        print("Invalid Input\n")
        pass
