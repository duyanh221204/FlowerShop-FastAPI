from schemas.base_response import BaseResponse

ERROR_CODES = {
    100001: "Login failed!",
    100002: "Cannot validate user!",
    100003: "Username existed!",
    100004: "Email existed!",
    100005: "Registration failed!"
}


def raise_error(error_code: int):
    return BaseResponse(
        status="error",
        message=ERROR_CODES[error_code]
    )