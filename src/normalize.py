import hashlib
from datetime import datetime, timezone

import pandas as pd


def generate_raw_record_id(row: pd.Series) -> str:
    key = "|".join([
        str(row.get("source_file", "")),
        str(row.get("source_line_number", "")),
        str(row.get("DATA_SERVIDOR", "")),
        str(row.get("TM_STAMP", "")),
        str(row.get("MESS_TYPE", "")),
        str(row.get("S/N ou IMEI", "")),
    ])

    return hashlib.sha256(key.encode("utf-8")).hexdigest()


def build_raw_payload(row: pd.Series) -> str:
    """
    Gera uma representação textual simples da linha original.
    Por enquanto, usamos JSON em formato string.
    """

    return row.to_json(force_ascii=False)


def normalize_rastreador_csv(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normaliza o CSV bruto do rastreador para o modelo intermediário
    NormalizedRawRecord.
    """

    normalized_rows = []

    created_at = datetime.now(timezone.utc).isoformat()

    for _, row in df.iterrows():
        normalized_rows.append({
            "raw_record_id": generate_raw_record_id(row),

            "source_system": row.get("source_system"),
            "source_format": row.get("source_format"),
            "source_file": row.get("source_file"),
            "source_line_number": row.get("source_line_number"),

            "raw_payload": build_raw_payload(row),

            "raw_server_timestamp": row.get("DATA_SERVIDOR"),
            "raw_event_timestamp": row.get("TM_STAMP"),
            "raw_message_type": row.get("MESS_TYPE"),
            "raw_device_id": row.get("S/N ou IMEI"),

            "raw_latitude": row.get("LAT"),
            "raw_longitude": row.get("LONT"),
            "raw_speed": row.get("SPEED"),
            "raw_heading": row.get("DIR"),

            "raw_hdop": row.get("HDOP"),
            "raw_odometer": row.get("ODO_TOTAL"),
            "raw_serial_counter": row.get("SER_COUNT"),

            "created_at": created_at,
        })

    return pd.DataFrame(normalized_rows)