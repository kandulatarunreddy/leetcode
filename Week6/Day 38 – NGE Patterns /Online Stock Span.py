class StockSpanner:

    def __init__(self):
        # stack stores (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        span = 1

        # Merge spans of previous smaller prices
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            span += prev_span

        # Push current price and its span
        self.stack.append((price, span))

        return span


if __name__ == "__main__":
    prices = [100, 80, 60, 70, 60, 75, 85]

    obj = StockSpanner()

    print("Prices:", prices)
    print("Spans:")

    for p in prices:
        print(obj.next(p))

# TC: O(1) amortized per call, SC: O(n)