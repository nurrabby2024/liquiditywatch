"""Minimal example for LiquidityWatch."""

from liquiditywatch import liquiditywatch


def main():
 runner = liquiditywatch({"name": "LiquidityWatch", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()