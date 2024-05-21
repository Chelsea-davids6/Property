import sqlite3

def get_properties():
    conn = sqlite3.connect('properties.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM properties')
    properties = cursor.fetchall()
    conn.close()
    return properties

import sqlite3

def get_property_info(property_id):
    try:
        conn = sqlite3.connect('properties.db')
        cursor = conn.cursor()
        cursor.execute('SELECT property_name, property_type, agent_name FROM properties WHERE id = ?', (property_id,))
        property_info = cursor.fetchone()
        return property_info
    except sqlite3.Error as e:
        print(f"Error fetching property information: {e}")
        return None
    finally:
        if conn:
            conn.close()


def get_user(email, password, name):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT email, password, type, name FROM users WHERE email=? AND password=? AND name=?', (email, password, name))
    user = cursor.fetchone()
    conn.close()
    return user



def get_tenant_requests(agent_name):
    try:
            
        conn = sqlite3.connect('tenant_request.db')
        cursor = conn.cursor()
        if agent_name == None:
            cursor.execute('SELECT tenant_name, tenant_email, location, property_type, agent_name FROM tenant_request')
        else:
            cursor.execute('SELECT tenant_name, tenant_email, location, property_type, agent_name FROM tenant_request WHERE agent_name = ?', (agent_name,))
        tenant_request = cursor.fetchall()
        return tenant_request
    except sqlite3.Error as e:
        print(f"Error fetching tenant requests: {e}")
        return None  
    finally:
        if conn:
            conn.close()




def insert_tenant_request(tenant_name, tenant_email, location, property_type, agent_name):
    try:
        conn = sqlite3.connect('tenant_request.db')
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO tenant_request (tenant_name, tenant_email, location, property_type, agent_name)
        VALUES (?, ?, ?, ?, ?)
        ''', (tenant_name, tenant_email, location, property_type, agent_name))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting data into tenant_request table: {e}")
    finally:
        if conn:
            conn.close()
