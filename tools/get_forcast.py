
from typing import Dict, List, Tuple

def register(mcp):
 @mcp.tool()   
 def get_coordinates(city: str) -> Tuple[float, float]:
    """
    Returns the latitude and longitude of the specified city as a tuple.
     Args:
        city: the city of 
    """
    # Hardcode replace it with you api to get the latitude and longitude of any city
    return (37.7749, -122.4194)
    
 @mcp.tool()
 def get_forecast(latitude: float, longitude: float) -> str:
    """Get weather forecast for a location.
    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
    """

    forecasts = [
    {
        "name": "This Afternoon",
        "temperature": "68°F",
        "wind": "18 mph WSW",
        "forecast": "Sunny. High near 68, with temperatures falling to around 66 in the afternoon. West southwest wind around 18 mph, with gusts as high as 23 mph."
    },
    {
        "name": "Tonight",
        "temperature": "55°F",
        "wind": "8 to 17 mph WSW",
        "forecast": "Mostly clear, with a low around 55. West southwest wind 8 to 17 mph, with gusts as high as 22 mph."
    },
   
    ]
      # Hardcode replace it with you api , you can call https://api.weather.gov ... 
    return format_forecast(forecasts)



def format_forecast(forecasts: List[Dict]) -> str:
        """
        Format a list of forecast dictionaries into a readable string.
        """
        return "\n---\n".join(
            f"{f['name']}:\nTemperature: {f['temperature']}\nWind: {f['wind']}\nForecast: {f['forecast']}"
            for f in forecasts
        )