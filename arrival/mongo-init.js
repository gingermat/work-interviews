db.auth("root", "example")
db = db.getSiblingDB("test")

db.createUser(
    {
        user: "test_user",
        pwd: "test_password",
        roles: [
            {
                role: "readWrite",
                db: "test"
            }
        ]
    }
);