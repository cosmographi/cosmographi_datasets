import os

from jax import numpy as jnp
import numpy as np
import pandas as pd

from typing import List, TypedDict


class RubinThroughput(TypedDict):
    bands: List[str]
    w_hardware: jnp.ndarray
    T_hardware: jnp.ndarray
    w_atmosphere: jnp.ndarray
    T_atmosphere: jnp.ndarray
    air_mass: float


def load_rubin_throughput(abspath: str) -> RubinThroughput:
    """Read in data from ```abspath``` and return derived properties as a typed dictionary.

    :param abspath: The absolute path to the data on the local filesystem.
    :type abspath: str
    """

    bands = ["u", "g", "r", "i", "z", "y"]
    w_hardware = []
    T_hardware = []
    for b in bands:
        df = pd.read_csv(
            os.path.join(abspath, f"lsst_hardware_{b}.csv"),
            names=["w", "T"],
            comment="#",
        )
        w_hardware.append(df["w"].values)
        T_hardware.append(df["T"].values)
    w_hardware = np.stack(w_hardware)
    T_hardware = np.stack(T_hardware)
    df = pd.read_csv(os.path.join(abspath, "lsst_atmos_10.csv"), names=["w", "T"], comment="#")
    w_atmosphere = df["w"].values
    T_atmosphere = df["T"].values

    return {
        "bands": bands,
        "w_hardware": jnp.array(w_hardware),
        "T_hardware": jnp.array(T_hardware),
        "w_atmosphere": jnp.array(w_atmosphere),
        "T_atmosphere": jnp.array(T_atmosphere),
        "air_mass": 1.2,
    }
