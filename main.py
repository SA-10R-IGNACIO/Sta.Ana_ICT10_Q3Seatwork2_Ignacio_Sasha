from js import document
from pyscript import display

def intrams_checker(e):
    document.getElementById("output").innerHTML = ""
    document.getElementById("image").innerHTML = ""

    reg_radio = document.querySelector('input[name="registration"]:checked')
    clear_radio = document.querySelector('input[name="clearance"]:checked')

    if reg_radio is None or clear_radio is None:
        display("Please answer all the questions before signing up.", target="output")
        return

    registration = reg_radio.value
    clearance = clear_radio.value
    grade_level = int(document.getElementById("level").value)
    section = document.getElementById("section").value

    if registration != "registered":
        display(
            "Not eligible: student is not registered for Intrams. Ask your PE teacher regarding the online registration.",
            target="output"
        )
    elif clearance != "cleared":
        display(
            "Not eligible: medical clearance required. Go to the clinic and secure your clearance.",
            target="output"
        )
    elif section == "emerald":
        display("Congratulations! You are part of the Emerald team 💚", target="output")
        document.getElementById("image").innerHTML = '<img src="green hornets.jpg" width="300">'
    elif section == "ruby":
        display("Congratulations! You are part of the Ruby team ❤️", target="output")
        document.getElementById("image").innerHTML = '<img src="yellow tigers.jpg" width="300">'
    elif section == "sapphire":
        display("Congratulations! You are part of the Sapphire team 💙", target="output")
        document.getElementById("image").innerHTML = '<img src="red bulldogs.jpg" width="300">'
    elif section == "topaz":
        display("Congratulations! You are part of the Blue Bears 💙", target="output")
        document.getElementById("image").innerHTML = '<img src="blue bears.jpg" width="300">'
