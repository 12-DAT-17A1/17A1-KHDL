"""def party_late(arrivals, name):
    if name in arrivals:
        index = arrivals.index(name)
        if index < len(arrivals) - 1:
            return True  # Nếu tên người tham gia đã đến và không phải là người cuối cùng đến, coi là đến muộn
    return False  # Ngược lại, coi là không đến muộn

# Ví dụ sử dụng:
guest_arrivals = ["Alice", "Bob", "Charlie", "David", "Eve"]
specific_name = "Charlie"
if party_late(guest_arrivals, specific_name):
    print(f"{specific_name} đã đến muộn.")
else:
    print(f"{specific_name} không đến muộn.")
"""
