<div align="center">

# KTC API

</div>

## Install
```bash
pip install ktc-api
```


## Usage
### Sync
```python
from ktc_api import KTCClient

client = KTCClient()
print(client.actual_version())
```
### Async
```python
from asyncio import new_event_loop
from ktc_api.aio import AKTCClient

async def main():
    client = AKTCClient()
    print(await client.actual_version())
    await client.close()

if __name__ == '__main__':
    loop = new_event_loop()
    loop.run_until_complete(main())
    loop.close()
```