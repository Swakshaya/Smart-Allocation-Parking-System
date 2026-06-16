import heapq

# =====================================================
# PARKING SLOT DATABASE
# =====================================================

parking_slots = {
    "A1": {"type": "Car", "status": "Free", "distance": 2},
    "A2": {"type": "Car", "status": "Occupied", "distance": 4},
    "A3": {"type": "Car", "status": "Free", "distance": 1},
    "B1": {"type": "Bike", "status": "Free", "distance": 5},
    "B2": {"type": "Bike", "status": "Occupied", "distance": 2},
    "C1": {"type": "Truck", "status": "Free", "distance": 3},
}

# =====================================================
# HEURISTIC FUNCTION
# =====================================================

def heuristic(slot):
    return parking_slots[slot]["distance"]

# =====================================================
# CSP VALIDATION
# =====================================================

def is_valid(slot, vehicle_type):
    if parking_slots[slot]["status"] != "Free":
        return False

    if parking_slots[slot]["type"] != vehicle_type:
        return False

    return True

# =====================================================
# SLOT RECOMMENDATION
# =====================================================

def recommend_slot(vehicle_no, vehicle_type):
    possible_slots = []

    for slot in parking_slots:
        if is_valid(slot, vehicle_type):
            cost = heuristic(slot)
            heapq.heappush(possible_slots, (cost, slot))

    if len(possible_slots) == 0:
        return "No Parking Slot Available"

    best_slot = heapq.heappop(possible_slots)[1]
    parking_slots[best_slot]["status"] = "Reserved"

    return f"AI Recommended Slot: {best_slot}"

# =====================================================
# DISPLAY PARKING STATUS
# =====================================================

def display_parking_slots():
    print("\n===== PARKING SLOT STATUS =====")

    for slot, details in parking_slots.items():
        print(
            f"{slot} | Type: {details['type']} | "
            f"Status: {details['status']} | "
            f"Distance: {details['distance']}"
        )

# =====================================================
# MAIN PROGRAM
# =====================================================

if __name__ == "__main__":

    print("======================================")
    print("  ParkAI - Automated Parking System")
    print("======================================")

    display_parking_slots()

    vehicle_no = input("\nEnter Vehicle Number: ")
    vehicle_type = input("Enter Vehicle Type (Car/Bike/Truck): ").title()

    result = recommend_slot(vehicle_no, vehicle_type)

    print("\n" + result)

    display_parking_slots()
