"""
WeatherLink v2 API - Basic Usage Example

Simple and direct example showing the core functionality of weatherlinkv2.
"""

import os
from dotenv import load_dotenv
from weatherlinkv2 import WeatherLinkAPI, parse_weather_data

def main():
    """Basic example demonstrating weatherlinkv2 usage"""

    # Read environment variables from .env file
    load_dotenv()

    # Set your API credentials here or use environment variables
    api_key = os.getenv('WEATHERLINK_API_KEY', 'your_api_key_here')
    api_secret = os.getenv('WEATHERLINK_API_SECRET', 'your_api_secret_here')

    # Check API credentials
    if not api_key or not api_secret or api_key == 'your_api_key_here' or api_secret == 'your_api_secret_here':
        print("❌ API credentials are missing")
        return

    # Initialize API in demo mode (for testing)
    api = WeatherLinkAPI(api_key, api_secret, demo_mode=True)
    print("✅ API initialized in demo mode")
    
    # Test connection
    if api.test_connection():
        print("✅ Connection successful")
    else:
        print("❌ Connection failed")
        return
    
    # Get available stations
    stations = api.get_stations()
    print(f"📍 Found {len(stations)} stations")
    
    # Get current weather data
    current_data = api.get_current_data()
    print(f"🌡️  Current data: {len(current_data.get('sensors', []))} sensors")
    
    # Get sensors information
    sensors = api.get_sensors()
    print(f" Available sensors: {len(sensors)}")
    
    # Get historical data (last 24 hours)
    historic_data = api.get_historic_data(hours_back=24)
    print(f"� Historic data: {len(historic_data.get('sensors', []))} sensors")
    
    # Parse data into pandas DataFrame
    df = parse_weather_data(historic_data, 323, 17)
    print(f"✅ Parsed {len(df)} weather records")
    
    if not df.empty:
        print(f"📅 Data range: {df.index.min()} to {df.index.max()}")

        # Display available columns
        print(f"📊 Available data columns: {list(df.columns)}")
        
        # Show basic statistics for temperature if available
        if 'temperature_c' in df.columns:
            temp = df['temperature_c'].dropna()
            if not temp.empty:
                print(f"🌡️  Temperature: {temp.mean():.1f}°C avg, {temp.min():.1f}°C - {temp.max():.1f}°C")
    
    print("\n🎉 Basic example completed!")


if __name__ == "__main__":
    main()
