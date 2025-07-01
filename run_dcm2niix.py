#!/usr/bin/env python3
import flywheel

fw = flywheel.Client()
project = fw.lookup('hafemanlab/BEAM2')
gear = fw.lookup('gears/dcm2niix/2.1.2_1.0.20240202')

subject_ids = ['1155', '1164', '1167', '1170', '1172', '1168', '1173', '1178', '1177', '1180', '1184', '1183']

for sub in project.subjects():
    if sub.label not in subject_ids:
        continue

    print(f"Subject: {sub.label}")
    for ses in sub.sessions():
        print(f"  Session: {ses.label}")
        for acq in ses.acquisitions():
            dicom_files = [f for f in acq.files if f.type == 'dicom']
            if not dicom_files:
                continue

            file = dicom_files[0]
            print(f"    Launching dcm2niix on acquisition: {acq.label}")
            print(f"    Using file: {file.name}")

            inputs = {'dcm2niix_input': file}
            config = {}

            try:
                gear.run(
                    inputs=inputs,
                    config=config,
                    destination=acq
                )
            except Exception as e:
                print(f"    Failed to launch: {e}")

