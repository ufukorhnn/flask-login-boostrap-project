from ..models import ContactRequest


def GetContactList():
    return [
        ["Berk", "Shipping", "High"],
        ["Ufuk", "Administration", "Medium"],
        ["Fırat", "Manufactoring", "Medium"],
        ["Ali", "Shipping", "Low"]
    ]


def SaveContactRequest(name, email, category, priority, message):
    contactRequest = ContactRequest()
    contactRequest.name = name
    contactRequest.email = email
    contactRequest.category = category
    contactRequest.priority = priority
    contactRequest.message = message

    contactRequest.Save()
    print(contactRequest)
