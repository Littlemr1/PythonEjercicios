class Solution(object):
    def validUtf8(self, data):
        """
        starts with 0, then skip
        start with 1, check number of numbers
        :type data: List[int]
        :rtype: bool
        """
        required = 0
        for d in data:
            if d & 0x80 == 0:
                if required != 0:
                    return False
            else:
                one_cnt = 0
                while d & 0x80 == 0x80:
                    one_cnt += 1
                    d <<= 1

                if required != 0:
                    if one_cnt != 1:
                        return False
                    required -= 1
                else:
                    if one_cnt == 1:
                        return False
                    required += (one_cnt - 1)

        return required == 0


if __name__ == "__main__":
    assert Solution().validUtf8([197, 130, 1]) == True
    assert Solution().validUtf8([235, 140, 4]) == False
