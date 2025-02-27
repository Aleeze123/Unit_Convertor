import streamlit as st

def convert(value, from_unit, to_unit, conversions):
    value_in_base = value * conversions[from_unit]
    return value_in_base / conversions[to_unit]

# conversion categories..
unit_conversions = {
    'Length': {'m': 1, 'cm': 100, 'mm': 1000, 'km': 0.001, 'inch': 39.3701, 'ft': 3.28084, 'yard': 1.09361, 'mile': 0.000621371},
    'Area': {'m²': 1, 'km²': 0.000001, 'cm²': 10000, 'mm²': 1000000, 'ft²': 10.7639, 'in²': 1550, 'acre': 0.000247105, 'hectare': 0.0001},
    'Data Transfer Rate': {'bps': 1, 'Kbps': 0.001, 'Mbps': 0.000001, 'Gbps': 0.000000001, 'Tbps': 0.000000000001},
    'Digital Storage': {'B': 1, 'KB': 0.001, 'MB': 0.000001, 'GB': 0.000000001, 'TB': 0.000000000001, 'PB': 0.000000000000001},
    'Energy': {'J': 1, 'kJ': 0.001, 'cal': 0.239006, 'kcal': 0.000239006, 'Wh': 0.000277778, 'BTU': 0.000947817},
    'Frequency': {'Hz': 1, 'kHz': 0.001, 'MHz': 0.000001, 'GHz': 0.000000001, 'THz': 0.000000000001},
    'Fuel Economy': {'km/L': 1, 'mpg': 2.35215, 'L/100km': 100},
    'Mass': {'kg': 1, 'g': 1000, 'mg': 1000000, 'lb': 2.20462, 'oz': 35.274, 'ton': 0.001, 'metric_ton': 0.001},
    'Plane Angle': {'degree': 1, 'radian': 0.0174533, 'grad': 1.11111},
    'Pressure': {'Pa': 1, 'kPa': 0.001, 'bar': 0.00001, 'psi': 0.000145038, 'atm': 0.00000986923},
    'Speed': {'m/s': 1, 'km/h': 3.6, 'mph': 2.23694, 'knot': 1.94384},
    'Temperature': {'C': lambda x: x, 'F': lambda x: (x * 9/5) + 32, 'K': lambda x: x + 273.15},
    'Time': {'s': 1, 'min': 1/60, 'h': 1/3600, 'day': 1/86400, 'week': 1/604800, 'month': 1/2592000, 'year': 1/31536000},
    'Volume': {'L': 1, 'mL': 1000, 'cm³': 1000, 'm³': 0.001, 'ft³': 0.0353147, 'gal': 0.264172, 'qt': 1.05669},
}

unit_names = {
    'Length': {'m': 'Meter', 'cm': 'Centimeter', 'mm': 'Millimeter', 'km': 'Kilometer', 'inch': 'Inch', 'ft': 'Foot', 'yard': 'Yard', 'mile': 'Mile'},
    'Area': {'m²': 'Square Meter', 'km²': 'Square Kilometer', 'cm²': 'Square Centimeter', 'mm²': 'Square Millimeter', 'ft²': 'Square Foot', 'in²': 'Square Inch', 'acre': 'Acre', 'hectare': 'Hectare'},
    'Data Transfer Rate': {'bps': 'Bit per Second', 'Kbps': 'Kilobit per Second', 'Mbps': 'Megabit per Second', 'Gbps': 'Gigabit per Second', 'Tbps': 'Terabit per Second'},
    'Digital Storage': {'B': 'Byte', 'KB': 'Kilobyte', 'MB': 'Megabyte', 'GB': 'Gigabyte', 'TB': 'Terabyte', 'PB': 'Petabyte'},
    'Energy': {'J': 'Joule', 'kJ': 'Kilojoule', 'cal': 'Calorie', 'kcal': 'Kilocalorie', 'Wh': 'Watt-hour', 'BTU': 'British Thermal Unit'},
    'Frequency': {'Hz': 'Hertz', 'kHz': 'Kilohertz', 'MHz': 'Megahertz', 'GHz': 'Gigahertz', 'THz': 'Terahertz'},
    'Fuel Economy': {'km/L': 'Kilometer per Liter', 'mpg': 'Miles per Gallon', 'L/100km': 'Liter per 100 Kilometer'},
    'Mass': {'kg': 'Kilogram', 'g': 'Gram', 'mg': 'Milligram', 'lb': 'Pound', 'oz': 'Ounce', 'ton': 'Ton', 'metric_ton': 'Metric Ton'},
    'Plane Angle': {'degree': 'Degree', 'radian': 'Radian', 'grad': 'Gradian'},
    'Pressure': {'Pa': 'Pascal', 'kPa': 'Kilopascal', 'bar': 'Bar', 'psi': 'Pound per Square Inch', 'atm': 'Atmosphere'},
    'Speed': {'m/s': 'Meter per Second', 'km/h': 'Kilometer per Hour', 'mph': 'Miles per Hour', 'knot': 'Knot'},
    'Temperature': {'C': 'Celsius', 'F': 'Fahrenheit', 'K': 'Kelvin'},
    'Time': {'s': 'Second', 'min': 'Minute', 'h': 'Hour', 'day': 'Day', 'week': 'Week', 'month': 'Month', 'year': 'Year'},
    'Volume': {'L': 'Liter', 'mL': 'Milliliter', 'cm³': 'Cubic Centimeter', 'm³': 'Cubic Meter', 'ft³': 'Cubic Foot', 'gal': 'Gallon', 'qt': 'Quart'},
}

st.set_page_config(page_title="Unit Converter", page_icon="🛠️")
st.title("Unit Converter")

if 'history' not in st.session_state:
    st.session_state.history = []

def add_to_history(conversion_result):
    if len(st.session_state.history) >= 5: 
        st.session_state.history.pop(0)
    st.session_state.history.append(conversion_result)

def remove_from_history(index):
    st.session_state.history.pop(index)

conversion_type = st.selectbox(
    "Select Conversion Type 🔽", 
    list(unit_conversions.keys())
)

value = st.number_input("Enter the value:", min_value=0.0, value=1.0)
from_unit = st.selectbox(f"From Unit ({conversion_type})", list(unit_conversions[conversion_type].keys()), format_func=lambda x: unit_names[conversion_type][x])
to_unit = st.selectbox(f"To Unit ({conversion_type})", list(unit_conversions[conversion_type].keys()), format_func=lambda x: unit_names[conversion_type][x])

# Custom button style using CSS
st.markdown("""
    <style>
        .stButton > button {
            border: 2px solid #FFFF00;
            
            font-size: 16px;
        }
        .stButton > button:hover {
         border: 2px solid #FFFF00;
            color: #FFFF00;
        }
    </style>
""", unsafe_allow_html=True)

if st.button("🔄 Convert 🔄"):
    result = convert(value, from_unit, to_unit, unit_conversions[conversion_type])
    conversion_result = f"{value} {unit_names[conversion_type][from_unit]} is equal to {result} {unit_names[conversion_type][to_unit]}"
    st.write(conversion_result)
    add_to_history(conversion_result)

st.sidebar.title("Recent Conversions 📜")
if len(st.session_state.history) == 0:
    st.sidebar.write("No conversions yet. 🤔 Start converting!")
else:
    for idx, history_item in enumerate(reversed(st.session_state.history)):
        col1, col2 = st.sidebar.columns([8, 1])
        col1.write(f"{idx + 1}. {history_item}")
        if col2.button("🗑️", key=f"delete_{idx}"):
            remove_from_history(len(st.session_state.history) - idx - 1)
            st.rerun()
