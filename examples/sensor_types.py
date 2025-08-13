"""
WeatherLink v2 API - Sensor Types Example

Shows how to work with different sensor types and their specific data.
"""

import os
from dotenv import load_dotenv
from weatherlinkv2 import WeatherLinkAPI, parse_weather_data

def main():
    """Example showing different sensor types"""

    # Read environment variables from .env file
    load_dotenv()

    # Initialize API
    api_key = os.getenv('WEATHERLINK_API_KEY', 'your_api_key_here')
    api_secret = os.getenv('WEATHERLINK_API_SECRET', 'your_api_secret_here')
    
    api = WeatherLinkAPI(api_key, api_secret, demo_mode=True)
    print("✅ API initialized")
    
    # Get all sensors
    sensors = api.get_sensors()
    print(f"📊 Found {len(sensors)} sensors")
    
    # Group sensors by type
    sensor_types = {}
    for sensor in sensors:
        sensor_type = sensor.get('sensor_type', 'Unknown')
        if sensor_type not in sensor_types:
            sensor_types[sensor_type] = []
        sensor_types[sensor_type].append(sensor)
    
    print(f"\n🔍 Sensor types found:")
    for sensor_type, sensors_list in sensor_types.items():
        print(f"   Type {sensor_type}: {len(sensors_list)} sensors")
        
    # Select any lsid from a sensor
    sample_lsid = sensors[0].get('lsid', 'Unknown')

    # Get detailed sensor information
    sensors_info = api.get_sensors_info(sample_lsid)
    print(f"\n📋 Detailed sensor information of the sensor: {sensors_info.get('product_name', 'Unknown')}")

    if sensors_info:
        sensor_type = sensors_info.get('sensor_type', 'Unknown')
        lsid = sensors_info.get('lsid', 'Unknown')
        manufacturer = sensors_info.get('manufacturer', 'Unknown')
        product_name = sensors_info.get('product_name', 'Unknown')

        print(f"   Sensor {lsid}:")
        print(f"     Type: {sensor_type}")
        print(f"     Product: {manufacturer} {product_name}")
    
    # Get historical data
    historic_data = api.get_historic_data(hours_back=24)
    
    # Parse data for different sensor types
    
    # AirLink sensor data (type 323)
    print(f"\n🌫️  AirLink sensor data (type 323):")
    df_airlink = parse_weather_data(historic_data, sensor_type=323)
    if not df_airlink.empty:
        print(f"   Records: {len(df_airlink)}")
        print(f"   Columns: {list(df_airlink.columns)}")
        
        # Show air quality data if available
        if 'pm25_ugm3' in df_airlink.columns:
            pm25 = df_airlink['pm25_ugm3'].dropna()
            if not pm25.empty:
                print(f"   PM2.5 average: {pm25.mean():.1f} μg/m³")
    else:
        print("   No AirLink data available")

if __name__ == "__main__":
    main()
