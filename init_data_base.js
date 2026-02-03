// Авторизуемся как root
db.getSiblingDB('admin').auth('admin', 'admin');

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
    print("User created");
} catch (e) {
    // Пользователь уже существует
    print("User already exists");
}