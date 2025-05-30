// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from px4:msg/GimbalManagerStatus.idl
// generated code does not contain a copyright notice

#ifndef PX4__MSG__DETAIL__GIMBAL_MANAGER_STATUS__BUILDER_HPP_
#define PX4__MSG__DETAIL__GIMBAL_MANAGER_STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "px4/msg/detail/gimbal_manager_status__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace px4
{

namespace msg
{

namespace builder
{

class Init_GimbalManagerStatus_secondary_control_compid
{
public:
  explicit Init_GimbalManagerStatus_secondary_control_compid(::px4::msg::GimbalManagerStatus & msg)
  : msg_(msg)
  {}
  ::px4::msg::GimbalManagerStatus secondary_control_compid(::px4::msg::GimbalManagerStatus::_secondary_control_compid_type arg)
  {
    msg_.secondary_control_compid = std::move(arg);
    return std::move(msg_);
  }

private:
  ::px4::msg::GimbalManagerStatus msg_;
};

class Init_GimbalManagerStatus_secondary_control_sysid
{
public:
  explicit Init_GimbalManagerStatus_secondary_control_sysid(::px4::msg::GimbalManagerStatus & msg)
  : msg_(msg)
  {}
  Init_GimbalManagerStatus_secondary_control_compid secondary_control_sysid(::px4::msg::GimbalManagerStatus::_secondary_control_sysid_type arg)
  {
    msg_.secondary_control_sysid = std::move(arg);
    return Init_GimbalManagerStatus_secondary_control_compid(msg_);
  }

private:
  ::px4::msg::GimbalManagerStatus msg_;
};

class Init_GimbalManagerStatus_primary_control_compid
{
public:
  explicit Init_GimbalManagerStatus_primary_control_compid(::px4::msg::GimbalManagerStatus & msg)
  : msg_(msg)
  {}
  Init_GimbalManagerStatus_secondary_control_sysid primary_control_compid(::px4::msg::GimbalManagerStatus::_primary_control_compid_type arg)
  {
    msg_.primary_control_compid = std::move(arg);
    return Init_GimbalManagerStatus_secondary_control_sysid(msg_);
  }

private:
  ::px4::msg::GimbalManagerStatus msg_;
};

class Init_GimbalManagerStatus_primary_control_sysid
{
public:
  explicit Init_GimbalManagerStatus_primary_control_sysid(::px4::msg::GimbalManagerStatus & msg)
  : msg_(msg)
  {}
  Init_GimbalManagerStatus_primary_control_compid primary_control_sysid(::px4::msg::GimbalManagerStatus::_primary_control_sysid_type arg)
  {
    msg_.primary_control_sysid = std::move(arg);
    return Init_GimbalManagerStatus_primary_control_compid(msg_);
  }

private:
  ::px4::msg::GimbalManagerStatus msg_;
};

class Init_GimbalManagerStatus_gimbal_device_id
{
public:
  explicit Init_GimbalManagerStatus_gimbal_device_id(::px4::msg::GimbalManagerStatus & msg)
  : msg_(msg)
  {}
  Init_GimbalManagerStatus_primary_control_sysid gimbal_device_id(::px4::msg::GimbalManagerStatus::_gimbal_device_id_type arg)
  {
    msg_.gimbal_device_id = std::move(arg);
    return Init_GimbalManagerStatus_primary_control_sysid(msg_);
  }

private:
  ::px4::msg::GimbalManagerStatus msg_;
};

class Init_GimbalManagerStatus_flags
{
public:
  explicit Init_GimbalManagerStatus_flags(::px4::msg::GimbalManagerStatus & msg)
  : msg_(msg)
  {}
  Init_GimbalManagerStatus_gimbal_device_id flags(::px4::msg::GimbalManagerStatus::_flags_type arg)
  {
    msg_.flags = std::move(arg);
    return Init_GimbalManagerStatus_gimbal_device_id(msg_);
  }

private:
  ::px4::msg::GimbalManagerStatus msg_;
};

class Init_GimbalManagerStatus_timestamp
{
public:
  Init_GimbalManagerStatus_timestamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GimbalManagerStatus_flags timestamp(::px4::msg::GimbalManagerStatus::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return Init_GimbalManagerStatus_flags(msg_);
  }

private:
  ::px4::msg::GimbalManagerStatus msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::px4::msg::GimbalManagerStatus>()
{
  return px4::msg::builder::Init_GimbalManagerStatus_timestamp();
}

}  // namespace px4

#endif  // PX4__MSG__DETAIL__GIMBAL_MANAGER_STATUS__BUILDER_HPP_
