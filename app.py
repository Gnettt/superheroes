from flask import Flask, request, make_response
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/heroes', methods=["GET"])
def get_heroes():
    heroes = [hero.to_dict() for hero in Hero.query.all()]
    return make_response(heroes, 200)

@app.route('/heroes/<int:id>', methods=["GET"])
def get_hero_by_id(id):
    hero = Hero.query.get(id)
    if hero:
        return make_response(hero.to_dict(), 200)
    return make_response({"error": "Hero not found"}, 404)

@app.route('/powers', methods=["GET"])
def get_powers():
    powers = [power.to_dict() for power in Power.query.all()]
    return make_response(powers, 200)

@app.route('/powers/<int:id>', methods=["GET"])
def get_power_by_id(id):
    power = Power.query.get(id)
    if power:
        return make_response(power.to_dict(), 200)
    return make_response({"error": "Power not found"}, 404)

@app.route('/powers/<int:id>', methods=["PATCH"])
def update_power_description(id):
    power = Power.query.get(id)
    if not power:
        return make_response({"error": "Power not found"}, 404)

    data = request.get_json()
    description = data.get("description")

    if not description or len(description.strip()) < 20:
        return make_response({"errors": ["description must be at least 20 characters long"]}, 400)

    power.description = description
    db.session.commit()
    return make_response(power.to_dict(), 200)

@app.route('/hero_powers', methods=["POST"])
def create_hero_power():
    data = request.get_json()
    strength = data.get('strength')
    hero_id = data.get('hero_id')
    power_id = data.get('power_id')

    if strength not in ['Strong', 'Weak', 'Average']:
        return make_response({"errors": ["Strength must be 'Strong', 'Weak', or 'Average'"]}, 400)

    new_hero_power = HeroPower(strength=strength, hero_id=hero_id, power_id=power_id)
    db.session.add(new_hero_power)
    db.session.commit()

    return make_response(new_hero_power.to_dict(), 201)

if __name__ == '__main__':
    app.run(port=5555, debug=True)