from molotov import scenario

@scenario(weight=1)
async def test_server(session):
    async with session.get("http://127.0.0.1:8000") as resp:
        assert resp.status == 200
        data = await resp.json()
        assert isinstance(data, dict)
        print("✅ Server returned JSON with 200 OK")
