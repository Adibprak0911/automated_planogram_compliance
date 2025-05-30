// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from px4:msg/VehicleMagnetometer.idl
// generated code does not contain a copyright notice

#ifndef PX4__MSG__DETAIL__VEHICLE_MAGNETOMETER__BUILDER_HPP_
#define PX4__MSG__DETAIL__VEHICLE_MAGNETOMETER__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "px4/msg/detail/vehicle_magnetometer__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace px4
{

namespace msg
{

namespace builder
{

class Init_VehicleMagnetometer_calibration_count
{
public:
  explicit Init_VehicleMagnetometer_calibration_count(::px4::msg::VehicleMagnetometer & msg)
  : msg_(msg)
  {}
  ::px4::msg::VehicleMagnetometer calibration_count(::px4::msg::VehicleMagnetometer::_calibration_count_type arg)
  {
    msg_.calibration_count = std::move(arg);
    return std::move(msg_);
  }

private:
  ::px4::msg::VehicleMagnetometer msg_;
};

class Init_VehicleMagnetometer_magnetometer_ga
{
public:
  explicit Init_VehicleMagnetometer_magnetometer_ga(::px4::msg::VehicleMagnetometer & msg)
  : msg_(msg)
  {}
  Init_VehicleMagnetometer_calibration_count magnetometer_ga(::px4::msg::VehicleMagnetometer::_magnetometer_ga_type arg)
  {
    msg_.magnetometer_ga = std::move(arg);
    return Init_VehicleMagnetometer_calibration_count(msg_);
  }

private:
  ::px4::msg::VehicleMagnetometer msg_;
};

class Init_VehicleMagnetometer_device_id
{
public:
  explicit Init_VehicleMagnetometer_device_id(::px4::msg::VehicleMagnetometer & msg)
  : msg_(msg)
  {}
  Init_VehicleMagnetometer_magnetometer_ga device_id(::px4::msg::VehicleMagnetometer::_device_id_type arg)
  {
    msg_.device_id = std::move(arg);
    return Init_VehicleMagnetometer_magnetometer_ga(msg_);
  }

private:
  ::px4::msg::VehicleMagnetometer msg_;
};

class Init_VehicleMagnetometer_timestamp_sample
{
public:
  explicit Init_VehicleMagnetometer_timestamp_sample(::px4::msg::VehicleMagnetometer & msg)
  : msg_(msg)
  {}
  Init_VehicleMagnetometer_device_id timestamp_sample(::px4::msg::VehicleMagnetometer::_timestamp_sample_type arg)
  {
    msg_.timestamp_sample = std::move(arg);
    return Init_VehicleMagnetometer_device_id(msg_);
  }

private:
  ::px4::msg::VehicleMagnetometer msg_;
};

class Init_VehicleMagnetometer_timestamp
{
public:
  Init_VehicleMagnetometer_timestamp()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_VehicleMagnetometer_timestamp_sample timestamp(::px4::msg::VehicleMagnetometer::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return Init_VehicleMagnetometer_timestamp_sample(msg_);
  }

private:
  ::px4::msg::VehicleMagnetometer msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::px4::msg::VehicleMagnetometer>()
{
  return px4::msg::builder::Init_VehicleMagnetometer_timestamp();
}

}  // namespace px4

#endif  // PX4__MSG__DETAIL__VEHICLE_MAGNETOMETER__BUILDER_HPP_
