# === Stage 16: Add argparse support for the most common commands ===
# Project: ProjectArchive
import argparse

def main():
    parser = argparse.ArgumentParser(description="ProjectArchive CLI")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # records command
    rec_parser = subparsers.add_parser('records', help='Manage project records')
    rec_parser.add_argument('--add', '-a', nargs='+', metavar='KEY VALUE', help='Add new record(s)')
    rec_parser.add_argument('--list', '-l', action='store_true', help='List all records')
    
    # decisions command
    dec_parser = subparsers.add_parser('decisions', help='Manage project decisions')
    dec_parser.add_argument('--add', '-a', nargs='+', metavar='KEY VALUE', help='Add decision record')
    dec_parser.add_argument('--list', '-l', action='store_true', help='List all decisions')
    
    # tags command
    tag_parser = subparsers.add_parser('tags', help='Manage project tags')
    tag_parser.add_argument('--add', '-a', nargs='+', metavar='TAG', help='Add new tag(s)')
    tag_parser.add_argument('--remove', '-r', nargs='+', metavar='TAG', help='Remove tag(s)')
    
    # reports command
    rep_parser = subparsers.add_parser('reports', help='Generate project reports')
    rep_parser.add_argument('--type', '-t', choices=['summary', 'timeline'], default='summary', help='Report type')
    rep_parser.add_argument('--output', '-o', metavar='FILE', help='Output file path (default: stdout)')
    
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return
    
    # Placeholder logic for command execution
    print(f"Executing command: {args.command}")
    if hasattr(args, 'add'):
        print(f"Adding items: {args.add}")
    if hasattr(args, 'list'):
        print("Listing items...")
    if hasattr(args, 'remove'):
        print(f"Removing items: {args.remove}")
    if hasattr(args, 'type'):
        print(f"Generating report type: {args.type}")

if __name__ == "__main__":
    main()
