import flywheel

fw = flywheel.Client()

# Get gear object
gear = fw.lookup('gears/curate-bids/2.2.14_1.2.28')

# Print gear input requirements
print("Inputs:")
for key, val in gear.gear.inputs.items():
    print(f"  {key}: base={val['base']}, optional={val.get('optional', False)}")

print("\nConfig options:")
for key, val in gear.gear.config.items():
    print(f"  {key}: type={val['type']}, default={val.get('default', 'None')}, optional={val.get('optional', False)}")

