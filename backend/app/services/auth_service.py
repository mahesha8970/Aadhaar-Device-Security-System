from app.config.database import users_collection
from app.config.security import hash_password, verify_password, create_access_token
from app.schemas.user import UserRegister, UserLogin


class AuthService:

    @staticmethod
    async def register_user(user: UserRegister):

        # Check if email already exists
        existing_user = await users_collection.find_one(
            {"email": user.email}
        )

        if existing_user:
            return {
                "success": False,
                "message": "Email already registered"
            }

        # Convert user data to dictionary
        user_data = user.dict()

        # Hash password
        user_data["password"] = hash_password(user.password)

        # Default values
        user_data["role"] = "user"
        user_data["is_verified"] = False

        # Save user
        await users_collection.insert_one(user_data)

        return {
            "success": True,
            "message": "Registration Successful"
        }

    @staticmethod
    async def login_user(user: UserLogin):

        # Find user by email
        existing_user = await users_collection.find_one(
            {"email": user.email}
        )

        if not existing_user:
            return {
                "success": False,
                "message": "User not found"
            }

        # Verify password
        if not verify_password(
            user.password,
            existing_user["password"]
        ):
            return {
                "success": False,
                "message": "Invalid password"
            }

        # Generate JWT Token
        token = create_access_token(
            {"sub": existing_user["email"]}
        )

        return {
            "success": True,
            "message": "Login Successful",
            "access_token": token,
            "token_type": "bearer"
        }