import mysql.connector as co

conn = co.connect(
    host="localhost",
    user="root",
    password="2503",
    database="travel_system"
)

cursor = conn.cursor()

print("Connected successfully!")

while True:
    print("\n\n==== SMART TRAVEL SYSTEM ====\n")
    print("1. Show Destinations")
    print("2. Show Food Places")
    print("3. Show Nearby Parking ")
    print("4. Show Emergency Services")
    print("5. Show Local Guides")
    print("6. Show Reviews")
    print("7. Show Nearby Garages")
    print("8. Show Routes")
    #print("9. Show Stays")
    #print("10. Apply Default Filters")
    print("11. Exit")

    choice = int(input("\nEnter choice: "))

    # 1️⃣ Destinations
    if choice == 1:
        cursor.execute("SELECT Destination_Name, Location FROM Destinations")
        for row in cursor.fetchall():
            print("\nDestination:", row[0], "| Location:", row[1])

    # 2️⃣ Food Places
    elif choice == 2:
        cursor.execute("""
        SELECT f.Food_Name, f.Rating, d.Destination_Name
        FROM Food_Places f
        JOIN Destinations d ON d.Destination_ID = d.Destination_ID
        """)
        for row in cursor.fetchall():
            print("\nFood:", row[0], "| Rating:", row[1], "| Destination:", row[2])
			
	

    # 3️⃣ Parking
    elif choice == 3:
        cursor.execute("""
        SELECT p.Security_Level, p.Paid_Free, d.Destination_Name
        FROM Parking_Spots p
        JOIN Destinations d ON p.Destination_ID = d.Destination_ID
        """)
        for row in cursor.fetchall():
            print("\nDestination:", row[2], "| Security:", row[0], "| Type:", row[1])

    # 4️⃣ Emergency
    elif choice == 4:
        cursor.execute("""
        SELECT e.Hospital_Name, e.Phone, d.Destination_Name
        FROM Emergency_Services e
        JOIN Destinations d ON e.Destination_ID = d.Destination_ID
        """)
        for row in cursor.fetchall():
            print("\nHospital:", row[0], "| Phone:", row[1], "| Destination:", row[2])

    # 5️⃣ Guides
    elif choice == 5:
        cursor.execute("""
        SELECT g.Guide_Name, g.Conntact_No, d.Destination_Name
        FROM Guides g
        JOIN Destinations d ON g.Destination_ID = d.Destination_ID
        """)
        for row in cursor.fetchall():
            print("\nGuide:", row[0], "| Contact:", row[1], "| Destination:", row[2])

    # 6️⃣ Reviews
    elif choice == 6:
        cursor.execute("""
        SELECT u.Name, r.Rating, r.Comment, d.Destination_Name
        FROM Reviews r
        JOIN Users u ON r.User_id = u.User_id
        JOIN Destinations d ON r.Destination_ID = d.Destination_ID
        """)
        for row in cursor.fetchall():
            print("\nUser:", row[0], "| Rating:", row[1], "| Review:", row[2], "| Destination:", row[3])

    # 7️⃣ Garages
    elif choice == 7:
        cursor.execute("""
        SELECT b.Shop_Name, b.Contact_Number, d.Destination_Name
        FROM Bike_Repair_Shops b
        JOIN Destinations d ON b.Destination_ID = d.Destination_ID
        """)
        for row in cursor.fetchall():
            print("\nGarage:", row[0], "| Contact:", row[1], "| Destination:", row[2])

    # 8️⃣ Routes
    elif choice == 8:
        cursor.execute("""
        SELECT r.Source, r.Distance_KM, r.Difficulty, d.Destination_Name
        FROM Routes r
        JOIN Destinations d ON r.Destination_ID = d.Destination_ID
        """)
        for row in cursor.fetchall():
            print("\nFrom:", row[0], "| Distance:", row[1], "| Difficulty:", row[2], "| Destination:", row[3])

    # 9️⃣ Stays (if table exists)
    elif choice == 9:
        cursor.execute("""
        SELECT s.Stay_Name, s.Price, d.Destination_Name
        FROM Stays s
        JOIN Destinations d ON s.Destination_ID = d.Destination_ID
        """)
        for row in cursor.fetchall():
            print("\nStay:", row[0], "| Price:", row[1], "| Destination:", row[2])

    # 🔟 Default Filter
    elif choice == 10:
        print("\n--- Apply Filters ---")
        destination = input("Enter destination: ")
        rating = float(input("Minimum rating: "))
        price = input("Price range (Low/Medium/High): ")

        cursor.execute("""
        SELECT d.Destination_Name, f.Food_Name, f.Rating, f.Price_Range
        FROM Destinations d
        JOIN Food_Places f ON d.Destination_ID = f.Destination_ID
        WHERE d.Destination_Name = %s
        OR f.Rating >= %s
        OR f.Price_Range = %s
        """, (destination, rating, price))

        for row in cursor.fetchall():
            print("Destination:", row[0],
                  "| Food:", row[1],
                  "| Rating:", row[2],
                  "| Price:", row[3])

    # Exit
    elif choice == 11:
        print("\nExiting system...")
        break

    else:
        print("\nInvalid choice!")

conn.close()