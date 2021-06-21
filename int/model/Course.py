class Course:
    def __init__(self=None, course_id=None, course_name=None, course_category=None, course_price=None, course_rating=None, instructor=None, discussions=None, is_coupon_enabled=None):
        self.course_id = course_id
        self.course_name = course_name
        self.course_category = course_category
        self.course_price = course_price
        self.course_rating = course_rating
        self.instructor = instructor
        self.discussions = discussions
        self.is_coupon_enabled = is_coupon_enabled
