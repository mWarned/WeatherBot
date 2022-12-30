from aiogram import Bot, Dispatcher, executor, types
import python_weather


#bot init
bot = Bot(token="5974861219:AAE2iRD4kY_YQs-FwHeZ1XYL31nsN5C7CkU")
dp = Dispatcher(bot)
client = python_weather.Client(format=python_weather.IMPERIAL)

#echo
@dp.message_handler()
async def echo(message: types.Message):
    weather = await client.get(message.text)
    currentTemp = (weather.current.temperature - 32) * 5 / 9

    resp_msg = f"Current temperature is {round(currentTemp)}°C\n"
    resp_msg += f"Weather status - {weather.current.description}"

    if currentTemp <= 10:
        resp_msg += "\n\nCold"
    else :
        resp_msg += "\n\nWarm"

    await message.answer(resp_msg)

#run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
