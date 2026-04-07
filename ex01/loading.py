import sys


def check_dependencies() -> bool:
    print("LOADING STATUS: Loading programs...")
    print()

    print("Checking dependencies:")
    program_ready_flag = True

    try:
        import pandas
        print(
            f"[OK] pandas ({pandas.__version__}) - Data manipulation ready"
        )
    except ImportError:
        print("[FAIL] pandas is missing")
        program_ready_flag = False

    try:
        import requests
        print(
            f"[OK] requests ({requests.__version__}) - Network access ready"
        )
    except ImportError:
        print("[FAIL] requests is missing")
        program_ready_flag = False

    try:
        import matplotlib
        print(
            f"[OK] matplotllib ({matplotlib.__version__}) "
            f"- Visualization ready"
        )
    except ImportError:
        print("[FAIL] matplotlib is missing", file=sys.stderr)
        program_ready_flag = False

    try:
        import numpy
        print(f"[OK] numpy ({numpy.__version__})")
    except ImportError:
        print("[FAIL] numpy is missing", file=sys.stderr)
        program_ready_flag = False

    print()
    return program_ready_flag


def run_analysis() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    num_points = 1000
    # numpy.random.randn 標準正規分布に従って配列(ndarray)に保存し返す
    # data = np.random.randn(num_points)
    # cumsum() 累積し配列に保存 -> 折れ線グラフに最適化
    data = np.random.randn(num_points).cumsum()
    df = pd.DataFrame({"Signal": data})

    print("Analyzing Matrix data...")
    print(f"Processing {num_points} data points...")
    print("Generating visualization...")
    print()

    # matplotlib.pyplot.figure() 生成する画像の縦*横の比率
    plt.figure(figsize=(10, 6))

    # alpha=0~1 濃さ
    # matplotlib.pyplot.plot() 折れ線グラフ
    plt.plot(df["Signal"], color="green", alpha=0.7)
    # matplotlib.pyplot.hist() ヒストグラフ
    # plt.hist(df["Signal"])

    # matplotlib.pyplot.title 生成する画像内に表示するタイトル
    plt.title("Matrix Signal Analysis")

    # 背景にうっすらあるグリッド
    # linestyle= "-", "--", "-.", ":", "None", " ", ""...
    plt.grid(True, linestyle=":", alpha=0.5)

    # 作成するファイル
    output_file = "matrix_analysis.png"
    # ファイルに保存
    plt.savefig(output_file)
    # クローズ
    plt.close()

    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


def main() -> None:
    if not check_dependencies():
        print("Error: Missing required dependencies.")
        print("Please install theem using pip or poetry.")
        sys.exit(1)

    run_analysis()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
