from pyscript import write, Element

class Classmate:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def introduce(self):
        return f"{self.name} –  {self.subject}"



classmates = [
    Classmate("Balagat, Michael", "SCI, ENG"),
    Classmate("Bernardo, Miko", "N/A"),
    Classmate("Caguiron, Carriena", "N/A"),
    Classmate("Calida, Lorenzo", "N/A"),
    Classmate("Chan, Jazmar", "SS, PE"),
    Classmate("Cruz, Rohann", "N/A"),
    Classmate("David, Terd", "SS, SCI"),
    Classmate("De Guzman, Nia", "Science"),
    Classmate("De Guzman, Uno", "SS, Math"),
    Classmate("Francisco, Annika", "PE, English"),
    Classmate("Kaur, Nav", "N/A"),
    Classmate("Laconsay, Heleina", "N/A"),
    Classmate("Lepasana, Khen", "PE"),
    Classmate("Lopez, Liam", "N/A"),
    Classmate("Lucman, Mohammad", "N/A"),
    Classmate("Malapitan, Caleb", "N/A"),
    Classmate("Manahan, Samantha", "SCI"),
    Classmate("Manuel, Elyze", "SCI, Math"),
    Classmate("Mendoza, Matthew", "SS, PE"),
    Classmate("Palafox, Coby", "PE, SS"),
    Classmate("Ramirez, Alfiona", "Math"),
    Classmate("Reynoso, Izeck", "N/A"),
    Classmate("Santos, Cas", "PE"),
    Classmate("Santos, Rafa", "SS"),
    Classmate("Tolentino, Kelsey", "N/A"),
    Classmate("Toribio, Sasha", "N/A"),
    Classmate("Valdez, David", "PE, SCI")
]


def show_list():
    output = ""
    for c in classmates:
        output += c.introduce() + "<br>"
    write("output", output)


def add_classmate():
    name = Element("name").value
    subject = Element("subject").value

    classmates.append(Classmate(name, subject))
    show_list()