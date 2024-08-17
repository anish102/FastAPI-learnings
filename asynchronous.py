import asyncio


async def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    await asyncio.sleep(5)
    print(full_name)


async def print_hello():
    print("Hello")


async def main():
    name_task = asyncio.create_task(get_full_name("John", "Doe"))
    hello_task = asyncio.create_task(print_hello())

    await name_task
    await hello_task


asyncio.run(main())
