class Solution:
    def minSpeedOnTime(self, dist, hour):
        """
        Returns the minimum integer speed such that
        total travel time is <= given hour.
        """

        # This function checks whether we can reach
        # within the allowed time using a given speed.
        def can_arrive(speed):

            total_time = 0.0
            # total_time stores the total hours needed
            # to travel all trains at this speed.

            for i in range(len(dist)):

                if i == len(dist) - 1:
                    # -------------------------------
                    # LAST TRAIN
                    # -------------------------------
                    # For the last train, we are allowed
                    # to take fractional time.
                    #
                    # So we use normal division:
                    # time = distance / speed
                    #
                    # Example:
                    # distance = 10, speed = 3
                    # time = 10 / 3 = 3.33 hours
                    #
                    # We DO NOT round up here.
                    total_time += dist[i] / speed

                else:
                    # -------------------------------
                    # ALL OTHER TRAINS
                    # -------------------------------
                    # For every train except the last one,
                    # we must wait until the next full hour.
                    #
                    # That means we need CEIL division.
                    #
                    # Example:
                    # distance = 10, speed = 3
                    # actual time = 3.33 hours
                    # but we must count it as 4 hours.
                    #
                    # Instead of using math.ceil(),
                    # we use this integer formula:
                    #
                    # ceil(a / b) = (a + b - 1) // b
                    #
                    # This avoids floating point errors.
                    total_time += (dist[i] + speed - 1) // speed

            # Return True if total time is within limit
            return total_time <= hour

        # ------------------------------------------------
        # Binary Search on Speed
        # ------------------------------------------------

        low = 1
        high = 10**7  # Maximum possible speed
        answer = -1

        while low <= high:

            mid = (low + high) // 2  # candidate speed

            if can_arrive(mid):
                # If we can reach on time,
                # try smaller speed to minimize it
                answer = mid
                high = mid - 1
            else:
                # If not possible,
                # increase speed
                low = mid + 1

        return answer


# -----------------------------
# Main function to run in IDE
# -----------------------------
if __name__ == "__main__":

    dist = [1, 3, 2]
    hour = 6

    obj = Solution()
    print("Minimum Speed:", obj.minSpeedOnTime(dist, hour))


# Time Complexity: O(n log(10^7))
# Space Complexity: O(1)