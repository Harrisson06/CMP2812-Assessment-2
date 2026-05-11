# CMP2812-Assessment-2
Full Stack Development
FAST API Assessment

## Initialisation

1. Create database and tables:
   `mysql -u root -p < schema/nyspd.sql`

2. Activate Python environment and install dependencies:
   `pip install -r requirements.txt`

3. Seed the users table with test accounts:
   `python -m seed.seed_users`

4. Start the API:
   `uvicorn app.main:app --reload`

## Test Accounts

| Email | Password | Role |
|---|---|---|
| admin@test.com    | Admin123  | Admin   |
| Citizen1@test.com | Driver123 | Citizen |
| Citizen2@test.com | Driver123 | Citizen |