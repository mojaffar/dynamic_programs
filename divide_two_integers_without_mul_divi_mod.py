class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        d = abs(dividend)
        dv = abs(divisor)
        count = 0

        while d>=dv:
            tmp = dv
            mul = 1
            while d >= tmp:
                d -=tmp
                count +=mul
                mul +=mul # doubling the multiplier
                tmp +=tmp # doubling the divisor chunk

        # Adjust the sign of the result.
        if (dividend < 0 <= divisor) or (dividend >= 0 > divisor):
            count = -count

        # Handle overflow conditions.
        if count > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if count < -2 ** 31:
            return -2 ** 31

        return count  # Final return for the computed result




dividend = 10
divisor = 3
sol = Solution()
print(sol.divide(dividend, divisor))
