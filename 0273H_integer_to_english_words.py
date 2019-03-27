class Solution(object):
    def numberToWords(self, num):
        if num is 0:
            return "Zero"
        # 2^31 ~ 2 billion
        res = []

        if 10**9 <= num < 10**12:
            group = num/10**9
            res.extend(three_to_words(group))
            res.append("Billion")
            num = num - (num/10**9)*10**9

        if 10**6 <= num < 10**9:
            group = num/10**6
            res.extend(three_to_words(group))
            res.append("Million")
            num = num - (num/10**6)*10**6

        if 10**3 <= num < 10**6:
            group = num/10**3
            res.extend(three_to_words(group))
            res.append("Thousand")
            num = num - (num/10**3)*10**3

        res.extend(three_to_words(num))

        return " ".join(res).strip()

def three_to_words(num):
    res = []
    ones = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}
    teens = {0:"", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine",                      10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 
            16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen"}
    tens = {2:"Twenty", 3:"Thirty", 4:"Forty", 5:"Fifty", 6:"Sixty", 7:"Seventy", 8:"Eighty", 9:"Ninety"}

    # hundreds
    if 100 <= num < 1000:
        digit = num / 100
        res.append(ones[digit])
        res.append("Hundred")
        num = num - (num / 100)*100

    # tens
    if 20 <= num < 100:
        digit = num / 10
        res.append(tens[digit])
        num = num - (num / 10)*10

    # teens
    if 0 < num <= 19:
        res.append(teens[num])

    return res
