class Donor:
    def __init__(self, donor_id, name, contact_number, blood_group, prev_donated_month, away_from):
        self.donor_id = donor_id
        self.name = name
        self.contact_number = contact_number
        self.blood_group = blood_group
        self.prev_donated_month = prev_donated_month
        self.away_from = away_from


class BloodBank:
    def __init__(self, name, list_of_donors):
        self.name = name
        self.list_of_donors = list_of_donors

    def getListofAvailableDonors(self):
        available_donors = {}
        current_month = "Nov"  # Current month as per the problem statement (November)

        for donor in self.list_of_donors:
            # Check if the donor satisfies the conditions to be considered available
            if current_month not in donor.prev_donated_month and donor.away_from <= 50:
                if donor.blood_group in available_donors:
                    available_donors[donor.blood_group] += 1
                else:
                    available_donors[donor.blood_group] = 1

        return dict(sorted(available_donors.items()))

    def getAndUpdateDonor(self, blood_group, required_count):
        available_donors = []
        current_month = "Nov"  # Current month as per the problem statement (November)

        for donor in self.list_of_donors:
            if donor.blood_group == blood_group and current_month not in donor.prev_donated_month and donor.away_from <= 50:
                available_donors.append(donor)

        if len(available_donors) >= required_count:
            for i in range(required_count):
                available_donors[i].prev_donated_month = current_month
            return True
        else:
            return False


# Main Section
if __name__ == "__main__":
    num_donors = int(input())
    list_of_donors = []

    for _ in range(num_donors):
        donor_id = int(input())
        name = input()
        contact_number = int(input())
        blood_group = input()
        prev_donated_month = input()
        away_from = int(input())
        donor = Donor(donor_id, name, contact_number, blood_group, prev_donated_month, away_from)
        list_of_donors.append(donor)

    blood_bank = BloodBank("MyBloodBank", list_of_donors)

    blood_group = input()
    required_count = int(input())

    available_donors_before = blood_bank.getListofAvailableDonors()
    for blood, count in available_donors_before.items():
        print(f"{blood} {count}")

    if blood_bank.getAndUpdateDonor(blood_group, required_count):
        print("Donor count available")
    else:
        print("Donor count not available")

    available_donors_after = blood_bank.getListofAvailableDonors()
    for blood, count in available_donors_after.items():
        print(f"{blood} {count}")
