import datetime

logs = []  
parked = []  
MAX_SLOTS = 30

def main():
        while True:
            print("=== VEHICLE PARKING SYSTEM ===")
            print("1. Parking Attendant")
            print("2. Security Supervisor")

            role_choice = input("Enter choice (1-2): ")
            
            if role_choice == "1":
                result = parking_attendant_menu()
                if result == "switch":
                    continue

            elif role_choice == "2":
                result = security_supervisor_menu()
                if result == "switch":
                    continue

            else:
                print("Access denied. Unknown role entered.")

def parking_attendant_menu():
        while True:
            print("--- PARKING ATTENDANT MENU ---")
            print("1. Time In Vehicle")
            print("2. Time Out Vehicle")
            print("3. Back to Role Menu")
            print("4. Exit System")

            choice = input("Enter choice (1-4): ")

            if choice == "1":

                occupied = 0
                for v in parked:
                    occupied += 1

                if occupied >= MAX_SLOTS:
                    print("Parking is FULL. No available slots.")
                    continue

                plate = input("Enter vehicle plate number: ").upper()
                
                for v in parked:
                    if v == plate:
                        print("Error: Vehicle is already inside.")
                        break
                else:
                    parked.append(plate)

                    time_in = datetime.datetime.now().strftime("%m/%d/%Y %I:%M %p")
                    record = f"[TIME IN] {plate} at {time_in}"
                    logs.append(record)
                    print(record)
        
        
            elif choice == "2":
                plate = input("Enter vehicle plate number: ").upper()

                found = False
                for v in parked:
                    if v == plate:
                        found = True
                        break

                if not found:
                    print("Error: Vehicle not found inside. Please time in first.")
                    continue  

                parked.remove(plate)

                time_out = datetime.datetime.now().strftime("%m/%d/%Y %I:%M %p")
                record = f"[TIME OUT] {plate} at {time_out}"
                logs.append(record)
                print(record)

            elif choice == "3":
                return "switch"

            elif choice == "4":
                print("Exiting system... Thankyou!")
                exit()

            else:
                print("Invalid choice. Try again.")

def security_supervisor_menu():
        while True:
            print("--- SECURITY SUPERVISOR MENU ---")
            print("1. View Vehicle Logs")
            print("2. Generate Report")
            print("3. Back to Role Menu")
            print("4. Exit System")

            choice = input("Enter choice (1-4): ")

            if choice == "1":
                print("=== VEHICLE LOGS ===")
                if not logs:
                    print("No logs available yet.")
                else:
                    for log in logs:
                        print(log)

            elif choice == "2":
                print("Generating report...")

                total_in = 0
                total_out = 0

                for log in logs:
                    if "TIME IN" in log:
                        total_in += 1
                    elif "TIME OUT" in log:
                        total_out += 1

                print(f"Total Vehicles Time In: {total_in}")
                print(f"Total Vehicles Time Out: {total_out}")

                occupied = 0
                for v in parked:
                    occupied += 1

                print("Current Occupied Slots:", occupied)
                print("Available Slots:", MAX_SLOTS - occupied)

                print("Report generated successfully.")

            elif choice == "3":
                return "switch"

            elif choice == "4":
                print("Exiting system... Thankyou!")
                exit()

            else:
                print("Invalid choice. Try again.")

main()