import json
import os


def import_incidents():
    if os.path.exists('incidents.json'):
        with open('incidents.json', 'r') as file:
            data = json.load(file)
    else:
        data = {"incidents": []}
        with open('incidents.json', 'w') as file:
            json.dump(data, file)
    return data


def export_incidents(data):
    with open('incidents.json', 'w') as f:
        json.dump(data, f, indent=2)


def view_all_incidents(data):
    print("\nINCIDENT SUMMARY")
    print("-" * 30)
    for x in data['incidents']:
        print_incidents(
            x['id'], x['service'], x['issue_type'],
            x['status'], x['start_time'], x['end_time']
        )
    print("-" * 30)


def view_open_incidents(data):
    print("\nOPEN INCIDENTS")
    print("-" * 30)
    for x in data['incidents']:
        if x['status'] == 'open' and x['end_time'] is None:
            print_incidents(
                x['id'], x['service'], x['issue_type'],
                x['status'], x['start_time'], x['end_time']
            )
    print("-" * 30)


def view_resolved_incidents(data):
    print("\nRESOLVED INCIDENTS")
    print("-" * 30)
    for x in data['incidents']:
        if x['status'] == 'resolved' and x['end_time'] is not None:
            print_incidents(
                x['id'], x['service'], x['issue_type'],
                x['status'], x['start_time'], x['end_time']
            )
    print("-" * 30)


def print_incidents(id, service, issue_type, status, start_time, end_time):
    print(f"""
Incident ID: {id}
  Service:      {service}
  Issue Type:   {issue_type}
  Status:       {status}
  Start Time:   {start_time}
  End Time:     {end_time}
  Downtime:     {calculate_downtime(start_time, end_time)}
""")


def calculate_downtime(start_time, end_time):
    if end_time is None:
        return "N/A"
    return end_time - start_time


def id_number():
    file_path = 'id.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            ticket_id = json.load(file)
        ticket_id += 1
    else:
        ticket_id = 1

    with open(file_path, 'w') as file:
        json.dump(ticket_id, file)

    return ticket_id


def report_incident(data):
    while True:
        choice = input("\nWould you like to report a new incident? (yes/no): ").lower()
        if choice == "no":
            break

        service = input("Enter service name: ").strip().lower()
        issue_type = input("Enter issue type: ").strip().lower()

        while True:
            status = input("Status (open / resolved): ").strip().lower()
            if status in ('open', 'resolved'):
                break
            print("Invalid status. Please enter 'open' or 'resolved'.")

        while True:
            start_time = input("Start time (positive number): ").strip()
            if start_time.isdigit() and int(start_time) >= 0:
                start_time = int(start_time)
                break
            print("Invalid input. Please enter a positive number.")

        while True:
            end_time = input("End time (leave blank if open): ").strip()
            if end_time == "":
                end_time = None
                break
            if end_time.isdigit() and int(end_time) >= 0:
                end_time = int(end_time)
                break
            print("Invalid input. Enter a positive number or leave blank.")

        incident = {
            "id": id_number(),
            "service": service,
            "issue_type": issue_type,
            "status": status,
            "start_time": start_time,
            "end_time": end_time
        }

        data['incidents'].append(incident)
        export_incidents(data)
        print("✅ Incident successfully recorded.")


def view_incident_report():
    while True:
        print("""
HOME MENU
------------------------
1. Report an incident
2. View all incidents
3. View open incidents
4. View resolved incidents
5. Exit
------------------------
""")
        choice = input("Select an option (1–5): ").strip()
        data = import_incidents()

        if choice == "1":
            report_incident(data)
        elif choice == "2":
            view_all_incidents(data)
        elif choice == "3":
            view_open_incidents(data)
        elif choice == "4":
            view_resolved_incidents(data)
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid selection. Please choose 1–5.")


view_incident_report()




