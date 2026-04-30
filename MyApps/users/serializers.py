from django.db import transaction
from django.db.models import Q
from rest_framework import serializers

from .models import AppUser, Notification, Role, SystemAudit, UserRole


class AppUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    password_hash = serializers.CharField(write_only=True, required=False)
    role = serializers.CharField(write_only=True, required=False)
    roles = serializers.SerializerMethodField()

    class Meta:
        model = AppUser
        fields = (
            "id",
            "home",
            "full_name",
            "username",
            "email",
            "password",
            "password_hash",
            "phone",
            "is_active",
            "registration_date",
            "last_access",
            "recovery_token",
            "role",
            "roles",
        )
        read_only_fields = ("id", "registration_date", "last_access", "roles")
        extra_kwargs = {
            "recovery_token": {"write_only": True, "required": False},
        }

    def get_roles(self, obj):
        return list(obj.user_roles.values_list("role__role_name", flat=True))

    def validate(self, attrs):
        if self.instance is None:
            if not attrs.get("password") and not attrs.get("password_hash"):
                raise serializers.ValidationError(
                    {"password": "Este campo es requerido."}
                )

            if not attrs.get("role"):
                raise serializers.ValidationError({"role": "Este campo es requerido."})

        return attrs

    def create(self, validated_data):
        role_name = validated_data.pop("role")
        password = validated_data.pop("password", None)
        password_hash = validated_data.pop("password_hash", None)

        with transaction.atomic():
            user = AppUser(**validated_data)
            user.set_password(password or password_hash)
            user.save()
            role = self._get_or_create_role(role_name)
            UserRole.objects.create(user=user, role=role)

        return user

    def update(self, instance, validated_data):
        role_name = validated_data.pop("role", None)
        password = validated_data.pop("password", None)
        password_hash = validated_data.pop("password_hash", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password or password_hash:
            instance.set_password(password or password_hash)

        with transaction.atomic():
            instance.save()

            if role_name:
                role = self._get_or_create_role(role_name)
                instance.user_roles.all().delete()
                UserRole.objects.create(user=instance, role=role)

        return instance

    def _get_or_create_role(self, role_name):
        role_name = role_name.strip()

        if not role_name:
            raise serializers.ValidationError(
                {"role": "Este campo no puede estar vacio."}
            )

        role = Role.objects.filter(role_name__iexact=role_name).first()

        if role:
            return role

        return Role.objects.create(
            role_name=role_name.lower(),
            description=f"Rol {role_name}",
            access_level=100 if role_name.lower() == "admin" else 1,
        )


class AppUserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        identifier = attrs.get("username") or attrs.get("email")

        if not identifier:
            raise serializers.ValidationError(
                {"username": "Envia username o email para iniciar sesion."}
            )

        user = AppUser.objects.filter(
            Q(username__iexact=identifier) | Q(email__iexact=identifier)
        ).first()

        if not user or not user.check_password(attrs["password"]):
            raise serializers.ValidationError("Credenciales invalidas.")

        if not user.is_active:
            raise serializers.ValidationError("Usuario inactivo.")

        attrs["user"] = user
        return attrs


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = "__all__"


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"


class SystemAuditSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemAudit
        fields = "__all__"
