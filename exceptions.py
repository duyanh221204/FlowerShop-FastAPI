from schemas.base_response import BaseResponse

ERROR_CODES = {
    1: "For sellers only",
    2: "For customers only",

    100001: "Login failed!",
    100002: "Cannot validate user!",
    100003: "Username existed!",
    100004: "Email existed!",
    100005: "Registration failed!",
    100006: "Incorrect current password!",
    100007: "Error on password change!",

    200001: "Cannot get flower!",
    200002: "Cannot create flower!",
    200003: "Flower not found!",
    200004: "Flower existed!",
    200005: "Cannot update flower!",
    200006: "Cannot delete flower!",

    300001: "Cannot get order!",
    300002: "Cannot create order!",
    300003: "Order not found!"
}


def raise_error(error_code: int) -> BaseResponse:
    return BaseResponse(
        status="error",
        message=ERROR_CODES[error_code]
    )