from pyscript import document, display

gr7 = {"john lennon", "irene velasco", "lance cruz", "paul reyes"}
gr8 ={"andrea geronimo", "isabelle lim", "charlize juan", "aaron de guzman" }
gr9 = {"neil guzman", "eliana darjuan", "korn de leon"}
gr10 = {"david denum", "elijah herrero"}
newmembers = {"rohan way", "ynigo garcia"}

display(gr7|gr8|gr9|gr10|{newmembers}, target = "output1")
