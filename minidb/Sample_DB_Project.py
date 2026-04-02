import mysql.connector as co
from tabulate import tabulate

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
    print("2. Show Route")
    print("3. Show Foods")
    print("4. Show Parkings")
    print("5. Show Stays")
    print("6. Show Local Guides")
    print("7. Show Emergency Services")
    print("8. Show Garages")
    print("9. Show User Reviews")
    print("10. Exit")

    choice = int(input("\nEnter choice: "))
    if choice in [2,3,4,5,6,7,8,9]:
        destination = input("Enter Destination: ")


    # 1️ Destinations
    if choice == 1:
        cursor.execute("SELECT Destination_ID, Destination_Name, Location FROM Destinations")
        data = cursor.fetchall()
        headers = ["Sr. No.", "Destination", "Location"]

        print("\n--- Destinations ---")
        print(tabulate(data, headers=headers, tablefmt="grid"))
        
        try:
            dest = int(input("\nEnter Destination ID to view details: "))
        except:
            print("❌ Invalid input")
            continue            
        
        cursor.execute("""
			SELECT d.Destination_Name, d.Type ,r.Base,  d.Location, d.Best_Visit_Time, r.Difficulty,f.Food_Name, g.Guide_Name, 
                       g.Conntact_no, h.Hospital_Name, h.Phone, b.Shop_Name , b.Contact_Number 
			FROM Destinations d
			JOIN Food_Places f ON f.Destination_ID = d.Destination_ID
			JOIN Bike_Repair_Shops b ON b.Destination_ID = d.Destination_ID
			JOIN Emergency_Services h ON h.Destination_ID = d.Destination_ID
			JOIN Guides g ON g.Destination_ID = d.Destination_ID
			JOIN Routes r ON r.Destination_ID = d.Destination_ID
            WHERE d.Destination_ID = %s
            """, (dest,))
        result = cursor.fetchall()

        if not result:
            print("❌ No data found for this destination")
        else:
            headers = [
                 "Destination_Name", "Type", "Base Village","Location","Best Visit Time", "Difficulty",
                "Food Places", "Guide Name", "Contact No",
                 "Hospital Name", "Phone", "Shop Name", "Contact No"
            ]
            print("\n--- Destination Details ---")
            print(tabulate(result, headers=headers, tablefmt="grid"))

	#2 Routes
    if choice == 2:
        cursor.execute("""
		SELECT t.Base, t.Distance_KM, t.Difficulty, d.Destination_Name
		FROM Routes t
		JOIN Destinations d ON t.Destination_ID = d.Destination_ID
		WHERE d.Destination_Name = %s
		""", (destination,))
        
        result = cursor.fetchall()
        headers = [" Start From","Distance (km)","Difficulty","Location"] 
        print("\n---Trek Route---\n")
        print(tabulate(result, headers=headers, tablefmt="grid"))
		
		
	# 3 Food
    if choice == 3:
        cursor.execute("""
		SELECT f.Food_ID, f.Food_Name, f.Rating, f.Price_Range, d.Destination_Name
		FROM Food_Places f
		JOIN Destinations d ON f.Destination_ID = d.Destination_ID
		WHERE d.Destination_Name = %s
		""", (destination,))
        
        result = cursor.fetchall()
        headers = ["Sr.No.","Food","Rating","PriceRange","Location"] 
        print("\n---Food Places---\n")
        print(tabulate(result, headers=headers, tablefmt="grid"))
		
	# 4 Parking
    if choice == 4:
        cursor.execute("""
		SELECT p.Parking_ID, p.Paid_Free, p.Capacity, p.Security_Level, p.Contact_No, d.Destination_Name
		FROM Parking_Spots p
		JOIN Destinations d ON p.Destination_ID = d.Destination_ID
		WHERE d.Destination_Name = %s
		""", (destination,))
        
        result = cursor.fetchall()
        headers = ["Parking ID","Paid/Free","Capacity","Security","Contact", "Location"] 
        print("\n---Parking Spots---\n")
        print(tabulate(result, headers=headers, tablefmt="grid"))
		
	#5 Stays
    if choice == 5:
        cursor.execute("""
		SELECT s.Stay_Name ,s.Address, s.Contact_No, s.Rating, d.Destination_Name
		FROM Stays s
		JOIN Destinations d ON s.Destination_ID = d.Destination_ID
		WHERE d.Destination_Name = %s
		""", (destination,))
        
        result = cursor.fetchall()
        headers = ["Stay Name","Address","Contact","Rating", "Location"] 
        print("\n--- Stays ---\n")
        print(tabulate(result, headers=headers, tablefmt="grid"))
		
	#6 Loacal Guides	
    if choice == 6:
        cursor.execute("""
		SELECT g.Guide_Name, g.Conntact_No, d.Destination_Name
		FROM Guides g
		JOIN Destinations d ON g.Destination_ID = d.Destination_ID
		WHERE d.Destination_Name = %s
		""", (destination,))
        
        result = cursor.fetchall()
        headers = [" Guide Name","Contact No","Location"] 
        print("\n---Local Guides---\n")
        print(tabulate(result, headers=headers, tablefmt="grid"))
		
	#7 Emergency Services
    if choice == 7:
        cursor.execute("""
		SELECT h.Hospital_Name, h.Phone, d.Destination_Name
		FROM Emergency_Services h
		JOIN Destinations d ON h.Destination_ID = d.Destination_ID
		WHERE d.Destination_Name = %s
		""", (destination,))
        
        result = cursor.fetchall()
        headers = ["Hospital Name","Contact", "Location"] 
        print("\n---Emergency Services---\n")
        print(tabulate(result, headers=headers, tablefmt="grid"))
	
		
	#8 Garrage
    if choice == 8:
        cursor.execute("""
		SELECT b.Shop_Name, b.Contact_Number, d.Destination_Name
		FROM Bike_Repair_Shops b
		JOIN Destinations d ON b.Destination_ID = d.Destination_ID
		WHERE d.Destination_Name = %s
		""", (destination,))
        
        result = cursor.fetchall()
        headers = ["Shop Name.","Contact No","Location"] 
        print("\n--- Garrages ---\n")
        print(tabulate(result, headers=headers, tablefmt="grid"))
		

		
	#9 Past User Review
    if choice == 9:
        cursor.execute("""
		SELECT d.Destination_Name , r.Comment, r.Rating
		FROM Reviews r
		JOIN Destinations d ON r.Destination_ID = d.Destination_ID
		WHERE d.Destination_Name = %s
		""", (destination,))
        
        result = cursor.fetchall()
        headers = ["Location","Comment","Rating"] 
        print("\n---Past User Reviews---\n")
        print(tabulate(result, headers=headers, tablefmt="grid"))
    
    #10
    # Exit
    elif choice == 10:
        print("\n\tTHANK YOU \n\tExiting system...")
        break

    else:
        print("\nInvalid choice!")

conn.close()