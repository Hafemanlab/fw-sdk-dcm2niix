import flywheel

fw = flywheel.Client()
project = fw.lookup('hafemanlab/BEAM2')

print("Subjects in BEAM2:")
for sub in project.subjects():
    print(f"- {sub.label}")

