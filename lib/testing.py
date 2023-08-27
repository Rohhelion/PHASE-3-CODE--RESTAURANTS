from customer import Customer
from restaurant import Restaurant
from review import Review

# Create some customers
customer1 = Customer("Roy", "Kip")
customer2 = Customer("Brian", "James")
customer3 = Customer("Mary", "Jane")
customer4 = Customer("Randy", "Rick")

# Create some restaurants
restaurant1 = Restaurant("Dairoy's")
restaurant2 = Restaurant("Comora center")

# Add reviews using the add_review method
customer1.add_review(restaurant1, 4)  # Customer1 reviews restaurant1 with a rating of 4
customer2.add_review(restaurant2, 5)  # Customer2 reviews restaurant2 with a rating of 5
customer3.add_review(restaurant1, 9)
customer4.add_review(restaurant2, 10)

# Write new reviews using the add_review method
#customer1.add_review(restaurant1, 5)  # New review for restaurant1 by customer1
#customer2.add_review(restaurant2, 2)  # New review for restaurant2 by customer2

# Test methods
print(customer1.full_name())
print(restaurant1.name)
print(customer1.reviews[0].rating)  # Print the rating of the first review for customer1

# Print all reviews for each customer and restaurant
for customer in Customer.all():
    print(f"{customer.full_name()} reviews:")
    for review in customer.reviews:
        print(f"   - {review.restaurant.name}: {review.rating}")

for restaurant in Restaurant.all():
    print(f"{restaurant.name} reviews:")
    for review in restaurant.reviews:
        print(f"   - {review.customer.full_name()}: {review.rating}")

# Test class methods
all_customers = Customer.all()
all_restaurants = Restaurant.all()
all_reviews = Review.all()

print("All Customers:")
for customer in all_customers:
    print(f"   - {customer.full_name()}")

print("All Restaurants:")
for restaurant in all_restaurants:
    print(f"   - {restaurant.name}")

print("All Reviews:")
for review in all_reviews:
    print(f"   - {review.customer.full_name()} reviewed {review.restaurant.name} with a rating of {review.rating}")
