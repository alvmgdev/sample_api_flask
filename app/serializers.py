from app import ma
from app.models import User
from marshmallow import post_load


class UserSchema(ma.Schema):
    username = ma.Str(required=True)
    email = ma.Email(required=True)

    class Meta:
        fields = ('username', 'email')

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)


user_schema = UserSchema()
users_schema = UserSchema(many=True)
