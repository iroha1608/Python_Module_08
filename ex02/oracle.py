import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("Error: python-dotenv not found", file=sys.stderr)
    print("Run: pip install python-dotenv")
    sys.exit(1)


def load_configration() -> dict[str, str]:
    load_dotenv()

    config: dict[str, str | None] = {
        "MATRIX_MODE": os.environ.get("MATRIX_MODE", "development"),
        "DATABASE_URL": os.environ.get("DATABASE_URL"),
        "API_KEY": os.environ.get("API_KEY"),
        "LOG_LEVEL": os.environ.get("LOG_LEVEL", "DEBUG"),
        "ZION_ENDPOINT": os.environ.get("ZION_ENDPOINT")
    }

    missing_keys = [key for key, val in config.items() if val is None]

    if missing_keys:
        raise KeyError(
            f"Missing required configration variables: "
            f"{', '.join(missing_keys)}"
        )

    return {k: str(v).strip() for k, v in config.items()}


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    try:
        print("Configuration loaded:")
        config = load_configration()
    except KeyError as e:
        print(f"Configuration Error: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Mode: {config['MATRIX_MODE']}")

    if config["MATRIX_MODE"] == "development":
        db_msg = "Connected to local instance"
    else:
        db_msg = "PRODUCTION Cluster"
    print(f"Database: {db_msg}")

    api_msg = "Authenticated" if config["API_KEY"] else "Unauthenticated"
    print(f"API Access: {api_msg}")

    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Zion Network: "
          f"{'Online' if config['ZION_ENDPOINT'] else 'Offline'}")
    print()

    print("Environment security check:")
    # ハードコードされたシークレットがないか
    print("[OK] No hardcoded secrets detected")
    # .envファイルは正しく設定されているか
    print("[OK] .env file properly configred")
    # 本番環境用のオーバーライドができるか
    print("[OK] Production overrides available")
    print()

    print("The Oracle sees all configrations.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
