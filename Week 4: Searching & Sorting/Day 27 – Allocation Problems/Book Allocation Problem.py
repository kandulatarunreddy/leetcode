class Solution:
    def allocateMinimumPages(self, pages, m):
        """
        Allocates books to m students such that
        the maximum number of pages assigned to any student is minimized.
        """

        n = len(pages)

        # If students are more than books,
        # we cannot give at least one book to each student.
        if m > n:
            return -1

        # ------------------------------------------------------------
        # WHY low = max(pages)?
        # ------------------------------------------------------------
        # Because:
        # Each student must get at least one book.
        # The student who gets the book with the maximum pages
        # must at least handle that many pages.
        #
        # Example:
        # pages = [10, 20, 30, 40]
        #
        # Even if we distribute optimally,
        # someone must take the book with 40 pages.
        #
        # So answer can NEVER be less than max(pages).
        #
        low = max(pages)

        # ------------------------------------------------------------
        # WHY high = sum(pages)?
        # ------------------------------------------------------------
        # This represents the worst-case scenario.
        #
        # Worst case:
        # Only ONE student takes ALL books.
        #
        # Example:
        # pages = [10, 20, 30, 40]
        # Total pages = 100
        #
        # If m = 1:
        # That one student must take all books → 100 pages.
        #
        # Even if m > 1, during binary search,
        # sum(pages) is the maximum possible upper bound.
        #
        high = sum(pages)

        # Helper function to check feasibility
        def can_allocate(max_pages):
            student_count = 1
            current_sum = 0

            for page in pages:

                # If adding this book exceeds max_pages,
                # assign books to next student
                if current_sum + page > max_pages:
                    student_count += 1
                    current_sum = page

                    # If students exceed m,
                    # this max_pages is too small
                    if student_count > m:
                        return False
                else:
                    current_sum += page

            return True

        result = high  # store answer

        # ------------------------------------------------------------
        # Binary Search on the answer range [low, high]
        # ------------------------------------------------------------
        while low <= high:
            mid = (low + high) // 2  # candidate maximum pages

            if can_allocate(mid):
                # If allocation is possible,
                # try to minimize further
                result = mid
                high = mid - 1
            else:
                # If not possible,
                # increase allowed maximum
                low = mid + 1

        return result


# Example Usage
if __name__ == "__main__":
    pages = [12, 34, 67, 90]
    m = 2

    obj = Solution()
    print("Minimum possible maximum pages:", obj.allocateMinimumPages(pages, m))

# Time Complexity: O(n log(sum(pages)))
# Space Complexity: O(1)