from app import app
from models import db, User, Recipe

with app.app_context():
    # Clear existing data
    db.drop_all()
    db.create_all()

    # Create users
    u1 = User(
        username='user1',
        bio='I love cooking!',
        image_url='https://example.com/user1.jpg'
    )
    u1.password_hash = 'password1'

    u2 = User(
        username='user2',
        bio='Professional chef',
        image_url='https://example.com/user2.jpg'
    )
    u2.password_hash = 'password2'

    db.session.add_all([u1, u2])
    db.session.commit()

    # Create recipes
    r1 = Recipe(
        title='Pasta Carbonara',
        instructions='1. Cook pasta. 2. Fry bacon. 3. Mix eggs and cheese. 4. Combine everything while hot. 5. Serve immediately. Add more detailed instructions to reach 50 characters.',
        minutes_to_complete=30,
        user_id=u1.id
    )

    r2 = Recipe(
        title='Chocolate Cake',
        instructions='1. Mix dry ingredients. 2. Mix wet ingredients. 3. Combine. 4. Bake at 350°F for 30 minutes. 5. Let cool before frosting. Add more detailed instructions to reach 50 characters.',
        minutes_to_complete=60,
        user_id=u2.id
    )

    db.session.add_all([r1, r2])
    db.session.commit()

    print("Database seeded successfully!")