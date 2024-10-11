# VolAPI by Guilherme Reis

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to VolAPI! Please check the documentation for help."}

@app.get("/volatility")
async def get_volatility(
        underlying_asset: str = Query("AAPL", min_length=1, max_length=6,
                                      description="Yahoo Finance Symbol for the underlying asset"),
        benchmark_asset: str = Query("SPY", min_length=1, max_length=6,
                                     description="Yahoo Finance Symbol for the benchmark asset"),
        estimator: str = Query("GarmanKlass",
                               description="Volatility estimator to be used. Options: GarmanKlass, "
                                           "HodgesTompkins, Kurtosis, Parkinson, Raw, RogersSatchell, Skew, YangZhang")
):
    valid_estimators = ["GarmanKlass", "HodgesTompkins", "Kurtosis", "Parkinson", "Raw", "RogersSatchell", "Skew",
                        "YangZhang"]

    logger.info(
        f"Received parameters: underlying_asset={underlying_asset}, "
        f"benchmark_asset={benchmark_asset}, estimator={estimator}")

    if estimator not in valid_estimators:
        logger.error(f"Invalid estimator provided: {estimator}")
        raise HTTPException(status_code=400, detail="Invalid estimator provided.")

    try:
        # Dummy implementation for volatility calculation (replace with actual logic)
        volatility_value = calculate_volatility(underlying_asset, benchmark_asset, estimator)

        return JSONResponse(
            content={
                "underlying_asset": underlying_asset,
                "benchmark_asset": benchmark_asset,
                "estimator": estimator,
                "volatility": volatility_value
            })

    except Exception as e:
    logger.error(f"Error during volatility calculation: {str(e)}")
    raise HTTPException(status_code=400, detail=str(e))


def calculate_volatility(underlying_asset: str, benchmark_asset: str, estimator: str) -> float:
    # This is a placeholder function, implement your logic here
    # Example of dummy logic, replace with actual computation
    return 0.25
