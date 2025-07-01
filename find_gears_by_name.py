import flywheel

fw = flywheel.Client()

gears = fw.gears()

for gear in gears:
    name = gear.gear.name
    version = gear.gear.version
    print(f"{name:<30} {version}")

