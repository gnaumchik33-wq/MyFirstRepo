import asyncio
import python_weather

async def get_weather():
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather = await client.get('Pinsk')

        print(f"Tемпература: {weather.temperature} °C")
        print(f"Описание: {weather.description}")

asyncio.run(get_weather())