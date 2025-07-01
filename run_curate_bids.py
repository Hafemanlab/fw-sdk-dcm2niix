#!/usr/bin/env python3
import flywheel

fw = flywheel.Client()
project = fw.lookup('hafemanlab/BEAM2')
gear = fw.lookup('gears/curate-bids/2.2.14_1.2.28')

subject_ids = ['1155', '1164', '1167', '1170', '1172', '1168', '1173', '1178', '1177', '1180', '1184', '1183']

for sub in project.subjects():
    if sub.label not in subject_ids:
        continue

    print(f"Subject: {sub.label}")
    for ses in sub.sessions():
        print(f"  Session: {ses.label}")
        
        # Skip if no NIfTI or DICOM outputs in the session
        has_dcm2niix_output = any(
            f.name.endswith(".nii.gz") or f.name.endswith(".json")
            for acq in ses.acquisitions()
            for f in acq.files
        )
        if not has_dcm2niix_output:
            print("    Skipping: no NIfTI or sidecar files found.")
            continue

        config = {
            "base_template": "reproin"
        }

        try:
            print("    Launching curate-bids...")
            gear.run(
                inputs={},  # no file input required
                config=config,
                destination=ses
            )
        except Exception as e:
            print(f"    Failed to launch: {e}")

