import flywheel

fw = flywheel.Client()
project = fw.lookup('hafemanlab/BEAM2')

# Try to find subject that contains '1155'
subject = next((s for s in project.subjects() if '1155' in s.label), None)

if subject is None:
    print("Subject 1155 not found.")
else:
    print(f"Subject ID: {subject.id} | Label: {subject.label}")

    sessions = subject.sessions()
    for session in sessions:
        print(f"\n  Session: {session.label} (ID: {session.id})")

        acquisitions = session.acquisitions()
        for acq in acquisitions:
            print(f"    Acquisition: {acq.label}")
            for f in acq.files:
                print(f"      File: {f.name} | Type: {f.type}")

