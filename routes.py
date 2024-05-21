from flask import Blueprint, render_template, redirect, session, url_for, request
from utils import get_properties, insert_tenant_request, get_property_info, get_tenant_requests

routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route('/')
def home():
    return render_template('index.html')

@routes_blueprint.route('/login')
def login():
    return render_template('login.html')

@routes_blueprint.route('/login', methods=['POST'])
def login_page():
    email = request.form.get('email')
    password = request.form.get('password')
    
    if email == 'admin@gmail.com' and password == 'admin123':
        session['logged_in_agent'] = 'admin@gmail.com'
        return redirect(url_for('routes.admin_page'))
    elif email == 'agent1@gmail.com' and password == 'agent123':
        session['logged_in_agent'] = 'agent1@gmail.com'
        return redirect(url_for('routes.agent_page'))
    elif email == 'agent2@gmail.com' and password == 'agent456':
        session['logged_in_agent'] = 'agent2@gmail.com'
        return redirect(url_for('routes.agent_page'))
    else:
        return render_template('login.html', error='Invalid credentials. Please try again.')

@routes_blueprint.route('/agent_page')
def agent_page():
    if 'logged_in_agent' in session:
        logged_in_agent = session['logged_in_agent']
        tenant_request = get_tenant_requests(logged_in_agent)
        print("Tenant Request Data:", tenant_request)

        if tenant_request is None:
            error_message = "Error fetching tenant requests. Please try again later."
            return render_template('agent_page.html', error_message=error_message)

        return render_template('agent_page.html', tenant_request=tenant_request)
    else:
        return redirect(url_for('routes.login'))

@routes_blueprint.route('/admin_page')
def admin_page():
    tenant_requests = get_tenant_requests(None)

    if tenant_requests is None:
        error_message = "Error fetching tenant requests. Please try again later."
        return render_template('admin_page.html', error_message=error_message)

    return render_template('admin_page.html', tenant_requests=tenant_requests)

@routes_blueprint.route('/properties')
def view_properties():
    properties = get_properties()
    return render_template('properties.html', properties=properties)

@routes_blueprint.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        tenant_name = request.form.get('fullname')
        tenant_email = request.form.get('email')
        location = request.form.get('location')
        property_type = request.form.get('property_type')
        agent_name = request.form.get('agent_name')

        insert_tenant_request(tenant_name, tenant_email, location, property_type, agent_name)

        return redirect(url_for('routes.success'))

    property_id = request.args.get('property_id')
    property_info = get_property_info(property_id)
    return render_template('register.html', property=property_info)

@routes_blueprint.route('/submit_register', methods=['POST'])
def submit_register():
    tenant_name = request.form.get('fullname')
    tenant_email = request.form.get('email')
    location = request.form.get('location')
    property_type = request.form.get('property_type')
    agent_name = request.form.get('agent_name')

    insert_tenant_request(tenant_name, tenant_email, location, property_type, agent_name)

    return redirect(url_for('routes.success'))

@routes_blueprint.route('/success')
def success():
    return render_template('success.html')

@routes_blueprint.route('/logout')
def logout():
    session.pop('logged_in_agent', None)
    return redirect(url_for('routes.login'))