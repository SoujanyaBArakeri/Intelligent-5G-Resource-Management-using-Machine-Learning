from flask import Flask, request, jsonify
from flask_cors import CORS
from db_config import db, cursor
from model import predict_power

app = Flask(__name__)

# Enable CORS
CORS(app)


# ---------------- HOME ----------------
@app.route('/')
def home():
    return "5G Network Slicing Optimization Backend Running"


# ---------------- LOGIN + NETWORK SLICING ----------------
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()

        username = data.get('username').strip()
        password = data.get('password').strip()

        query = """
        SELECT role FROM users
        WHERE TRIM(username)=%s AND TRIM(password)=%s
        """

        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            role = result[0]

            # ✅ Automatic Network Slice Assignment
            if role == "admin":
                slice_name = "URLLC"   # High priority
            elif role == "operator":
                slice_name = "eMBB"    # Multimedia
            else:
                slice_name = "mMTC"    # IoT / Normal users

            return jsonify({
                "message": "Login Successful",
                "role": role,
                "slice": slice_name
            })

        return jsonify({"message": "Invalid Login"})

    except Exception as e:
        return jsonify({"error": str(e)})


# ---------------- NETWORK SIMULATION ----------------
@app.route('/network', methods=['POST'])
def network():
    try:
        data = request.get_json()

        bandwidth = float(data.get('bandwidth'))
        latency = float(data.get('latency'))
        signal = float(data.get('signal'))
        users = float(data.get('users'))
        slice_name = data.get('slice')

        # ✅ Slice Based Resource Control
        if slice_name == "URLLC":
            priority = "High Priority"
            bandwidth *= 1.2

        elif slice_name == "eMBB":
            priority = "Medium Priority"

        else:
            priority = "Low Priority"
            bandwidth *= 0.8

        query = """
        INSERT INTO network_data
        (bandwidth, latency, signal_strength, connected_users)
        VALUES (%s,%s,%s,%s)
        """

        cursor.execute(query,
                       (bandwidth, latency, signal, users))
        db.commit()

        return jsonify({
            "message": "Network Data Stored Successfully",
            "priority": priority
        })

    except Exception as e:
        return jsonify({"error": str(e)})


# ---------------- POWER OPTIMIZATION ----------------
@app.route('/optimize', methods=['POST'])
def optimize():
    try:
        data = request.get_json()

        distance = float(data.get('distance'))
        users = float(data.get('users'))
        slice_name = data.get('slice')

        # ✅ Machine Learning Prediction
        power = predict_power(distance, users)

        # ✅ Slice-Based Power Adjustment
        if slice_name == "URLLC":
            power *= 1.2   # reliability boost
        elif slice_name == "mMTC":
            power *= 0.8   # energy saving

        query = """
        INSERT INTO power_allocation
        (network_id, allocated_power, transmission_time)
        VALUES (%s,%s,%s)
        """

        cursor.execute(query, (1, power, 2.5))
        db.commit()

        return jsonify({
            "optimized_power": round(power, 2),
            "slice_used": slice_name
        })

    except Exception as e:
        return jsonify({"error": str(e)})


# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(debug=True)