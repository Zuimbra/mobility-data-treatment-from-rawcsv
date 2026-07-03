from extract import read_raw_csv
from load import save_intermediate_records
from normalize import normalize_rastreador_csv


def main():
    input_path = "data/raw/logs_rastreador_2026-07-01.csv"
    output_path = "data/intermediate/normalized_raw_records.csv"

    print("Mobility Data Treatment")
    print("Sprint 2: leitura e normalização do dado bruto")

    raw_df = read_raw_csv(input_path)
    print(f"Registros brutos lidos: {len(raw_df)}")

    normalized_df = normalize_rastreador_csv(raw_df)
    print(f"Registros normalizados: {len(normalized_df)}")

    save_intermediate_records(normalized_df, output_path)
    print(f"Arquivo intermediário salvo em: {output_path}")


if __name__ == "__main__":
    main()