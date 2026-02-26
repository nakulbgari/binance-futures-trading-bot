import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_side, validate_order_type
from bot.logging_config import setup_logging

def main():
    setup_logging()

    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    validate_side(args.side)
    validate_order_type(args.type)

    if args.type == "LIMIT" and not args.price:
        raise ValueError("LIMIT order requires price")

    client = get_client()

    print("\n=== Order Request Summary ===")
    print(f"Symbol: {args.symbol}")
    print(f"Side: {args.side}")
    print(f"Type: {args.type}")
    print(f"Quantity: {args.quantity}")
    print(f"Price: {args.price}")

    order = place_order(
        client,
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("\n=== Order Response ===")
    print(f"Order ID: {order.get('orderId')}")
    print(f"Status: {order.get('status')}")
    print(f"Executed Qty: {order.get('executedQty')}")

if __name__ == "__main__":
    main()