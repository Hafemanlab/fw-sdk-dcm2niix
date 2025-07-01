#!/usr/bin/env python3
import flywheel

# Connect to Flywheel
fw = flywheel.Client()
project = fw.lookup('hafemanlab/BEAM2')
gear = fw.lookup('gears/curate-bids/2.2.14_1.2.28')

# Template file
template = None
for file in project.files:
    if file.name == 'beam2-project-template.json':
        template = file
        break

# Target subject IDs (no prefix assumption)
subject_ids = ['1155', '1164', '1167', '1170', '1172', '1168', '1173', '1178', '1177', '1180', '1184', '1183']

# Loop through subjects that match IDs
for sub in project.subjects():
    if sub.label not in subject_ids:
        continue

    print(f"\nSubject: {sub.label}")
    for ses in sub.sessions():
        print(f"  Session: {ses.label}")

        # Check for .json and .nii.gz files
        found_json = False
        found_nii = False
        for acq in ses.acquisitions():
            for f in acq.files:
                if f.name.endswith('.json'):
                    found_json = True
                elif f.name.endswith('.nii.gz'):
                    found_nii = True
            if found_json and found_nii:
                break

        if not (found_json and found_nii):
            print(f"    Skipping: no NIfTI+JSON found in session")
            continue

        # Prepare inputs and config
        inputs = {}
        if template:
            inputs['template'] = template

        config = {
            'base_template': 'reproin',
            'verbosity': 'INFO'
        }

        print(f"    Launching curate-bids on session: {ses.label}")
        gear.run(
            inputs=inputs,
            config=config,
            destination=ses
        )

