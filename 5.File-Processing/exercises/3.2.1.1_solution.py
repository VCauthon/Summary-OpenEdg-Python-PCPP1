import csv
from dataclasses import dataclass
import os
from typing import List


@dataclass
class PhoneContact:
    name: str
    phone: str

    def __str__(self) -> str:
        return f"{self.name}{self.phone}"


class Phone:
    def __init__(self, initial_load: str) -> None:
        self.contacts: List[PhoneContact] = []
        self.load_contacts_from_csv(initial_load)

    def load_contacts_from_csv(self, path: str) -> None:
        # Loads the contacts from a CSV into contacts

        new_contacts = set()
        csv_header_name = "Name"
        csv_phone_name = "Phone"

        try:
            with open(path, newline="") as file:
                data = csv.DictReader(file)

                # Only loads the users that don't exist in contacts
                none_existing_users = [
                    con
                    for con in data
                    if not self.search_contacts(
                        f"{con.get(csv_header_name)}{con.get(csv_phone_name)}"
                    )
                ]

                # Imports all new contacts into the phone agenda
                for contact in none_existing_users:
                    new_contact = PhoneContact(
                        name=contact.get(csv_header_name),
                        phone=contact.get(csv_phone_name),
                    )

                    # Ensures that the imported csv doesn't have duplicated contacts
                    if str(new_contact) not in new_contacts:
                        new_contacts.add(str(new_contact))
                        self.contacts.append(new_contact)

        except FileNotFoundError:
            print(f"Error: The file {path} was not found.")

    def search_contacts(
        self, keyword: str, display_contacts=False
    ) -> List[PhoneContact]:
        matching_contacts = [cont for cont in self.contacts if keyword in str(cont)]

        if display_contacts:
            self.__display_contacts(matching_contacts)

        return matching_contacts

    def __display_contacts(self, displayed_contacts: List[PhoneContact]) -> None:
        for cont in displayed_contacts:
            print(f"{cont.name} ({cont.phone})")
        if not displayed_contacts:
            print("No contacts found")


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    my_phone = Phone("../persistance/contacts.csv")

    print("First search".center(50, "*"))
    my_phone.search_contacts(keyword="mother", display_contacts=True)

    print("Second search".center(50, "*"))
    my_phone.search_contacts(keyword="103", display_contacts=True)
