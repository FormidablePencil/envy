import argparse
from database.database import Database

def main():
    parser = argparse.ArgumentParser(description='Database CLI')
    subparsers = parser.add_subparsers(dest='command')

    # Tasks
    task_parser = subparsers.add_parser('tasks')
    task_parser.add_argument('--create', nargs=3, metavar=('TITLE', 'DESCRIPTION', 'COMPLETED_AT'), help='Create a new task')
    task_parser.add_argument('--list', action='store_true', help='List all tasks')

    # Implementation Details
    detail_parser = subparsers.add_parser('details')
    detail_parser.add_argument('--create', nargs=2, metavar=('COMPONENT', 'DESCRIPTION'), help='Create a new implementation detail')
    detail_parser.add_argument('--list', action='store_true', help='List all implementation details')

    # Completion Records
    record_parser = subparsers.add_parser('records')
    record_parser.add_argument('--create', nargs=3, metavar=('TASK_ID', 'COMPLETED_AT', 'RELATED_TASKS'), help='Create a new completion record')
    record_parser.add_argument('--list', action='store_true', help='List all completion records')

    # Coordination Capabilities
    capability_parser = subparsers.add_parser('capabilities')
    capability_parser.add_argument('--create', nargs=2, metavar=('NAME', 'DESCRIPTION'), help='Create a new coordination capability')
    capability_parser.add_argument('--list', action='store_true', help='List all coordination capabilities')

    args = parser.parse_args()

    db = Database()

    if args.command == 'tasks':
        if args.create:
            task = {"title": args.create[0], "description": args.create[1]}
            task_id = db.commit_task(task, args.create[2], "", "")
            print(f"Created task: {args.create[0]} - {args.create[1]} (ID: {task_id})")
        elif args.list:
            tasks = db.get_tasks()
            for task in tasks:
                print(f"{task['id']} - {task['title']} - {task['description']}")

    elif args.command == 'details':
        if args.create:
            detail = {"component": args.create[0], "description": args.create[1]}
            db.create_implementation_detail(detail)
            print(f"Created implementation detail: {args.create[0]} - {args.create[1]}")
        elif args.list:
            details = db.get_implementation_details()
            for detail in details:
                print(f"{detail['id']} - {detail['component']} - {detail['description']}")

    elif args.command == 'records':
        if args.create:
            db.create_completion_record(int(args.create[0]), args.create[1], args.create[2], "")
            print(f"Created completion record: Task {args.create[0]} - Completed at {args.create[1]} - Related tasks: {args.create[2]}")
        elif args.list:
            records = db.get_completion_records()
            for record in records:
                print(f"Task {record['task_id']} - Completed at {record['completed_at']} - Related tasks: {record['related_tasks']} - Impact notes: {record['impact_notes']}")

    elif args.command == 'capabilities':
        if args.create:
            capability = {"name": args.create[0], "description": args.create[1]}
            db.create_coordination_capability(capability)
            print(f"Created coordination capability: {args.create[0]} - {args.create[1]}")
        elif args.list:
            capabilities = db.get_coordination_capabilities()
            for capability in capabilities:
                print(f"{capability['id']} - {capability['name']} - {capability['description']}")

if __name__ == '__main__':
    main()