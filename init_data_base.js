db = db.getSiblingDB('catalog_db');

db.createUser({
    user: "admin_user",
    pwd: "kWaf3983gd18fnr",
    roles: [
    { role: "readWrite", db: "catalog_db" }

    ]
});

if (!db.getCollectionNames().includes("products")) {
    db.createCollection("products");
}

if (!db.getCollectionNames().includes("reviews")) {
    db.createCollection("reviews");
}
print("MongoDB initialization completed!");