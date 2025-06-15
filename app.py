
from flask import Flask, make_response, request
from flask_migrate import Migrate

from models import db, Hero, Power, HeroPower

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/heroes', methods=["GET"])
def get_heroes():

    heroes = []

    for hero in Hero.query.all():
        heroes.append(hero.to_dict())

    return make_response(heroes, 200)

@app.route('/heroes/<int:id>', methods=["GET"])
def get_hero_by_id(id):
    hero = Hero.query.get(id)

    if hero:
        return make_response(hero.to_dict(), 200)
    else:
        return make_response({"error": "Hero not found"}, 404)

@app.route('/powers', methods=["GET"])
def get_powers():
    powers = []

    for power in Power.query.all():
        powers.append(power.to_dict())

    return make_response(powers, 200)

@app.route('/powers/<int:id>', methods=["GET"])
def get_power_by_id(id):
    power = Power.query.get(id)

    if power:
        return make_response(power.to_dict(), 200)
    else:
        return make_response({"error": "Power not found"}, 404)

@app.route('/powers/<int:id>/<string:new_description>', methods=["PATCH"])
def update_power_description(id, new_description):
    power = Power.query.get(id)

    if not power:
        return make_response({"error": "Power not found"}, 404)

    if len(new_description) < 20:
        return make_response({"errors": ["description must be at least 20 characters long"]}, 400)

    power.description = new_description
    db.session.commit()

    return make_response(power.to_dict(), 200)

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    new_hero_power = HeroPower(
        strength=request.form.get('strength'),
        hero_id=request.form.get('hero_id'),
        power_id=request.form.get('power_id')
    )

    
    if new_hero_power.strength not in ['Strong', 'Weak', 'Average']:
        return make_response({"errors": ["Invalid strength value"]}, 400)
    
    db.session.add(new_hero_power)
    db.session.commit()
    new_hero_power_dict = new_hero_power.to_dict()
    return make_response(new_hero_power_dict, 201)


if __name__ == '__main__':
    app.run(port=5555, debug=True)