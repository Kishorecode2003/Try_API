from schemas import UserBase, TaskCreate
from database import SessionLocal
from crud import UserCRUD, TaskCRUD

def prompt_user(fields):
    data = {}
    for field, field_type in fields.items():
        value = input(f"Enter {field} ({field_type.__name__}): ").strip()
        if field_type == int:
            value = int(value)
        elif field_type == str and value == "":
            value = None
        data[field] = value
    return data


def create_user_cli(db):
    print("\n🧑 Creating User")
    user_data = prompt_user({"username": str})
    user_schema = UserBase(**user_data)
    user = UserCRUD(db).create_user(user_schema)
    print(f"✅ User created: ID={user.id}, Username={user.username}")


def create_task_cli(db):
    print("\n📝 Creating Task")
    task_data = prompt_user({
        "title": str,
        "status": str,
        "user_id": int
    })
    task_schema = TaskCreate(**task_data)
    task = TaskCRUD(db).create_task(task_schema)
    print(f"✅ Task created: ID={task.id}, Title={task.title}, User ID={task.user_id}")


def show_all_users(db):
    users = UserCRUD(db).get_all_users()
    print("\n📋 All Users:")
    for user in users:
        print(f"ID={user.id}, Username={user.username}")


def show_all_tasks(db):
    tasks = TaskCRUD(db).get_all_tasks()
    print("\n📋 All Tasks:")
    for task in tasks:
        print(f"ID={task.id}, Title={task.title}, Status={task.status}, User ID={task.user_id}")


def main():
    db = SessionLocal()
    try:
        while True:
            print("\n===== CLI To-Do Manager =====")
            print("1. Add User")
            print("2. Add Task")
            print("3. View All Users")
            print("4. View All Tasks")
            print("0. Exit")

            choice = input("Select an option: ").strip()
            if choice == "1":
                create_user_cli(db)
            elif choice == "2":
                create_task_cli(db)
            elif choice == "3":
                show_all_users(db)
            elif choice == "4":
                show_all_tasks(db)
            elif choice == "0":
                print("👋 Exiting...")
                break
            else:
                print("❌ Invalid option. Try again.")
    finally:
        db.close()


if __name__ == "__main__":
    main()
