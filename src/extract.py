from pathlib import Path

import pandas as pd


def read_raw_csv(input_path: str) -> pd.DataFrame:
    """
    Lê o arquivo CSV bruto sem aplicar validação ou transformação de negócio.

    Todos os campos são lidos como string para preservar o dado original.
    """

    path = Path(input_path)

    df = pd.read_csv(
        path,
        dtype=str,
        keep_default_na=False
    )

    df["source_file"] = path.name
    df["source_line_number"] = range(2, len(df) + 2)
    df["source_system"] = "rastreador"
    df["source_format"] = "csv"

    return df