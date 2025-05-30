// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from px4:msg/VehicleLocalPositionSetpoint.idl
// generated code does not contain a copyright notice

#ifndef PX4__MSG__DETAIL__VEHICLE_LOCAL_POSITION_SETPOINT__BUILDER_HPP_
#define PX4__MSG__DETAIL__VEHICLE_LOCAL_POSITION_SETPOINT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "px4/msg/detail/vehicle_local_position_setpoint__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace px4
{

namespace msg
{

namespace builder
{

class Init_VehicleLocalPositionSetpoint_yawspeed
{
public:
  explicit Init_VehicleLocalPositionSetpoint_yawspeed(::px4::msg::VehicleLocalPositionSetpoint & msg)
  : msg_(msg)
  {}
  ::px4::msg::VehicleLocalPositionSetpoint yawspeed(::px4::msg::VehicleLocalPositionSetpoint::_yawspeed_type arg)
  {
    msg_.yawspeed = std::move(arg);
    return std::move(msg_);
  }

private:
  ::px4::msg::VehicleLocalPositionSetpoint msg_;
};

class Init_VehicleLocalPositionSetpoint_yaw
{
public:
  explicit Init_VehicleLocalPositionSetpoint_yaw(::px4::msg::VehicleLocalPositionSetpoint & msg)
  : msg_(msg)
  {}
  Init_VehicleLocalPositionSetpoint_yawspeed yaw(::px4::msg::VehicleLocalPositionSetpoint::_yaw_type arg)
  {
    msg_.yaw = std::move(arg);
    return Init_VehicleLocalPositionSetpoint_yawspeed(msg_);
  }

private:
  ::px4::msg::VehicleLocalPositionSetpoint msg_;
};

class Init_VehicleLocalPositionSetpoint_thrust
{
public:
  explicit Init_VehicleLocalPositionSetpoint_thrust(::px4::msg::VehicleLocalPositionSetpoint & msg)
  : msg_(msg)
  {}
  Init_VehicleLocalPositionSetpoint_yaw thrust(::px4::msg::VehicleLocalPositionSetpoint::_thrust_type arg)
  {
    msg_.thrust = std::move(arg);
    return Init_VehicleLocalPositionSetpoint_yaw(msg_);
  }

private:
  ::px4::msg::VehicleLocalPositionSetpoint msg_;
};

class Init_VehicleLocalPositionSetpoint_acceleration
{
public:
  explicit Init_VehicleLocalPositionSetpoint_acceleration(::px4::msg::VehicleLocalPositionSetpoint & msg)
  : msg_(msg)
  {}
  Init_VehicleLocalPositionSetpoint_thrust acceleration(::px4::msg::VehicleLocalPositionSetpoint::_acceleration_type arg)
  {
    msg_.acceleration = std::move(arg);
    return Init_VehicleLocalPositionSetpoint_thrust(msg_);
  }

private:
  ::px4::msg::VehicleLocalPositionSetpoint msg_;
};

class Init_VehicleLocalPositionSetpoint_vz
{
public:
  explicit Init_VehicleLocalPositionSetpoint_vz(::px4::msg::VehicleLocalPositionSetpoint & msg)
  : msg_(msg)
  {}
  Init_VehicleLocalPositionSetpoint_acceleration vz(::px4::msg::VehicleLocalPositionSetpoint::_vz_type arg)
  {
    msg_.vz = std::move(arg);
    return Init_VehicleLocalPositionSetpoint_acceleration(msg_);
  }

private:
  ::px4::msg::VehicleLocalPositionSetpoint msg_;
};

class Init_VehicleLocalPositionSetpoint_vy
{
public:
  explicit Init_VehicleLocalPositionSetpoint_vy(::px4::msg::VehicleLocalPositionSetpoint & msg)
  : msg_(msg)
  {}
  Init_VehicleLocalPositionSetpoint_vz vy(::px4::msg::VehicleLocalPositionSetpoint::_vy_type arg)
  {
    msg_.vy = std::move(arg);
    return Init_VehicleLocalPositionSetpoint_vz(msg_);
  }

private:
  ::px4::msg::VehicleLocalPositionSetpoint msg_;
};

class Init_VehicleLocalPositionSetpoint_vx
{
public:
  explicit Init_VehicleLocalPositionSetpoint_vx(::px4::msg::VehicleLocalPositionSetpoint & msg)
  : msg_(msg)
  {}
  Init_VehicleLocalPositionSetpoint_vy vx(::px4::msg::VehicleLocalPositionSetpoint::_vx_type arg)
  {
    msg_.vx = std::move(arg);
    return Init_VehicleLocalPositionSetpoint_vy(msg_);
  }

private:
  ::px4::msg::VehicleLocalPositionSetpoint msg_;
};

class Init_VehicleLocalPositionSetpoint_z
{
public:
  explicit Init_VehicleLocalPositionSetpoint_z(::px4::msg::VehicleLocalPositionSetpoint & msg)
  : msg_(msg)
  {}
  Init_VehicleLocalPositionSetpoint_vx z(::px4::msg::VehicleLocalPositionSetpoint::_z_type arg)
  {
    msg_.z = std::move(arg);
    return Init_VehicleLocalPositionSetpoint_vx(msg_);
  }

private:
  ::px4::msg::VehicleLocalPositionSetpoint msg_;
};

class Init_VehicleLocalPositionSetpoint_y
{
public:
  explicit Init_VehicleLocalPositionSetpoint_y(::px4::msg::VehicleLocalPositionSetpoint & msg)
  : msg_(msg)
  {}
  Init_VehicleLocalPositionSetpoint_z y(::px4::msg::VehicleLocalPositionSetpoint::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_VehicleLocalPositionSetpoint_z(msg_);
  }

private:
  ::px4::msg::VehicleLocalPositionSetpoint msg_;
};

class Init_VehicleLocalPositionSetpoint_x
{
public:
  explicit Init_VehicleLocalPositionSetpoint_x(::px4::msg::VehicleLocalPositionSetpoint & msg)
  : msg_(msg)
  {}
  Init_VehicleLocalPositionSetpoint_y x(::px4::msg::VehicleLocalPositionSetpoint::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_VehicleLocalPositionSetpoint_y(msg_);
  }

private:
  ::px4::msg::VehicleLocalPositionSetpoint msg_;
};

class Init_VehicleLocalPositionSetpoint_timestamp
{
public:
  Init_VehicleLocalPositionSetpoint_timestamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_VehicleLocalPositionSetpoint_x timestamp(::px4::msg::VehicleLocalPositionSetpoint::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return Init_VehicleLocalPositionSetpoint_x(msg_);
  }

private:
  ::px4::msg::VehicleLocalPositionSetpoint msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::px4::msg::VehicleLocalPositionSetpoint>()
{
  return px4::msg::builder::Init_VehicleLocalPositionSetpoint_timestamp();
}

}  // namespace px4

#endif  // PX4__MSG__DETAIL__VEHICLE_LOCAL_POSITION_SETPOINT__BUILDER_HPP_
