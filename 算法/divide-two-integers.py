class Solution:

    def divide1(self, dividend: int, divisor: int) -> int:
        sigin=(dividend > 0) ^ (divisor > 0)

        divisor = abs(divisor)
        old_divisor = divisor
        dividend = abs(dividend)

        result=0

        while (divisor<<1) <= dividend:
            divisor <<= 1

        while old_divisor <= divisor:
            result <<= 1
            # print(bin(dividend), bin(divisor))
            if divisor <= dividend:
                dividend -= divisor
                result += 1
            divisor >>= 1


        if sigin:
            result = -result

        return result if -(1<<31) <= result <= (1<<31)-1 else (1<<31)-1


    def divide2(self, dividend: int, divisor: int) -> int:
        sigin = (dividend > 0) ^ (divisor > 0)
        result = 0
        if dividend > 0: dividend = -dividend
        if divisor > 0: divisor = -divisor

        # print(bin(dividend), bin(divisor))
        while dividend <= divisor :
            temp_result = -1
            temp_divisor = divisor
            while dividend <= (temp_divisor << 1):
                temp_result <<= 1
                temp_divisor <<= 1

            dividend -= temp_divisor
            result += temp_result

        if not sigin:
            result = -result

        return result if -(1<<31) <= result <= (1<<31)-1 else (1<<31)-1







s1 = Solution()
# divide = s1.divide1
divide = s1.divide2

print(divide(2147483648,1))
print(divide(-2147483648,1))

