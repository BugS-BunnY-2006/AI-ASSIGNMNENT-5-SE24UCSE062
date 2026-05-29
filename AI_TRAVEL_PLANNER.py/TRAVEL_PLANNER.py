
# AI BASED TRAVEL PLANNER
#
# Uses:
# 1. Tourist Place Knowledge Base
# 2. Food Recommendation Knowledge Base
# 3. Hotel Knowledge Base
# 4. Cost Assessment Module
# 5. User Preference Matching
# =====================================================

tourist_places = {
    "Hyderabad": {
        "Historical": ["Charminar", "Golconda Fort", "Salar Jung Museum"],
        "Nature": ["Nehru Zoological Park", "Hussain Sagar Lake"],
        "Adventure": ["Wonderla", "Ramoji Film City"]
    },

    "Jaipur": {
        "Historical": ["Amber Fort", "Hawa Mahal", "City Palace"],
        "Nature": ["Jal Mahal"],
        "Adventure": ["Hot Air Balloon Ride"]
    }
}


food_recommendations = {
    "Hyderabad": [
        "Hyderabadi Biryani",
        "Double Ka Meetha",
        "Haleem"
    ],

    "Jaipur": [
        "Dal Baati Churma",
        "Ghewar",
        "Kachori"
    ]
}


hotels = {
    "Hyderabad": {
        "Budget": 1500,
        "Standard": 3000,
        "Luxury": 6000
    },

    "Jaipur": {
        "Budget": 1200,
        "Standard": 2500,
        "Luxury": 5000
    }
}


def recommend_hotel(budget):

    if budget < 10000:
        return "Budget"

    elif budget < 30000:
        return "Standard"

    else:
        return "Luxury"


def generate_plan(city,
                  budget,
                  days,
                  interest):

    print("\n===================================")
    print(" PERSONALIZED TRAVEL PLAN")
    print("===================================\n")

    print("Destination :", city)
    print("Duration    :", days, "Days")
    print("Interest    :", interest)

    hotel_type = recommend_hotel(budget)

    hotel_cost = hotels[city][hotel_type] * days

    print("\nRecommended Hotel Type :", hotel_type)

    print("\nPlaces To Visit:")

    places = tourist_places[city][interest]

    for place in places:
        print("-", place)

    print("\nRecommended Local Foods:")

    for food in food_recommendations[city]:
        print("-", food)

    food_cost = days * 500
    travel_cost = days * 1000

    total_cost = (
        hotel_cost +
        food_cost +
        travel_cost
    )

    print("\nEstimated Cost")

    print("Hotel Cost  : ₹", hotel_cost)
    print("Food Cost   : ₹", food_cost)
    print("Travel Cost : ₹", travel_cost)

    print("--------------------------")
    print("Total Cost  : ₹", total_cost)

    if total_cost <= budget:
        print("\nStatus : Within Budget")
    else:
        print("\nStatus : Budget Exceeded")


# ==========================
# USER INPUT
# ==========================

city = input("Enter Destination City: ")

budget = int(
    input("Enter Budget (₹): ")
)

days = int(
    input("Enter Number of Days: ")
)

interest = input(
    "Enter Interest "
    "(Historical/Nature/Adventure): "
)

generate_plan(
    city,
    budget,
    days,
    interest
)

Sample Input:
#
Destination City : Hyderabad

Budget : 20000

Days : 3

Interest : Historical


Sample Output:
#
PERSONALIZED TRAVEL PLAN

Destination : Hyderabad
Duration : 3 Days
Interest : Historical

Recommended Hotel Type : Standard

Places To Visit:

- Charminar
- Golconda Fort
- Salar Jung Museum

Recommended Local Foods:

- Hyderabadi Biryani
- Double Ka Meetha
- Haleem

Estimated Cost

Hotel Cost  : ₹9000
Food Cost   : ₹1500
Travel Cost : ₹3000

Total Cost  : ₹13500

Status : Within Budget
