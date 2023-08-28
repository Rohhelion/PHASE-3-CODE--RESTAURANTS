# Object Relations Code Challenge - Restaurants

## Introduction

Welcome to the Object Relations Code Challenge - Restaurants project! In this project, we'll be building a Yelp-style domain to manage information about restaurants, customers, and reviews. The goal is to practice object-oriented programming concepts using Python.

## Project Overview

In this project, we have three main models:

- `Restaurant`: Represents a restaurant and has a one-to-many relationship with `Review`.
- `Customer`: Represents a customer and has a one-to-many relationship with `Review`.
- `Review`: Represents a review given by a customer for a specific restaurant.

## Class Definitions

### `Customer`

- Properties:
  - `given_name`: The given name of the customer.
  - `family_name`: The family name of the customer.
  - `reviews`: A list of reviews written by the customer.
  
- Methods:
  - `__init__(self, given_name, family_name)`: Initializes a new `Customer` instance.
  - `full_name(self)`: Returns the full name of the customer.
  - `add_review(self, restaurant, rating)`: Adds a review for a restaurant.
  - `restaurants(self)`: Returns a unique list of restaurants reviewed by the customer.
  - `num_reviews(self)`: Returns the total number of reviews authored by the customer.
  - `find_by_name(cls, name)`: Returns the first customer with a matching full name.
  - `find_all_by_given_name(cls, name)`: Returns a list of customers with a matching given name.
  - `all()`: Returns a list of all customer instances.

### `Restaurant`

- Properties:
  - `name`: The name of the restaurant.
  
- Methods:
  - `__init__(self, name)`: Initializes a new `Restaurant` instance.
  - `reviews(self)`: Returns a list of all reviews for the restaurant.
  - `customers(self)`: Returns a unique list of customers who reviewed the restaurant.
  - `average_star_rating(self)`: Returns the average star rating for the restaurant.
  - `all()`: Returns a list of all restaurant instances.

### `Review`

- Properties:
  - `customer`: The customer who wrote the review.
  - `restaurant`: The restaurant being reviewed.
  - `rating`: The rating given in the review.
  
- Methods:
  - `__init__(self, customer, restaurant, rating)`: Initializes a new `Review` instance.
  - `customer(self)`: Returns the customer object associated with the review.
  - `restaurant(self)`: Returns the restaurant object associated with the review.
  - `all()`: Returns a list of all review instances.

## Usage

To use the project, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using the provided Pipfile.
4. Define the classes in the corresponding Python files: `customer.py`, `restaurant.py`, and `review.py`.
5. Run the `testing.py` script to test the implemented features. This script creates instances of customers and restaurants, adds reviews, and displays information about the created objects.

## Contributing

Feel free to contribute to this project by forking the repository and submitting pull requests with your improvements.

## License

This project is licensed under the MIT License. You're free to use, modify, and distribute it as needed.

