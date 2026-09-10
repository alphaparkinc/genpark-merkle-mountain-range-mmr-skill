from client import MMRAccumulator
import json

def handle_request(req):
    mmr = MMRAccumulator()
    action = req.get("action")
    if action == "append_batch":
        items = req.get("items", [])
        for it in items:
            mmr.append(str(it))
        return {
            "status": "ok",
            "bagged_root": mmr.get_bagged_root(),
            "peak_count": mmr.peak_count()
        }
    return {"status": "error", "message": "Unknown action"}

if __name__ == "__main__":
    print(json.dumps(handle_request({"action": "append_batch", "items": ["a", "b", "c"]})))
