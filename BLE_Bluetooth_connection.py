import asyncio
from bleak import BleakScanner

async def main():
    scanner = BleakScanner()
    devices = await scanner.discover(timeout=5)
    print(devices)

asyncio.run(main())