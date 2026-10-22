
from pyscript import document

# 
gr7 = {"John Lennon", "Irene Velasco", "Lance Cruz", "Paul Reyes"}
gr8 = {"Andrea Geronimo", "Isabelle Lim", "Charlize Juan", "Aaron de Guzman"}
gr9 = {"Neil Guzman", "Eliana Darjuan", "Korn de Leon"}
gr10 = {"David Denum", "Elijah Herrero"}

# Combining
all_members = gr7 | gr8 | gr9 | gr10


# Function ? ithink
def getData(event=None):

    # names
    first = document.getElementById("first").value.strip()
    last = document.getElementById("last").value.strip()

    # new member
    if first and last:
        all_members.add(f"{first} {last}".title())

    # alphabetically
    members_list = "<br>".join(sorted(all_members))

    # full
    document.getElementById("output1").innerHTML = f"""
        <b>ALL MEMBERS:</b><br>
        {members_list}
        <br><br>
        TOTAL MEMBERS: {len(all_members)}
    """
