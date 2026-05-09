from app.db.session import SessionLocal
from app.models.User import User
from app.core.security import hash_password


# Each entry uses an existing drivers license from the drivers seed data
# So Citizen account will see violations on their dashboard 
USERS_TO_SEED = [
    {
        "email": "admin@test.com",
        "password": "Password1",
        "role": "Admin",
        "OfficerID": 1,
        "drivers_license": None,
    },
    {
        "email": "officer.test@test.com",
        "password": "Password1",
        "role": "Officer",
        "OfficerID": 3,
        "drivers_license": None,
    },
    {
        "email": "Citizen@test.com",
        "password": "Password1",
        "role": "Citizen",
        "OfficerID": None,
        "drivers_license": 822895210,
    },
    {
        "email": "Citizen@test.com",
        "password": "Password1",
        "role": "Citizen",
        "OfficerID": None, 
        "drivers_license": 49641347,
    },
]

def seed_users() -> None:
    db = SessionLocal()
    try: 
        created = 0
        skipped = 0

        for entry in USERS_TO_SEED:
            existing = db.query(User).filter(User.email == entry["email"]).first()
            if existing:
                print(f" -> skipped (already exists): {entry['email']}")
                skipped += 1
                continue

            user = user(
                email=entry["email"],
                password_hash=hash_password(entry["password"]),
                role=entry["role"],
                OfficerID=entry["OfficerID"],
                drivers_license=entry["drivers_license"],
            )
            db.add(user)
            created += 1
            print(f" -> created {entry['email']} ({entry['role']})")

        db.commit()
        created += 1
        print(f"\nDone. Created {created}, skipped {skipped}.")

    except Exception as e:
        db.rollback()
        print(f"\nSeed Failed: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    print("seeding users...\n")
    seed_users()