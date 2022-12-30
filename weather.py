# import the module
import python_weather
import asyncio
import os

location = input("Type the city you want to get the weather: ")

async def getweather():

    client = python_weather.Client(format=python_weather.IMPERIAL)

    weather = await client.get(location)

    currentTemp = (weather.current.temperature - 32) * 5/9

    print(f"Temperature outside is {str(round(currentTemp))}°C and {weather.current.description}")

    await client.close()

if __name__ == "__main__":
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(getweather())