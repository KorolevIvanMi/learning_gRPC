// Простая инициализация replica set
try {
    rs.status();
} catch (e) {
    if (e.codeName === 'NoReplicationEnabled') {
        rs.initiate({
            _id: "rs0",
            members: [{ _id: 0, host: "localhost:27017" }]
        });
        print("Replica set initiated");
    }
}

// Создаем пользователя
db = db.getSiblingDB('catalog_db');
try {
    db.createUser({
        user: "admin_user",
        pwd: "kWaf3983gd18fnr",
        roles: [
            { role: "readWrite", db: "catalog_db" }
        ]
    });
} catch (e) {
    // Пользователь уже существует
}