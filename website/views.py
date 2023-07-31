from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from website.models import ControlPointsData
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('search.html')

@views.route('/general')
def general():
    data = ControlPointsData.query.all()
    serialized_data = []

    for item in data:
        serialized_item = {
            'point_id': item.point_id,
            'arch1960_eastings': item.arch1960_eastings,
            'arch1960_northings': item.arch1960_northings,
            'latitude': item.latitude,
            'longitude': item.longitude,
            'heights': item.heights,
            'monument_status': item.monument_status,
            'usage': item.usage,
            'image_description': item.image_description,
            'satellite_image': item.satellite_image,
            'wgs84_eastings': item.wgs84_eastings,
            'wgs84_northings': item.wgs84_northings
        }
        serialized_data.append(serialized_item)

    return render_template('general.html', data=serialized_data)



@views.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        point_id = request.form.get('search')
        point_id = point_id.upper()
        return redirect(url_for('views.control_point', point_id=point_id))
    else:
        search_term = request.args.get('search', '').strip()
        search_term = search_term.upper()
        if search_term:
            results = ControlPointsData.query.filter(ControlPointsData.point_id.like(f'%{search_term}%')).limit(10).all()
            suggestions = [result.point_id for result in results]
        else:
            suggestions = []
        return jsonify({'suggestions': suggestions})

@views.route('/control_point/<point_id>')
def control_point(point_id):
    control_point_data = ControlPointsData.query.filter_by(point_id=point_id).first()
    if control_point_data:
        return render_template('details.html', control_point_data=control_point_data)
        
    else:
        return redirect(url_for('views.home'))
