from fastapi import FastAPI
from solana_memecoin_scanner import scan_and_build_df

app = FastAPI(
    title="Solana Memecoin Scanner API",
    description="REST API untuk Solana Memecoin Scanner",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Solana Memecoin Scanner API",
        "docs": "/docs"
 }


@app.get("/scan")
def scan():

    for _ in range(3):
        df = scan_and_build_df()

        if not df.empty:
            return {
                "success": True,
                "total": len(df),
                "data": df.to_dict(orient="records")
            }

        time.sleep(2)

    return {
        "success": False,
        "message": "Scanner is warming up. Please try again in a few seconds.",
        "total": 0,
        "data": []
    }

@app.get("/health")
def health():
    return {
        "status": "OK"
    }